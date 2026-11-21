#!/usr/bin/env python3
"""Place POLE c.138del among the other start-loss and truncating variants recorded in exons 1-2.

Standard library only, no network. For every record in
data/reference/POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv the script
  1. checks the reference allele against the MANE CDS fixture (catches transcription errors),
  2. converts the plus-strand change to transcript orientation and applies the HGVS 3' rule,
  3. derives the protein consequence on ENST00000320574.10, and
  4. reports the translation context that decides whether a ribosome can restart downstream
     (position of the stop, next in-frame AUG, gap between them).

Scope: single-exon changes inside c.1-c.204. Records that reach into an intron or the 5'UTR are listed
but not modelled. Reinitiation "eligibility" is a sequence-based statement only (see docs/EVIDENCE_PROTOCOL.md):
no experiment in this repository shows that any of these alleles makes protein.

Usage:
    python3 analysis/variant_verification/nterm_truncations.py [--tsv]
"""
from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import verify_c138del as v  # noqa: E402  (same directory; shares fixtures and codon table)

FIX = os.path.join(v.REF, "POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv")
EXON1_CDS = (132687254, 132687315)   # c.62 .. c.1   (minus strand: higher coordinate = more 5')
EXON2 = (132681138, 132681279)       # c.204 .. c.63
IN_FRAME_MET = {44: 130, 66: 196, 221: 661}   # codon -> c. position of the A; from the Q07864 fixture (aa 1-240)
COHEN_MAX_PTC_CODON = 126            # Cohen et al. 2019, doi:10.1093/nar/gkz319 (p53 reporters)
COHEN_GAP_NT = (6, 243)


def revcomp(s: str) -> str:
    return s.translate(v.COMPLEMENT)[::-1]


def g_to_c(g: int) -> int | None:
    if EXON1_CDS[0] <= g <= EXON1_CDS[1]:
        return EXON1_CDS[1] - g + 1
    if EXON2[0] <= g <= EXON2[1]:
        return 63 + (EXON2[1] - g)
    return None


def plus_ref(cds: str, start: int, end: int) -> str | None:
    """Plus-strand reference for a genomic interval that lies wholly inside the modelled CDS."""
    cs = [g_to_c(g) for g in range(start, end + 1)]
    if any(c is None for c in cs):
        return None
    return "".join(cds[c - 1] for c in cs).translate(v.COMPLEMENT)


def to_transcript_edit(cds: str, start: int, end: int, ref: str, alt: str):
    """Return (i, deleted, inserted): replace cds[i:i+len(deleted)] by inserted (0-based, transcript strand)."""
    ref, alt = ref.replace("-", ""), alt.replace("-", "")
    if not ref:                                   # Ensembl insertion style: start = end + 1, empty reference
        # the new bases go between plus positions `end` and `start`; on the transcript strand that is
        # between c(start) and c(end), so they are inserted before 0-based index c(end)-1
        c_hi, c_lo = g_to_c(end), g_to_c(start)
        if c_hi is None or c_lo is None:
            return None
        return c_hi - 1, "", revcomp(alt)
    got = plus_ref(cds, start, start + len(ref) - 1)
    if got is None:
        return None
    if got != ref:
        raise ValueError(f"reference mismatch at {start}: fixture says {ref}, CDS says {got}")
    c_first = g_to_c(start + len(ref) - 1)        # transcript-5' end of the interval
    return c_first - 1, revcomp(ref), revcomp(alt)


def normalise(cds: str, i: int, dele: str, ins: str):
    """Trim shared flanks, then shift a pure deletion or insertion to its most 3' position (HGVS 3' rule)."""
    while dele and ins and dele[0] == ins[0]:
        dele, ins, i = dele[1:], ins[1:], i + 1
    while dele and ins and dele[-1] == ins[-1]:
        dele, ins = dele[:-1], ins[:-1]
    if dele and not ins:
        L = len(dele)
        while i + L < len(cds) and cds[i] == cds[i + L]:
            i += 1
        dele = cds[i:i + L]
    elif ins and not dele:
        while i < len(cds) and ins[0] == cds[i]:
            ins, i = ins[1:] + cds[i], i + 1
    return i, dele, ins


def hgvs_c(cds: str, i: int, dele: str, ins: str) -> str:
    if dele and ins:
        if len(dele) == 1 and len(ins) == 1:
            return f"c.{i + 1}{dele}>{ins}"
        return f"c.{i + 1}_{i + len(dele)}delins{ins}"
    if dele:
        return f"c.{i + 1}del" if len(dele) == 1 else f"c.{i + 1}_{i + len(dele)}del"
    L = len(ins)
    if cds[i - L:i] == ins:
        return f"c.{i}dup" if L == 1 else f"c.{i - L + 1}_{i}dup"
    return f"c.{i}_{i + 1}ins{ins}"


