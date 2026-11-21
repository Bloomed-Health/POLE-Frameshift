"""Sequence-level facts about POLE c.138del, recomputed from data/reference/ on every run."""
import csv
import os
import re

import export_viewer_json
import fetch_reference
import nterm_truncations as nt
import verify_c138del as v

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REP = v.build_report()


def test_two_independent_sources_agree():
    cv = REP["cross_validation"]
    assert cv["cds_nt"] == 480 and cv["identical_to_uniprot_prefix"] and not cv["mismatches"]


def test_protein_consequence():
    c = REP["c138del"]
    assert c["hgvs_p"] == "p.Leu46Phefs*8"
    assert (c["wt_codon"], c["mut_codon"], c["deleted_base"]) == ("TTG", "TTC", "G")
    assert c["hgvs_c_position_after_3prime_rule"] == 138          # no homopolymer: the name cannot shift
    assert c["stop_codon_number"] == 53 and c["stop_codon"] == "TGA"
    assert c["truncated_length_aa"] == 52 and c["native_residues"] == 45 and c["novel_residues"] == "FGLVLSG"
    assert tuple(c["stop_cds_wt_numbering"]) == (158, 160)


def test_genomic_coordinates():
    g = REP["genomic"]
    assert g["exon"] == "2/49" and g["exon_cds_range"] == "c.63-c.204"
    assert g["GRCh38"]["hgvs_g"] == "NC_000012.12:g.132681204del" and g["GRCh38"]["vcf"] == "12-132681203-GC-G"
    assert g["GRCh37"]["hgvs_g"] == "NC_000012.11:g.133257790del" and g["GRCh37"]["vcf"] == "12-133257789-GC-G"
    assert (g["dist_to_exon_5prime_end_nt"], g["dist_to_exon_3prime_end_nt"]) == (75, 66)


def test_retired_grch37_coordinate_is_a_different_site():
    back = REP["legacy_grch37_coordinate_check"]["maps_to"]
    assert back == {"exon": 14, "cds_pos": 1376, "codon": 459}


def test_recessive_allele_sites_match_ensembl_vep():
    segs = v.cds_segments(v.read_exons(os.path.join(v.REF, "POLE_MANE_exons_GRCh38.tsv")))
    assert v.cds_to_grch38(1686, segs)[1] - 32 == 132672595       # c.1686+32C>G, VEP 2026-11-20
    assert v.cds_to_grch38(4444, segs)[1] - 3 == 132643404        # c.4444+3A>G, VEP 2026-11-20


def test_start_codon_context_and_translation_map():
    assert REP["start_codon_context"] == {"kozak": "TCCATGT", "strength": "weak"}
    mut = {o["atg_c"]: o for o in REP["orf_map_c138del"]}
    assert [mut[c]["codons"] for c in (1, 47, 65, 68, 130)] == [52, 34, 28, 27, 9]
    assert all(mut[c]["stop_c"][1] <= 160 for c in (1, 47, 65, 68, 130))
    assert mut[130]["peptide"] == "MDFGLVLSG"
    assert mut[196]["stop_c"] is None                              # Met66 reads on into POLE
    assert REP["first_atg_after_ptc"]["cds_pos"] == 196 and REP["first_atg_after_ptc"]["codon_number"] == 66
    assert REP["first_atg_after_ptc"]["nt_between_stop_and_atg"] == 35
    assert REP["in_frame_methionines_1_240"] == [1, 44, 66, 221]
    assert REP["exon2"] == {"cds_nt": 142, "skipping_keeps_frame": False}


def test_neighbouring_truncations():
    rows = nt.rows()
    assert not [r for r in rows if r["kind"] == "REFERENCE_MISMATCH"]
    by_c = {r.get("hgvs_c"): r for r in rows}
    assert by_c["c.138del"]["hgvs_p"] == "p.Leu46Phefs*8" and by_c["c.138del"]["rsid"] == "rs1555230420"
    assert by_c["c.137del"]["hgvs_p"] == "p.Leu46Cysfs*8" and by_c["c.137del"]["novel_tail"] == "CGLVLSG"
    assert by_c["c.141del"]["hgvs_p"] == "p.Phe48Leufs*6"
    assert by_c["c.1A>T"]["kind"] == "start_lost"
    assert sum(r["kind"] in ("nonsense", "frameshift") for r in rows) == 26
    assert sum(r["kind"] == "start_lost" for r in rows) == 8
    assert sum(r.get("stop_c") == 158 for r in rows) == 5
    assert by_c["c.138del"]["next_met"] == 66 and by_c["c.138del"]["within_cohen_window"]


