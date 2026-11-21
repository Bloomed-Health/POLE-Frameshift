# Verified reference fixtures

Small, checked-in slices of the POLE reference, so that every sequence-level statement in this repository can be
recomputed offline. Retrieved on 2026-11-20. Nothing here was typed from memory.

| File | Content | Source | How it was checked |
|------|---------|--------|--------------------|
| `POLE_MANE_cds_1-480.fa` | First 480 nt of the ENST00000320574.10 coding sequence (MANE Select; RefSeq match NM_006231.4) | Ensembl REST `sequence/id/ENST00000320574?type=cds` | Translates to the first 160 residues of UniProt Q07864 with no mismatch (`verify_c138del.py`, step 1) |
| `POLE_MANE_cds_full.fa` | The full 6,861-nt coding sequence of ENST00000320574.10 | Ensembl REST, written by `scripts/fetch_reference.py --write` on 2026-11-20 | Translates to all 2,286 residues of UniProt Q07864 with no mismatch; the 480-nt file is its prefix (`tests/test_variant_facts.py`). Used to verify every substitution in `data/POLE_clinvar_variants.tsv` and to list all 56 in-frame methionines (`data/POLE_all_methionines.tsv`) |
| `POLE_Q07864_aa_1-240.fa` | First 240 residues of UniProt Q07864 | UniProt REST | Independent of the Ensembl file; agreement of the two is the cross-check |
| `POLE_MANE_exons_GRCh38.tsv` | The 49 exons of ENST00000320574.10 on GRCh38 (minus strand) | Ensembl REST `lookup/id/ENST00000320574?expand=1` | c.138 maps to chr12:132681204; Ensembl VEP independently returns the same position for c.138del, and chr12:132672595 for c.1686+32C>G |
| `POLE_MANE_5utr_last6.fa` | c.-6 to c.-1 | Ensembl REST `sequence/region/human/12:132687312..132687321:-1` (returned `GGCTCCATGT`) | The last four letters equal the start of the CDS fixture; the dbSNP allele string of rs2043299858 gives the same bases |
| `POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv` | Start-loss, nonsense, frameshift and splice-donor records in exons 1 and 2 | Ensembl REST `overlap/region/human/12:...?feature=variation` | Transcribed by hand from the API output; `nterm_truncations.py` re-checks every reference allele against the CDS fixture and fails on a mismatch |
| `POLE_clinvar_PLP_2026-11-21.tsv` (+ `.summary.txt`) | Every ClinVar POLE record with germline classification Pathogenic or Likely pathogenic on the date in the name: 497 records with cDNA/protein change, consequence, review status, conditions and GRCh38 position. The gene query also returns records annotated to neighbouring genes; one P2RX2 missense (VCV004082203) was dropped by the script's title filter on the second run the same day | NCBI E-utilities via `analysis/variant_verification/fetch_clinvar_pole.py` | Dated snapshot; re-run the script to refresh. Summary: 413 truncating, 12 missense (10 in the exonuclease domain), 72 other. `tests/test_scientific_consistency.py` recomputes the summary from the TSV and checks every point variant lies in the POLE transcript |

## Limits

- The protein fixture holds only the first 240 residues; the full CDS is held and translates to the full UniProt sequence,
  so statements about residues beyond 240 (for example the exonuclease active site) can be recomputed from `POLE_MANE_cds_full.fa`.
- The exon table was re-compared with the live Ensembl record on 2026-11-20 (49 exons, identical coordinates).
- The GRCh37 coordinates are obtained by adding 576,586 to the GRCh38 position. Ensembl's assembly mapper returns the whole
  gene (GRCh38 132623762-132687342) as a single block at GRCh37 133200348-133263928, so the offset is constant inside POLE
  and nowhere else.
- ClinVar terms in the truncating-variant table are aggregated per rsID by Ensembl. At multi-allelic sites they are not
  allele-specific.

To refresh or extend the fixtures on a machine with network access, run `python3 scripts/fetch_reference.py`.
It downloads the full CDS and protein, confirms that they still agree with these files, and reports any difference.
