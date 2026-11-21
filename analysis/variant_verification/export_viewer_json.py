#!/usr/bin/env python3
"""Write pole_mutations.json for the 3D-POLE-Modeler mutation viewer from the verified fixtures.

The viewer (js/mutation-viewer.js in Bloomed-Health/3D-POLE-Modeler) reads ./data/pole_mutations.json and
falls back to hard-coded codons when the file is missing. This script makes the verified derivation the
single source for both repositories.

    python3 analysis/variant_verification/export_viewer_json.py > /path/to/3D-POLE-Modeler/data/pole_mutations.json
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_c138del as v  # noqa: E402

FIRST, LAST = 43, 53        # codon window shown by the viewer


def build() -> dict:
    rep = v.build_report()
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_1-480.fa"))
    mut = cds[:137] + cds[138:]
    c = rep["c138del"]
    aa3 = lambda codon: "*" if v.CODON[codon] == "*" else v.AA3[v.CODON[codon]]
    wt = [{"codon": cds[3 * k - 3:3 * k], "aa": aa3(cds[3 * k - 3:3 * k]), "pos": k} for k in range(FIRST, LAST + 1)]
    mt = []
    for k in range(FIRST, c["stop_codon_number"] + 1):
        codon = mut[3 * k - 3:3 * k]
        status = "normal" if k < c["codon_number"] else ("stop" if v.CODON[codon] == "*" else "frameshift")
        mt.append({"codon": codon, "aa": aa3(codon), "pos": k, "status": status})
    nxt = rep["first_atg_after_ptc"]
    return {
        "frameshift": {
            "hgvs_c": "NM_006231.4:c.138del", "hgvs_p": "NP_006222.2:" + c["hgvs_p"],
            "wt_codons": wt, "mut_codons": mt,
            "truncation_site": c["stop_codon_number"], "total_residues": 2286,
            "translated_residues": c["truncated_length_aa"], "native_residues": c["native_residues"],
            "novel_peptide": c["novel_residues"], "stop_codon": c["stop_codon"],
            "next_in_frame_aug": {"codon": nxt["codon_number"], "c": nxt["cds_pos"], "kozak": nxt["kozak"],
                                  "nt_after_stop": nxt["nt_between_stop_and_atg"],
                                  "residues_missing_if_used": nxt["residues_missing_if_used"]},
            "start_codon_context": rep["start_codon_context"],
        },
        "provenance": {
            "generated_by": "POLE-Frameshift/analysis/variant_verification/export_viewer_json.py",
            "transcript": "ENST00000320574.10 (NM_006231.4, MANE Select)",
            "fixtures": rep["fixtures"],
            "note": "Sequence facts only. Whether translation restarts at the next AUG is untested.",
        },
    }


if __name__ == "__main__":
    json.dump(build(), sys.stdout, indent=2)
    print()
