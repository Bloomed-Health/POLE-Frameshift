#!/usr/bin/env python3
"""Download the full POLE MANE Select CDS and UniProt protein and compare them with data/reference/.

Needs network access. Standard library only. Writes nothing unless --write is given.

    python3 scripts/fetch_reference.py            # compare only
    python3 scripts/fetch_reference.py --write    # also save the full sequences and a full methionine table

Status: written during the 2026-11-20 audit without network access; run end to end with --write on the same day during
the review of the audit (Ensembl CDS 6,861 nt, UniProt 2,286 aa, fixtures agree, 56 in-frame methionines). The
comparison logic is also exercised by tests/test_variant_facts.py with stand-in data.
"""
from __future__ import annotations

import argparse
import os
import sys
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.join(ROOT, "analysis", "variant_verification"))
import verify_c138del as v  # noqa: E402

ENSEMBL = "https://rest.ensembl.org/sequence/id/ENST00000320574?type=cds;content-type=text/plain"
UNIPROT = "https://rest.uniprot.org/uniprotkb/Q07864.fasta"


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "POLE-Frameshift-verification/1.0"})
    with urllib.request.urlopen(req, timeout=60) as fh:
        return fh.read().decode()


def compare(full_cds: str, full_aa: str, fix_cds: str, fix_aa: str) -> list[str]:
    """Return a list of problems; empty means the fixtures are still a true prefix of the live sequences."""
    problems = []
    if not full_cds.startswith(fix_cds):
        problems.append("the CDS fixture is no longer a prefix of the Ensembl CDS")
    if not full_aa.startswith(fix_aa):
        problems.append("the protein fixture is no longer a prefix of UniProt Q07864")
    if len(full_cds) % 3:
        problems.append(f"CDS length {len(full_cds)} is not a multiple of 3")
    tr = v.translate(full_cds)
    if tr.rstrip("*") != full_aa:
        problems.append("the full CDS does not translate to the full UniProt sequence")
    return problems


def methionine_table(full_cds: str, full_aa: str) -> list[tuple[int, int, str, str]]:
    rows = []
    for k, aa in enumerate(full_aa, 1):
        if aa == "M":
            idx = 3 * (k - 1)
            ctx, strength = v.kozak(full_cds, idx)
            rows.append((k, idx + 1, ctx, strength))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    full_cds = "".join(get(ENSEMBL).split()).upper()
    full_aa = "".join(l.strip() for l in get(UNIPROT).splitlines() if not l.startswith(">"))
    _, fix_cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_1-480.fa"))
    _, fix_aa = v.read_fasta(os.path.join(v.REF, "POLE_Q07864_aa_1-240.fa"))
    print(f"Ensembl CDS: {len(full_cds)} nt; UniProt protein: {len(full_aa)} aa")
    problems = compare(full_cds, full_aa, fix_cds, fix_aa)
    for p in problems:
        print("PROBLEM:", p)
    if not problems:
        print("Fixtures agree with the live sequences.")
    rows = methionine_table(full_cds, full_aa)
    print(f"{len(rows)} in-frame methionines; first ten: {[r[0] for r in rows[:10]]}")
    if a.write and not problems:
        with open(os.path.join(v.REF, "POLE_MANE_cds_full.fa"), "w") as fh:
            fh.write(">ENST00000320574 full CDS (fetched by scripts/fetch_reference.py)\n")
            fh.writelines(full_cds[i:i + 60] + "\n" for i in range(0, len(full_cds), 60))
        with open(os.path.join(ROOT, "data", "POLE_all_methionines.tsv"), "w") as fh:
            fh.write("position_aa\tposition_cdna\tkozak_context\tkozak_strength\n")
            fh.writelines(f"M{k}\tc.{c}A\t{ctx}\t{s}\n" for k, c, ctx, s in rows)
        print("Wrote data/reference/POLE_MANE_cds_full.fa and data/POLE_all_methionines.tsv")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
