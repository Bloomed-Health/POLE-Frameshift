# Reference Data

This directory contains computationally useful reference data for POLE c.138del research. All data is derived from public databases and published literature.

## Contents

| File | Description | Source |
|------|-------------|--------|
| `reference/` | Verified MANE Select fixtures: the full 6,861-nt ENST00000320574.10 CDS and its first 480 nt, the first 240 residues of UniProt Q07864, the 49-exon GRCh38 table, the start-codon context, and dbSNP/ClinVar truncating variants in exons 1-2 (see `reference/README.md`). Replaces `POLE_coding_sequence.fa`, which was not POLE | Ensembl REST, UniProt (2026-11-20) |
| `POLE_domain_boundaries.tsv` | Literature domain boundaries used by the figures and text (Liu & Linn 2000; Church 2013; Korona 2011). UniProt Q07864 itself annotates no domain in the first 2,000 residues | Literature, as cited per row |
| `POLE_domains_interpro.tsv` | Database-anchored domain boundaries with accessions (CDD, Pfam, SMART, UniProt). CDD cd05779 (268-471) coincides with the "narrow exonuclease" range | InterPro API, UniProt REST (2026-11-20) |
| `POLE_downstream_methionines.tsv` | In-frame AUGs in residues 1-240 with Kozak context, regenerated from the fixtures | `analysis/variant_verification/verify_c138del.py` |
| `POLE_all_methionines.tsv` | All 56 in-frame AUGs in the full CDS with Kozak context | `scripts/fetch_reference.py --write` (2026-11-20) |
| `POLE_gnomad_constraints.tsv` | gnomAD v4.1 constraint metrics (pLI, LOEUF, oe_lof, missense and synonymous Z); every value re-verified against the gnomAD API on 2026-11-20 | gnomAD v4.1 |
| `POLE_clinvar_variants.tsv` | Curated POLE variants. Nucleotide and codon of every substitution verified against the full MANE CDS; ClinVar variation IDs and germline classifications checked on 2026-11-20 (the three IDs previously listed were MEN1 records) | ClinVar, full CDS fixture |
| `claims_ledger.tsv` | One row per factual claim with status, source and verification date | 2026-11-20 audit |
| `phenotype_hpo.tsv` | Patient phenotype mapped to Human Phenotype Ontology (HPO) terms; every ID and label checked against the HPO API on 2026-11-20 (none obsolete) | HPO (hpo.jax.org) |
| `phenotype_timeline.tsv` | Age-at-onset data for each finding. Ages and findings are repository-owner statements (ledger rows P03-P08). `tissue_key` (added 2026-11-21) names the row of `tissue_replication_rates.tsv` each finding joins to (empty for the comorbidity triad, which has no turnover row); the free-text `tissue_turnover_rate` label must agree with that row, which a test enforces. The n = 6 dataset behind the notebook's Spearman test is reproducible from this join except for two entries the tables do not support (breast turnover 60 days; adenomyosis as a tissue separate from endometrium); `tests/test_scientific_consistency.py::test_notebook_dataset_versus_the_tables` records that | Owner statements + `tissue_replication_rates.tsv` |
| `tissue_replication_rates.tsv` | Tissue-specific cell division rates with POLE vulnerability predictions and Model 4 support assessment. Since 2026-11-21 each row carries `source` (PMID and the figure in its abstract) and `source_status` (CITED, PHYSIOLOGY, PARTLY SOURCED or UNSOURCED); the HSC value was corrected from 40 days to once per ~40 weeks | PubMed abstracts as cited per row |
| `cosmic_signatures_cited.tsv` | Every COSMIC SBS signature named in this repository with the proposed aetiology and comment copied from the COSMIC signatures site, and how the repository uses it | cancer.sanger.ac.uk/signatures (2026-11-21) |

## Tissue Replication Rate Overlay

The `tissue_replication_rates.tsv` file maps 12 affected tissues to estimated cell division periods, enabling direct testing of Model 4's prediction that high-turnover tissues are most vulnerable to POLE haploinsufficiency. Combined with the temporal onset data in `phenotype_timeline.tsv`, these files generate the visualizations in [`analysis/temporal_phenotype/`](../analysis/temporal_phenotype/).

## HPO Interoperability

The `phenotype_hpo.tsv` file maps all 19 clinical findings (five phenotype categories plus the three comorbidity-triad terms, added 2026-11-21 so that the table and the phenopacket list the same findings) to standardized [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) terms. This enables:

- **Phenopacket export:** HPO terms can be directly embedded in [GA4GH Phenopackets](https://phenopacket-schema.readthedocs.io/) for standardized case sharing with collaborators and registries
- **Exomiser/AMELIE integration:** HPO-coded phenotypes are the required input for variant prioritization tools like [Exomiser](https://exomiser.monarchinitiative.org/) and [AMELIE](https://amelie.stanford.edu/)
- **Cross-cohort comparison:** Standardized terms enable phenotype matching across PPAP cohorts and rare disease databases (e.g., Matchmaker Exchange, DECIPHER)

**Note:** Some findings lack exact HPO terms (e.g., PASH, FNH). In these cases, the closest parent term is used with an explanatory note in the `notes` column. As HPO expands, more specific terms may become available. The "ultra-hypermutation" row was removed on 2026-11-20 because no tumour has been sequenced.
