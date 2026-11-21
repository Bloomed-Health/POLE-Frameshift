#!/usr/bin/env python3
"""Read-level checks on the patient's 47-gene panel BAM/CRAM. Runs locally; nothing leaves the machine.

Needs: Python >= 3.9 and samtools >= 1.10 on PATH. A CRAM also needs the reference FASTA it was aligned to (--ref).

    python3 panel_bam_checks.py profile --bam sample.bam            # what the file is: build, read count, POLE depth
    python3 panel_bam_checks.py variant --bam sample.bam            # c.138del: supporting reads, fraction, strands
    python3 panel_bam_checks.py sites   --bam sample.bam            # recessive POLE alleles c.1686+32C>G, c.4444+3A>G
    python3 panel_bam_checks.py mosaic  --bam sample.bam --ref ref.fa --gene APC   # low-fraction variants in blood
    python3 panel_bam_checks.py power   --depth 600                 # chance of seeing a mosaic variant at that depth

What it cannot do: call structural variants, see genes the panel did not capture, or detect a mosaic variant that
is absent from blood. A clean result here does not exclude APC mosaicism; sequencing the polyps does that.

Status: the pileup parser and statistics are covered by tests/test_panel_bam_checks.py on synthetic input.
The samtools calls have not been run on real data by the author (no samtools in the authoring sandbox).
Coordinates: POLE positions are derived in analysis/variant_verification and were confirmed against Ensembl on
2026-11-20; the whole POLE gene maps GRCh38 -> GRCh37 as one block with a constant offset of +576,586.
The APC gene spans are Ensembl's (ENSG00000134982) for each build, looked up on the same day.
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from collections import Counter

CHR12_LEN = {133275309: "GRCh38", 133851895: "GRCh37"}      # Ensembl info/assembly, 2026-11-20
GRCH37_OFFSET = 576586                                      # valid inside POLE only
GENE_SPAN = {"APC": {"GRCh38": ("5", 112707452, 112846239), "GRCh37": ("5", 112043195, 112181936)}}
# name: (GRCh38 position, plus-strand reference, plus-strand variant, note)
POLE_SITES = {
    "c.138del": (132681203, "G", "-1C", "anchor base before the deleted C at 132681204"),
    "c.1686+32C>G": (132672595, "G", "C", "IMAGe syndrome allele (Logan 2018); rs762985435"),
    "c.4444+3A>G": (132643404, "T", "C", "FILS syndrome allele (Pachlopnik Schmid 2012); rs398122515"),
}


def parse_bases(bases: str) -> dict:
    """Tokenise the read-base column of `samtools mpileup`.

    Returns {"base": Counter[(base, strand)], "indel": Counter[(event, strand)], "placeholder": n, "skip": n};
    an indel event keeps the pileup spelling, e.g. "-1C" or "+2AT".
    base is one of A C G T N or "ref" (for . and ,); strand is "f" or "r".
    """
    base, indel = Counter(), Counter()
    placeholder = skip = 0
    i, n = 0, len(bases)
    while i < n:
        ch = bases[i]
        if ch == "^":                       # read start, followed by one mapping-quality character
            i += 2
        elif ch == "$":                     # read end
            i += 1
        elif ch in "+-":
            j = i + 1
            while j < n and bases[j].isdigit():
                j += 1
            length = int(bases[i + 1:j])
            seq = bases[j:j + length]
            indel[(f"{ch}{length}{seq.upper()}", "r" if seq.islower() else "f")] += 1
            i = j + length
        elif ch in ".,":
            base[("ref", "f" if ch == "." else "r")] += 1
            i += 1
        elif ch in "*#":
            placeholder += 1
            i += 1
        elif ch in "<>":
            skip += 1
            i += 1
        elif ch.upper() in "ACGTN":
            base[(ch.upper(), "f" if ch.isupper() else "r")] += 1
            i += 1
        else:
            raise ValueError(f"unexpected character {ch!r} at offset {i} in pileup column")
    return {"base": base, "indel": indel, "placeholder": placeholder, "skip": skip}


def allele_table(ref: str, parsed: dict) -> dict:
    """Collapse a parsed column into per-allele forward/reverse counts. ref 'N' -> majority base is the reference."""
    fr = {}
    for (b, strand), c in parsed["base"].items():
        fr.setdefault(b, [0, 0])[0 if strand == "f" else 1] += c
    ref = ref.upper()
    if ref in "ACGT" and "ref" in fr:
        f, r = fr.pop("ref")
        cur = fr.setdefault(ref, [0, 0])
        cur[0] += f
        cur[1] += r
    elif "ref" not in fr and ref not in "ACGT" and fr:
        ref = max(fr, key=lambda k: sum(fr[k]))        # no FASTA given: majority allele stands in for the reference
    depth = sum(sum(v) for v in fr.values())
    ind = {}
    for (ev, strand), c in parsed["indel"].items():
        ind.setdefault(ev, [0, 0])[0 if strand == "f" else 1] += c
    return {"ref": ref, "depth": depth, "alleles": fr, "indels": ind}


def binom_tail(n: int, p: float, k: int) -> float:
    """P(X >= k) for X ~ Binomial(n, p)."""
    return 1.0 - sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k))


def binom_two_sided_half(n: int, k: int) -> float:
    """Two-sided exact p-value for k of n under p = 0.5 (heterozygous expectation)."""
    pk = math.comb(n, k)
    return min(1.0, sum(math.comb(n, i) for i in range(n + 1) if math.comb(n, i) <= pk) / 2 ** n)


def detect_build(header: str) -> tuple[str, str]:
    """Return (build, prefix) from `samtools view -H` text, using the length of chromosome 12."""
    for line in header.splitlines():
        if not line.startswith("@SQ"):
            continue
        f = dict(x.split(":", 1) for x in line.split("\t")[1:] if ":" in x)
        if f.get("SN") in ("12", "chr12"):
            build = CHR12_LEN.get(int(f.get("LN", 0)))
            if build is None:
                raise SystemExit(f"chromosome 12 has length {f.get('LN')}: neither GRCh37 nor GRCh38")
            return build, ("chr" if f["SN"].startswith("chr") else "")
    raise SystemExit("no chromosome 12 in the header")


def candidates(table: dict, min_alt: int, min_frac: float, max_frac: float) -> list[dict]:
    """Non-reference alleles whose fraction lies in [min_frac, max_frac] with support on both strands."""
    out, depth = [], table["depth"]
    if depth == 0:
        return out
    pool = {k: v for k, v in table["alleles"].items() if k != table["ref"]}
    pool.update(table["indels"])
    for allele, (f, r) in pool.items():
        n = f + r
        if n >= min_alt and f >= 1 and r >= 1 and min_frac <= n / depth <= max_frac:
            out.append({"allele": allele, "count": n, "fwd": f, "rev": r, "fraction": n / depth})
    return out


# ---------------------------------------------------------------------------------------------- samtools wrappers
def run(cmd: list[str]) -> str:
    if shutil.which(cmd[0]) is None:
        raise SystemExit(f"{cmd[0]} not found on PATH")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise SystemExit(f"{' '.join(cmd)} failed:\n{res.stderr.strip()}")
    return res.stdout


def pileup(bam: str, region: str, ref: str | None, min_bq: int = 20, min_mq: int = 20):
    cmd = ["samtools", "mpileup", "-a", "-B", "-d", "0", "-Q", str(min_bq), "-q", str(min_mq), "-r", region]
    if ref:
        cmd += ["-f", ref]
    for line in run(cmd + [bam]).splitlines():
        chrom, pos, refb, _depth, bases = line.split("\t")[:5]
        yield chrom, int(pos), allele_table(refb, parse_bases(bases))


def build_of(bam: str) -> tuple[str, str]:
    return detect_build(run(["samtools", "view", "-H", bam]))


def site_region(name: str, build: str, prefix: str) -> tuple[str, int]:
    pos = POLE_SITES[name][0] + (GRCH37_OFFSET if build == "GRCh37" else 0)
    return f"{prefix}12:{pos}-{pos}", pos


def cmd_profile(a) -> None:
    build, prefix = build_of(a.bam)
    print(f"reference build: {build} (contigs named '{prefix}12')")
    try:
        rows = [l.split("\t") for l in run(["samtools", "idxstats", a.bam]).splitlines()]
        mapped = sum(int(r[2]) for r in rows)
        print(f"mapped reads: {mapped:,}")
        print("  for scale: a 30x genome with 150-bp reads has roughly 600 million; a gene panel has a few million")
    except SystemExit as exc:
        print(f"idxstats unavailable ({exc}); index the file with `samtools index` first")
    for name in POLE_SITES:
        region, pos = site_region(name, build, prefix)
        for _c, _p, t in pileup(a.bam, region, a.ref):
            print(f"depth at POLE {name} ({region}): {t['depth']}")


def cmd_variant(a) -> None:
    build, prefix = build_of(a.bam)
    region, pos = site_region("c.138del", build, prefix)
    for _c, _p, t in pileup(a.bam, region, a.ref):
        dels = {k: v for k, v in t["indels"].items() if k.startswith("-1")}
        f, r = (sum(v[0] for v in dels.values()), sum(v[1] for v in dels.values()))
        n, depth = f + r, t["depth"]
        print(f"POLE c.138del  {build} {region} (anchor base; deleted base is {pos + 1})")
        print(f"reads covering the anchor: {depth}")
        print(f"reads carrying the 1-bp deletion: {n} (forward {f}, reverse {r})")
        if depth:
            print(f"deletion fraction: {n / depth:.3f}")
            print(f"exact two-sided p for a 50% heterozygous allele: {binom_two_sided_half(depth, n):.3g}")
            print("reading: about 0.4-0.5 fits an inherited heterozygous variant (indels often read slightly below 0.5);")
            print("         a fraction well below that, with a small p-value, raises mosaicism and needs a second tissue.")
        other = {k: v for k, v in t["indels"].items() if not k.startswith("-1")}
        if other:
            print(f"other indel events at this base: {other}")


def cmd_sites(a) -> None:
    build, prefix = build_of(a.bam)
    for name in ("c.1686+32C>G", "c.4444+3A>G"):
        region, _pos = site_region(name, build, prefix)
        _g38, refb, alt, note = POLE_SITES[name]
        for _c, _p, t in pileup(a.bam, region, a.ref):
            f, r = t["alleles"].get(alt, [0, 0])
            status = "NOT COVERED" if t["depth"] < 20 else ("VARIANT READS PRESENT" if f + r >= 3 else "no variant reads")
            print(f"POLE {name}  {region}  plus-strand {refb}>{alt}  depth {t['depth']}  variant reads {f + r} "
                  f"(fwd {f}, rev {r})  -> {status}   [{note}]")
    print("A panel may not capture these intronic bases. 'NOT COVERED' means untested, not negative.")


def gene_region(gene: str, build: str, prefix: str) -> str:
    chrom, start, end = GENE_SPAN[gene][build]
    return f"{prefix}{chrom}:{start}-{end}"


def cmd_mosaic(a) -> None:
    regions = list(a.region or [])
    if a.gene:
        build, prefix = build_of(a.bam)
        regions.append(gene_region(a.gene, build, prefix))
    if not regions:
        raise SystemExit("give --gene APC or at least one --region")
    if not a.ref:
        raise SystemExit("mosaic needs --ref: without the reference FASTA mpileup reports N as the reference base, "
                         "the majority allele would be taken as reference, and deletions would print as -1N")
    print("chrom\tpos\tref\tdepth\tallele\tcount\tfwd\trev\tfraction")
    n_pos = n_hit = 0
    for region in regions:
        for chrom, pos, t in pileup(a.bam, region, a.ref, a.min_bq, a.min_mq):
            if t["depth"] < a.min_depth:
                continue
            n_pos += 1
            for c in candidates(t, a.min_alt, a.min_frac, a.max_frac):
                n_hit += 1
                print(f"{chrom}\t{pos}\t{t['ref']}\t{t['depth']}\t{c['allele']}\t{c['count']}\t{c['fwd']}\t{c['rev']}\t{c['fraction']:.4f}")
    print(f"# {n_pos} positions with depth >= {a.min_depth} scanned, {n_hit} candidate(s).", file=sys.stderr)
    print("# Every candidate is a lead, not a call: check it in a genome browser, annotate it, and look for it in polyp DNA.",
          file=sys.stderr)


def cmd_power(a) -> None:
    print(f"depth {a.depth}, variant reported when >= {a.min_alt} supporting reads")
    for vaf in (0.005, 0.01, 0.02, 0.05, 0.10, 0.20):
        print(f"  mosaic fraction {vaf:>5.1%}: detection probability {binom_tail(a.depth, vaf, a.min_alt):.2f}")
    print("This counts sampling only. Sequencing error adds false leads at the lowest fractions.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("profile", cmd_profile), ("variant", cmd_variant), ("sites", cmd_sites), ("mosaic", cmd_mosaic)):
        p = sub.add_parser(name)
        p.add_argument("--bam", required=True, help="BAM or CRAM, indexed")
        p.add_argument("--ref", help="reference FASTA (required for CRAM and for `mosaic`)")
        p.set_defaults(fn=fn)
        if name == "mosaic":
            p.add_argument("--region", action="append", help="chr:start-end; repeat for several")
            p.add_argument("--gene", choices=sorted(GENE_SPAN), help="scan a whole gene span for the detected build")
            p.add_argument("--min-alt", type=int, default=5)
            p.add_argument("--min-frac", type=float, default=0.01)
            p.add_argument("--max-frac", type=float, default=0.35)
            p.add_argument("--min-depth", type=int, default=100)
            p.add_argument("--min-bq", type=int, default=20)
            p.add_argument("--min-mq", type=int, default=20)
    p = sub.add_parser("power")
    p.add_argument("--depth", type=int, required=True)
    p.add_argument("--min-alt", type=int, default=5)
    p.set_defaults(fn=cmd_power)
    a = ap.parse_args(argv)
    a.fn(a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