def consequence(cds: str, i: int, dele: str, ins: str) -> dict:
    mut = cds[:i] + ins + cds[i + len(dele):]
    wt_aa, mut_aa = v.translate(cds), v.translate(mut)
    shift = len(ins) - len(dele)
    out = {"mut": mut, "shift": shift}
    if mut[:3] != "ATG":
        out.update(kind="start_lost", hgvs_p="p.Met1?", ptc_codon=None, stop_c=None)
        return out
    k = next((n for n, (a, b) in enumerate(zip(wt_aa, mut_aa)) if a != b), None)
    if k is None:
        out.update(kind="synonymous", hgvs_p="p.=", ptc_codon=None, stop_c=None)
        return out
    stop = mut_aa.find("*", k)
    if mut_aa[k] == "*":
        kind, p = "nonsense", f"p.{v.AA3[wt_aa[k]]}{k + 1}Ter"
    elif shift % 3:
        if stop < 0:
            kind, p = "frameshift", f"p.{v.AA3[wt_aa[k]]}{k + 1}{v.AA3[mut_aa[k]]}fs*?"
        else:
            kind, p = "frameshift", f"p.{v.AA3[wt_aa[k]]}{k + 1}{v.AA3[mut_aa[k]]}fs*{stop - k + 1}"
    else:
        kind, p = "missense_or_inframe", f"p.{v.AA3[wt_aa[k]]}{k + 1}{v.AA3[mut_aa[k]]}"
    out.update(kind=kind, hgvs_p=p, ptc_codon=None if stop < 0 else stop + 1,
               novel=mut_aa[k:stop] if (kind == "frameshift" and stop >= 0) else "")
    if stop >= 0 and kind in ("nonsense", "frameshift"):
        stop_mut_idx = stop * 3                              # 0-based index of the stop's first base in the mutant
        # express in wild-type numbering: undo the length change if the stop lies 3' of the edit
        out["stop_c"] = stop_mut_idx + 1 - (shift if stop_mut_idx >= i + len(ins) else 0)
    else:
        out["stop_c"] = None
    return out


def restart(stop_c: int | None, ptc_codon: int | None) -> dict:
    """Next in-frame AUG 3' of the stop, in wild-type numbering, and the two Cohen 2019 conditions."""
    if stop_c is None:
        return {}
    last = stop_c + 2
    nxt = next(((cod, c) for cod, c in sorted(IN_FRAME_MET.items()) if c > last), None)
    if nxt is None:
        return {"next_met": None}
    gap = nxt[1] - last - 1
    return {"next_met": nxt[0], "gap_nt": gap, "lost_residues": nxt[0] - 1,
            "within_cohen_window": ptc_codon <= COHEN_MAX_PTC_CODON and COHEN_GAP_NT[0] <= gap <= COHEN_GAP_NT[1]}


def rows() -> list[dict]:
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_1-480.fa"))
    out = []
    with open(FIX, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("rsid") or not line.strip():
                continue
            rsid, start, end, ref, alts, cons, clin = (line.rstrip("\n").split("\t") + [""] * 7)[:7]
            start, end = int(start), int(end)
            for alt in alts.split(","):
                base = {"rsid": rsid, "g38": f"12:{start}" if start >= end else f"12:{start}-{end}",
                        "plus_change": f"{ref}>{alt}", "ensembl_consequence": cons, "clin_sig_rsid_level": clin}
                try:
                    edit = to_transcript_edit(cds, start, end, ref, alt)
                except ValueError as exc:
                    out.append({**base, "kind": "REFERENCE_MISMATCH", "note": str(exc)})
                    continue
                if edit is None:
                    out.append({**base, "kind": "not_modelled", "note": "reaches into an intron or the 5'UTR"})
                    continue
                i, dele, ins = normalise(cds, *edit)
                c = consequence(cds, i, dele, ins)
                if c["kind"] in ("synonymous", "missense_or_inframe"):
                    continue                      # other alleles of a multi-allelic site
                r = restart(c["stop_c"], c["ptc_codon"])
                out.append({**base, "hgvs_c": hgvs_c(cds, i, dele, ins), "hgvs_p": c["hgvs_p"], "kind": c["kind"],
                            "ptc_codon": c["ptc_codon"], "stop_c": c["stop_c"], "novel_tail": c.get("novel", ""), **r})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tsv", action="store_true", help="tab-separated output")
    a = ap.parse_args()
    rs = rows()
    cols = ["rsid", "g38", "plus_change", "hgvs_c", "hgvs_p", "kind", "ptc_codon", "stop_c", "novel_tail",
            "next_met", "gap_nt", "lost_residues", "within_cohen_window", "clin_sig_rsid_level", "note"]
    if a.tsv:
        print("\t".join(cols))
        for r in rs:
            print("\t".join("" if r.get(c) is None else str(r.get(c, "")) for c in cols))
        return 0
    print("POLE exons 1-2: start-loss and truncating variants in dbSNP/ClinVar (via Ensembl, 2026-11-20), re-derived on MANE Select")
    print("=" * 118)
    for r in rs:
        if r["kind"] in ("not_modelled", "REFERENCE_MISMATCH"):
            print(f"{r['rsid']:13s} {r['g38']:24s} {r['kind']}: {r.get('note', '')}  [{r['clin_sig_rsid_level']}]")
            continue
        tail = f" tail {r['novel_tail']}" if r["novel_tail"] else ""
        if r["kind"] == "start_lost":
            ctx = "first AUG then met by a scanning ribosome is c.47 (out of frame)"
        elif r.get("next_met"):
            ctx = (f"stop codon {r['ptc_codon']} (c.{r['stop_c']}_{r['stop_c'] + 2}); next in-frame AUG Met{r['next_met']}, "
                   f"{r['gap_nt']} nt on; Cohen window: {'yes' if r['within_cohen_window'] else 'no'}")
        else:
            ctx = f"stop codon {r['ptc_codon']}"
        print(f"{r['rsid']:13s} {r['hgvs_c']:22s} {r['hgvs_p']:20s}{tail:14s} {ctx}  [{r['clin_sig_rsid_level'] or 'no ClinVar term'}]")
    n_trunc = sum(1 for r in rs if r["kind"] in ("nonsense", "frameshift"))
    n_start = sum(1 for r in rs if r["kind"] == "start_lost")
    same_stop = sum(1 for r in rs if r.get("stop_c") == 158)
    print(f"\n{n_trunc} truncating alleles and {n_start} start-loss alleles modelled; "
          f"{same_stop} end at the same stop codon as c.138del (c.158_160).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
