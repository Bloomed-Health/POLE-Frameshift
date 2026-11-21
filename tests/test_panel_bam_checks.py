"""The pileup parser and statistics behind analysis/panel_bam_checks, on synthetic input (no samtools needed)."""
import os

import panel_bam_checks as p
import verify_c138del as v


def test_parse_heterozygous_deletion_column():
    col = "^F." + "....." + ",,,,," + ".-1C" * 5 + ",-1c" * 4 + ".$"
    t = p.allele_table("G", p.parse_bases(col))
    assert t["depth"] == 21 and t["alleles"] == {"G": [12, 9]} and t["indels"] == {"-1C": [5, 4]}


def test_parse_handles_read_start_quality_that_looks_like_a_base():
    # "^A" is a read start with mapping quality 'A', not an A base; "^+" must not be read as an insertion
    t = p.allele_table("C", p.parse_bases("^A.^+,T$"))
    assert t["depth"] == 3 and t["alleles"] == {"C": [1, 1], "T": [1, 0]} and t["indels"] == {}


def test_parse_insertion_placeholder_and_skip():
    parsed = p.parse_bases(".+2AT,+2at*#<>")
    assert parsed["indel"][("+2AT", "f")] == 1 and parsed["indel"][("+2AT", "r")] == 1
    assert parsed["placeholder"] == 2 and parsed["skip"] == 2
    assert p.allele_table("A", parsed)["depth"] == 2


def test_without_reference_the_majority_allele_is_the_reference():
    t = p.allele_table("N", p.parse_bases("GGGGggggCc"))
    assert t["ref"] == "G" and t["alleles"]["C"] == [1, 1]


def test_mosaic_candidates_need_both_strands_and_a_fraction_window():
    deep = "." * 300 + "," * 290
    assert p.candidates(p.allele_table("C", p.parse_bases(deep + "T" * 6 + "t" * 5)), 5, 0.01, 0.35)[0]["count"] == 11
    assert p.candidates(p.allele_table("C", p.parse_bases(deep + "T" * 11)), 5, 0.01, 0.35) == []         # one strand only
    assert p.candidates(p.allele_table("C", p.parse_bases("." * 10 + "," * 10 + "T" * 10 + "t" * 10)), 5, 0.01, 0.35) == []  # heterozygous


def test_build_detection():
    assert p.detect_build("@HD\tVN:1.6\n@SQ\tSN:chr12\tLN:133275309\n") == ("GRCh38", "chr")
    assert p.detect_build("@SQ\tSN:12\tLN:133851895") == ("GRCh37", "")


def test_power_and_heterozygosity_statistics():
    assert round(p.binom_tail(600, 0.01, 5), 2) == 0.72
    assert round(p.binom_tail(30, 0.10, 3), 2) == 0.59
    assert p.binom_two_sided_half(20, 10) == 1.0
    assert p.binom_two_sided_half(600, 90) < 1e-6


def test_site_coordinates_agree_with_the_derivation():
    segs = v.cds_segments(v.read_exons(os.path.join(v.REF, "POLE_MANE_exons_GRCh38.tsv")))
    assert p.POLE_SITES["c.138del"][0] == v.cds_to_grch38(138, segs)[1] - 1
    assert p.POLE_SITES["c.1686+32C>G"][0] == v.cds_to_grch38(1686, segs)[1] - 32
    assert p.POLE_SITES["c.4444+3A>G"][0] == v.cds_to_grch38(4444, segs)[1] - 3
    assert p.site_region("c.138del", "GRCh37", "")[0] == "12:133257789-133257789"
    assert p.GRCH37_OFFSET == v.GRCH37_MINUS_GRCH38_EXON2


def test_gene_region_follows_the_build_and_contig_naming():
    assert p.gene_region("APC", "GRCh38", "chr") == "chr5:112707452-112846239"
    assert p.gene_region("APC", "GRCh37", "") == "5:112043195-112181936"
