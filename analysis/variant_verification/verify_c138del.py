#!/usr/bin/env python3
"""Deterministic re-derivation of POLE c.138del (p.Leu46Phefs*8) on the MANE Select transcript.

Standard library only. No network access. Every number printed here is computed
from the reference fixtures in data/reference/ -- nothing is typed in by hand.

Usage:
    python3 analysis/variant_verification/verify_c138del.py            # human-readable report
    python3 analysis/variant_verification/verify_c138del.py --json     # machine-readable
    python3 analysis/variant_verification/verify_c138del.py --check-legacy data/POLE_coding_sequence.fa

Fixtures (see data/reference/README.md for provenance):
    POLE_MANE_cds_1-480.fa       first 480 nt of ENST00000320574.10 CDS (= NM_006231.4)
    POLE_Q07864_aa_1-240.fa      first 240 aa of UniProt Q07864
    POLE_MANE_exons_GRCh38.tsv   49 exons of ENST00000320574.10 on GRCh38
    POLE_MANE_5utr_last6.fa      c.-6..c.-1, needed for the Kozak context of the annotated start codon
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, "..", "..", "data", "reference"))

CODON = {
    a + b + c: aa
    for (a, b, c), aa in zip(
        ((a, b, c) for a in "TCAG" for b in "TCAG" for c in "TCAG"),
        "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
    )
}
AA3 = {
    "A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys", "Q": "Gln", "E": "Glu",
    "G": "Gly", "H": "His", "I": "Ile", "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe",
    "P": "Pro", "S": "Ser", "T": "Thr", "W": "Trp", "Y": "Tyr", "V": "Val", "*": "Ter",
}
COMPLEMENT = str.maketrans("ACGT", "TGCA")

# Values retrieved from Ensembl REST / ClinVar on 2026-11-20 (see data/claims_ledger.tsv).
CDS_START_GRCH38 = 132687315          # genomic position of c.1 (minus strand)
FIVE_PRIME_UTR_LEN = 27               # 132687316..132687342
GRCH37_MINUS_GRCH38_EXON2 = 576586    # 133257790 - 132681204, verified for exon 2 only


def read_fasta(path: str) -> tuple[str, str]:
    header, seq = "", []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                header = line[1:]
            else:
                seq.append(line.upper())
    return header, "".join(seq)


def translate(nt: str) -> str:
    return "".join(CODON.get(nt[i:i + 3], "X") for i in range(0, len(nt) - len(nt) % 3, 3))


def read_exons(path: str) -> list[tuple[int, int, int]]:
    exons = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("exon") or not line.strip():
                continue
            n, s, e = line.split()[:3]
            exons.append((int(n), int(s), int(e)))
    return exons


def cds_segments(exons):
    """Yield (exon_number, cds_start, cds_end, genomic_start_of_cds_start) for a minus-strand gene."""
    out, c = [], 1
    for n, s, e in exons:            # exons are listed 5'->3' (descending genomic coordinate)
        hi = min(e, CDS_START_GRCH38)   # clip 5'UTR in exon 1
        if hi < s:
            continue
        length = hi - s + 1
        out.append((n, c, c + length - 1, hi))
        c += length
    return out


def cds_to_grch38(pos: int, segs) -> tuple[int, int]:
    for n, c0, c1, ghi in segs:
        if c0 <= pos <= c1:
            return n, ghi - (pos - c0)
    raise ValueError(f"c.{pos} outside mapped CDS (3'UTR/last-exon clipping is not modelled)")


def grch38_to_cds(g: int, segs) -> tuple[int, int] | None:
    for n, c0, c1, ghi in segs:
        glo = ghi - (c1 - c0)
        if glo <= g <= ghi:
            return n, c0 + (ghi - g)
    return None


def kozak(seq: str, a_idx: int) -> tuple[str, str]:
    """Return (context -3..+4, strength) for an ATG whose A is at 0-based index a_idx.

    Strength uses the rule already stated in models/mechanistic_models.md:
    strong = purine at -3 AND G at +4; moderate = exactly one; weak = neither.
    """
    if a_idx < 3 or a_idx + 4 > len(seq):
        return "n/a", "n/a"
    ctx = seq[a_idx - 3:a_idx + 4]
    purine, g4 = ctx[0] in "AG", ctx[6] == "G"
    return ctx, ("strong" if purine and g4 else "moderate" if purine or g4 else "weak")


def hgvs_frameshift(wt_cds: str, wt_protein_hint: str, del_pos: int) -> dict:
    """Delete one base at 1-based CDS position del_pos and derive the protein consequence."""
    base = wt_cds[del_pos - 1]
    # HGVS 3' rule: a deletion inside a homopolymer is assigned to its most 3' position.
    three_prime = del_pos
    while three_prime < len(wt_cds) and wt_cds[three_prime] == base:
        three_prime += 1
    mut = wt_cds[:del_pos - 1] + wt_cds[del_pos:]
    wt_aa, mut_aa = translate(wt_cds), translate(mut)
    first = next(i for i, (a, b) in enumerate(zip(wt_aa, mut_aa)) if a != b)   # 0-based
    stop = mut_aa.find("*", first)
    if stop < 0:
        raise ValueError("no stop codon inside the supplied CDS window; extend the fixture")
    codon = (first + 1)
    return {
        "deleted_base": base,
        "hgvs_c_position_after_3prime_rule": three_prime,
        "codon_number": codon,
        "wt_codon": wt_cds[first * 3:first * 3 + 3],
        "mut_codon": mut[first * 3:first * 3 + 3],
        "wt_aa": wt_aa[first],
        "mut_aa": mut_aa[first],
        "fs_length": stop - first + 1,            # the N in fs*N (first changed residue = 1)
        "stop_codon_number": stop + 1,
        "stop_codon": mut[stop * 3:stop * 3 + 3],
        "stop_cds_wt_numbering": (stop * 3 + 1 + 1, stop * 3 + 3 + 1),   # +1: positions after the deletion
        "truncated_length_aa": stop,
        "native_residues": first,
        "novel_residues": mut_aa[first:stop],
        "truncated_protein": mut_aa[:stop],
        "hgvs_p": f"p.{AA3[wt_aa[first]]}{codon}{AA3[mut_aa[first]]}fs*{stop - first + 1}",
        "mutant_cds": mut,
    }


def all_atgs(seq: str) -> list[dict]:
    out, i = [], seq.find("ATG")
    while i >= 0:
        ctx, strength = kozak(seq, i)
        out.append({"cds_pos": i + 1, "frame": i % 3, "kozak": ctx, "strength": strength})
        i = seq.find("ATG", i + 1)
    return out


def orf_end(seq: str, start_idx: int) -> int | None:
    """0-based index of the first base of the first in-frame stop codon downstream of start_idx."""
    for i in range(start_idx, len(seq) - 2, 3):
        if CODON[seq[i:i + 3]] == "*":
            return i
    return None


def orf_map(utr: str, cds: str, deleted_c: int | None = None, upto_c: int = 280) -> list[dict]:
    """Every AUG a scanning ribosome can meet in the first `upto_c` nt, with the ORF it opens.

    `utr` is the 5' context (transcript orientation) placed in front of `cds`. If `deleted_c` is given the
    base at that wild-type c. position is removed first; positions are still reported in wild-type numbering.
    """
    seq = utr + (cds if deleted_c is None else cds[:deleted_c - 1] + cds[deleted_c:])
    off = len(utr)

    def wt_c(idx: int) -> int:                       # 0-based index in seq -> wild-type c. position
        c = idx - off + 1
        return c + 1 if (deleted_c is not None and c >= deleted_c) else c

    out, i = [], seq.find("ATG")
    while i >= 0 and i - off + 1 <= upto_c:
        ctx, strength = kozak(seq, i)
        pep, j = [], i
        while j + 3 <= len(seq) and CODON[seq[j:j + 3]] != "*":
            pep.append(CODON[seq[j:j + 3]])
            j += 3
        closed = j + 3 <= len(seq)
        out.append({"atg_c": wt_c(i), "kozak": ctx, "strength": strength, "codons": len(pep),
                    "stop_c": [wt_c(j), wt_c(j + 2)] if closed else None,
                    "peptide": "".join(pep) if closed else "".join(pep[:12]) + "..."})
        i = seq.find("ATG", i + 1)
    return out


def build_report(legacy_fasta: str | None = None) -> dict:
    cds_header, cds = read_fasta(os.path.join(REF, "POLE_MANE_cds_1-480.fa"))
    aa_header, aa = read_fasta(os.path.join(REF, "POLE_Q07864_aa_1-240.fa"))
    exons = read_exons(os.path.join(REF, "POLE_MANE_exons_GRCh38.tsv"))
    segs = cds_segments(exons)

    rep: dict = {"fixtures": {"cds": cds_header, "protein": aa_header, "n_exons": len(exons)}}

    # 1. Cross-validation of two independently retrieved sources.
    tr = translate(cds)
    rep["cross_validation"] = {
        "cds_nt": len(cds),
        "translated_aa": len(tr),
        "identical_to_uniprot_prefix": tr == aa[:len(tr)],
        "mismatches": [(i + 1, a, b) for i, (a, b) in enumerate(zip(tr, aa)) if a != b],
    }

    # 2. Local codon table around the variant.
    rep["codons_44_54_wt"] = [
        {"codon": k, "c": f"{3 * k - 2}-{3 * k}", "nt": cds[3 * k - 3:3 * k], "aa": tr[k - 1]}
        for k in range(44, 55)
    ]

    # 3. The variant.
    fs = hgvs_frameshift(cds, aa, 138)
    mut = fs.pop("mutant_cds")
    rep["c138del"] = fs
    rep["codons_44_53_mut"] = [
        {"codon": k, "nt": mut[3 * k - 3:3 * k], "aa": CODON[mut[3 * k - 3:3 * k]]} for k in range(44, 54)
    ]

    # 4. Genomic coordinates.
    exon, g38 = cds_to_grch38(138, segs)
    seg = next(s for s in segs if s[0] == exon)
    plus_ref = cds[136:139][::-1].translate(COMPLEMENT)          # c.139,c.138,c.137 complemented = g-1,g,g+1
    rep["genomic"] = {
        "exon": f"{exon}/{len(exons)}",
        "exon_cds_range": f"c.{seg[1]}-c.{seg[2]}",
        "dist_to_exon_5prime_end_nt": 138 - seg[1],
        "dist_to_exon_3prime_end_nt": seg[2] - 138,
        "GRCh38": {"chrom": "12", "pos_deleted_base": g38, "hgvs_g": f"NC_000012.12:g.{g38}del",
                   "plus_strand_context_g-1_g_g+1": plus_ref,
                   "vcf": f"12-{g38 - 1}-{plus_ref[0]}{plus_ref[1]}-{plus_ref[0]}"},
        "GRCh37": {"chrom": "12", "pos_deleted_base": g38 + GRCH37_MINUS_GRCH38_EXON2,
                   "hgvs_g": f"NC_000012.11:g.{g38 + GRCH37_MINUS_GRCH38_EXON2}del",
                   "vcf": f"12-{g38 + GRCH37_MINUS_GRCH38_EXON2 - 1}-{plus_ref[0]}{plus_ref[1]}-{plus_ref[0]}"},
        "cdna_position": 138 + FIVE_PRIME_UTR_LEN,
    }
    # Reverse-map the coordinate previously published in this repository.
    legacy_g37 = 133249847
    back = grch38_to_cds(legacy_g37 - GRCH37_MINUS_GRCH38_EXON2, segs)
    rep["legacy_grch37_coordinate_check"] = {
        "coordinate": f"chr12:{legacy_g37}",
        "maps_to": None if back is None else {"exon": back[0], "cds_pos": back[1], "codon": (back[1] + 2) // 3},
        "note": "offset verified for exon 2 only; Ensembl GRCh37 REST independently maps c.1376 to chr12:133249847",
    }

    # 5. Start codons available to a ribosome on the wild-type and mutant mRNA.
    atgs = all_atgs(cds)
    rep["atg_codons_wt_cds_1_480"] = atgs
    stop_first_base_wt = fs["stop_cds_wt_numbering"][0]
    downstream = [a for a in atgs if a["cds_pos"] > stop_first_base_wt]
    rep["first_atg_after_ptc"] = downstream[0] if downstream else None
    if downstream:
        d = downstream[0]
        rep["first_atg_after_ptc"].update({
            "in_canonical_frame": d["frame"] == 0,
            "codon_number": (d["cds_pos"] + 2) // 3 if d["frame"] == 0 else None,
            "nt_between_stop_and_atg": d["cds_pos"] - (fs["stop_cds_wt_numbering"][1] + 1),
            "residues_missing_if_used": (d["cds_pos"] - 1) // 3 if d["frame"] == 0 else None,
        })
    # The +1 frame entered by the deletion is also open in the wild-type mRNA from out-of-frame AUGs.
    plus1 = []
    for a in atgs:
        if a["frame"] == 1 and a["cds_pos"] < 138:
            end = orf_end(cds, a["cds_pos"] - 1)
            plus1.append({**a, "orf_stop_cds": None if end is None else (end + 1, end + 3),
                          "orf_codons": None if end is None else (end - (a["cds_pos"] - 1)) // 3})
    rep["out_of_frame_atgs_upstream_sharing_the_frameshift_stop"] = plus1
    rep["in_frame_methionines_1_240"] = [i + 1 for i, r in enumerate(aa) if r == "M"]

    # 6. Translation map of the wild-type and mutant mRNA, with the true context of the annotated start codon.
    utr_header, utr = read_fasta(os.path.join(REF, "POLE_MANE_5utr_last6.fa"))
    rep["fixtures"]["utr"] = utr_header
    rep["start_codon_context"] = dict(zip(("kozak", "strength"), kozak(utr + cds, len(utr))))
    rep["orf_map_wild_type"] = orf_map(utr, cds)
    rep["orf_map_c138del"] = orf_map(utr, cds, deleted_c=138)
    ex2 = next(s_ for s_ in segs if s_[0] == 2)
    rep["exon2"] = {"cds_nt": ex2[2] - ex2[1] + 1, "skipping_keeps_frame": (ex2[2] - ex2[1] + 1) % 3 == 0}
    upstream = [o for o in rep["orf_map_c138del"] if o["atg_c"] < 138]
    rep["c138del_translation_summary"] = {
        "every_upstream_aug_terminates_by_c": max(o["stop_c"][1] for o in upstream),
        "upstream_orf_lengths_codons": {f"c.{o['atg_c']}": o["codons"] for o in upstream},
        "first_aug_after_all_stops": rep["first_atg_after_ptc"]["cds_pos"] if rep["first_atg_after_ptc"] else None,
    }

    # 7. Optional: audit the legacy FASTA shipped in data/.
    if legacy_fasta:
        lh, ls = read_fasta(legacy_fasta)
        n = min(len(ls), len(cds))
        ident = sum(1 for x, y in zip(ls[:n], cds[:n]) if x == y)
        lt = translate(ls)
        rep["legacy_fasta_audit"] = {
            "header": lh, "length_nt": len(ls), "expected_full_cds_nt": 6861,
            "nt_identity_first_%d" % n: round(ident / n, 3),
            "aa_identity_first_160": round(sum(1 for x, y in zip(lt[:160], aa[:160]) if x == y) / 160, 3),
            "legacy_codon_45": ls[132:135], "legacy_codon_46": ls[135:138], "legacy_aa_46": CODON.get(ls[135:138]),
            "is_pole": ident / n > 0.95,
        }
    return rep


def print_report(r: dict) -> None:
    p = print
    cv, v, g = r["cross_validation"], r["c138del"], r["genomic"]
    p("POLE c.138del -- deterministic re-derivation on MANE Select (ENST00000320574.10 / NM_006231.4)")
    p("=" * 96)
    p(f"[1] Source cross-check: {cv['cds_nt']} nt of Ensembl CDS translate to {cv['translated_aa']} aa; "
      f"identical to UniProt Q07864 prefix: {cv['identical_to_uniprot_prefix']}")
    p("\n[2] Wild-type codons 44-54")
    p("    " + "  ".join(f"{c['codon']}:{c['nt']}({c['aa']})" for c in r["codons_44_54_wt"]))
    p(f"\n[3] c.138 is the third base of codon {v['codon_number']} ({v['wt_codon']} = {AA3[v['wt_aa']]}); "
      f"deleted base = {v['deleted_base']}; 3'-rule position = c.{v['hgvs_c_position_after_3prime_rule']}")
    p("    Mutant codons 44-53")
    p("    " + "  ".join(f"{c['codon']}:{c['nt']}({c['aa']})" for c in r["codons_44_53_mut"]))
    p(f"    => {v['hgvs_p']}   (stop codon {v['stop_codon']} = new codon {v['stop_codon_number']}; "
      f"wild-type numbering c.{v['stop_cds_wt_numbering'][0]}_{v['stop_cds_wt_numbering'][1]})")
    p(f"    Predicted product if translated and stable: {v['truncated_length_aa']} aa "
      f"({v['native_residues']} native + {len(v['novel_residues'])} novel: {v['novel_residues']})")
    p(f"\n[4] Genomic: exon {g['exon']} ({g['exon_cds_range']}); {g['dist_to_exon_5prime_end_nt']} nt from the "
      f"exon's 5' end, {g['dist_to_exon_3prime_end_nt']} nt from its 3' end; cDNA position {g['cdna_position']}")
    for asm in ("GRCh38", "GRCh37"):
        p(f"    {asm}: chr12:{g[asm]['pos_deleted_base']}  {g[asm]['hgvs_g']}  VCF {g[asm]['vcf']}")
    lc = r["legacy_grch37_coordinate_check"]
    p(f"    Previously published GRCh37 coordinate {lc['coordinate']} maps to {lc['maps_to']}")
    p("\n[5] ATG codons in CDS 1-480 (cds_pos, frame 0 = canonical, Kozak -3..+4, strength)")
    for a in r["atg_codons_wt_cds_1_480"]:
        p(f"    c.{a['cds_pos']:<4d} frame {a['frame']}  {a['kozak']:8s} {a['strength']}")
    f = r["first_atg_after_ptc"]
    p(f"    First ATG 3' of the premature stop: c.{f['cds_pos']} (Met{f['codon_number']}), in canonical frame: "
      f"{f['in_canonical_frame']}, {f['nt_between_stop_and_atg']} nt after the stop, Kozak {f['kozak']} ({f['strength']}); "
      f"a product starting there would lack residues 1-{f['residues_missing_if_used']}")
    p("    Wild-type mRNA: out-of-frame ATGs 5' of c.138 whose ORFs end at the stop codon the frameshift runs into:")
    for a in r["out_of_frame_atgs_upstream_sharing_the_frameshift_stop"]:
        p(f"      c.{a['cds_pos']} ({a['kozak']}, {a['strength']}): {a['orf_codons']}-codon ORF ending at c.{a['orf_stop_cds'][0]}_{a['orf_stop_cds'][1]}")
    p(f"    In-frame Met residues within aa 1-240: {r['in_frame_methionines_1_240']}")
    sc = r["start_codon_context"]
    p(f"\n[6] Translation map (5' context from Ensembl). Annotated start codon: {sc['kozak']} = {sc['strength']} Kozak context")
    for label, key in (("wild-type mRNA", "orf_map_wild_type"), ("c.138del mRNA", "orf_map_c138del")):
        p(f"    {label}")
        for o in r[key]:
            stop = "open beyond the 480-nt fixture" if o["stop_c"] is None else f"stop c.{o['stop_c'][0]}_{o['stop_c'][1]}"
            p(f"      AUG c.{o['atg_c']:<4d} {o['kozak']} {o['strength']:8s} {o['codons']:3d} codons, {stop:32s} {o['peptide']}")
    ts = r["c138del_translation_summary"]
    p(f"    On the mutant mRNA every AUG 5' of the deletion opens an ORF that ends by c.{ts['every_upstream_aug_terminates_by_c']} "
      f"({', '.join(f'{k}: {n} codons' for k, n in ts['upstream_orf_lengths_codons'].items())}); "
      f"the next AUG is c.{ts['first_aug_after_all_stops']}.")
    p(f"    Exon 2 holds {r['exon2']['cds_nt']} nt of CDS; skipping it would "
      f"{'keep' if r['exon2']['skipping_keeps_frame'] else 'also shift'} the reading frame.")
    if "legacy_fasta_audit" in r:
        la = r["legacy_fasta_audit"]
        p("\n[7] Legacy FASTA audit")
        for k, val in la.items():
            p(f"    {k}: {val}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check-legacy", metavar="FASTA")
    a = ap.parse_args()
    rep = build_report(a.check_legacy)
    if a.json:
        json.dump(rep, sys.stdout, indent=1)
        print()
    else:
        print_report(rep)
    ok = rep["cross_validation"]["identical_to_uniprot_prefix"] and rep["c138del"]["hgvs_p"] == "p.Leu46Phefs*8"
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