def test_methionine_table_matches_the_derivation():
    with open(os.path.join(ROOT, "data", "POLE_downstream_methionines.tsv"), encoding="utf-8") as fh:
        rows = {r["position_aa"]: r for r in csv.DictReader(fh, delimiter="\t")}
    assert set(rows) == {"M1", "M44", "M66", "M221"}
    wt = {o["atg_c"]: o for o in REP["orf_map_wild_type"]}
    for name, c in (("M1", 1), ("M44", 130), ("M66", 196)):
        assert rows[name]["position_cdna"] == f"c.{c}A"
        assert rows[name]["kozak_context"] == wt[c]["kozak"]
        assert rows[name]["kozak_strength"].lower() == wt[c]["strength"]


def _full_cds():
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_full.fa"))
    return cds


def test_full_cds_fixture_is_consistent():
    cds = _full_cds()
    _, short = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_1-480.fa"))
    _, aa240 = v.read_fasta(os.path.join(v.REF, "POLE_Q07864_aa_1-240.fa"))
    assert len(cds) == 6861 and cds.startswith(short)
    protein = v.translate(cds)
    assert protein.endswith("*") and len(protein) - 1 == 2286 and protein.startswith(aa240)
    with open(os.path.join(ROOT, "data", "POLE_all_methionines.tsv"), encoding="utf-8") as fh:
        mets = [int(r["position_aa"][1:]) for r in csv.DictReader(fh, delimiter="\t")]
    assert mets == [i + 1 for i, a in enumerate(protein) if a == "M"]
    assert mets[:4] == [1, 44, 66, 221]


def test_variant_table_substitutions_match_the_reference():
    cds = _full_cds()
    aa3 = {"A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys", "Q": "Gln", "E": "Glu", "G": "Gly", "H": "His",
           "I": "Ile", "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe", "P": "Pro", "S": "Ser", "T": "Thr", "W": "Trp",
           "Y": "Tyr", "V": "Val", "*": "Ter"}
    with open(os.path.join(ROOT, "data", "POLE_clinvar_variants.tsv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    checked = 0
    for r in rows:
        m = re.fullmatch(r"c\.(\d+)([ACGT])>([ACGT])", r["variant_cdna"])
        if not m:
            continue
        pos, ref, alt = int(m[1]), m[2], m[3]
        assert cds[pos - 1] == ref, r["variant_cdna"]
        codon = (pos - 1) // 3
        wt = cds[3 * codon:3 * codon + 3]
        mut = wt[:(pos - 1) % 3] + alt + wt[(pos - 1) % 3 + 1:]
        expected = f"p.{aa3[v.CODON[wt]]}{codon + 1}{aa3[v.CODON[mut]]}"
        assert r["variant_protein"] == expected, (r["variant_cdna"], r["variant_protein"], expected)
        assert not r["clinvar_variation_id"].startswith("ClinVar:3652"), "MEN1 record IDs retired 2026-11-20"
        checked += 1
    assert checked == 8


def test_fetch_script_comparison_logic():
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_1-480.fa"))
    _, aa = v.read_fasta(os.path.join(v.REF, "POLE_Q07864_aa_1-240.fa"))
    stand_in_cds, stand_in_aa = cds + "TGA", aa[:160]
    assert fetch_reference.compare(stand_in_cds, stand_in_aa, cds, aa[:160]) == []
    broken = "ATGGCT" + cds[6:] + "TGA"
    assert fetch_reference.compare(broken, stand_in_aa, cds, aa[:160])
    assert [r[0] for r in fetch_reference.methionine_table(cds, aa[:160])] == [1, 44, 66]


def test_viewer_export_matches_the_derivation():
    fs = export_viewer_json.build()["frameshift"]
    assert [c["aa"] for c in fs["wt_codons"]] == ["Lys", "Met", "Asp", "Leu", "Arg", "Phe", "Gly", "Phe", "Glu", "Arg", "Leu"]
    assert [c["codon"] for c in fs["mut_codons"]][-1] == "TGA" and fs["mut_codons"][-1]["status"] == "stop"
    assert "".join(v.CODON[c["codon"]] for c in fs["mut_codons"] if c["status"] == "frameshift") == "FGLVLSG"
    assert fs["truncation_site"] == 53 and fs["next_in_frame_aug"]["codon"] == 66
