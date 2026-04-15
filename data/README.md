# Reference Data

This directory contains computationally useful reference data for POLE c.138del research. All data is derived from public databases and published literature.

## Contents

| File | Description | Source |
|------|-------------|--------|
| `POLE_coding_sequence.fa` | POLE coding sequence (ENST00000320574) | Ensembl/GENCODE |
| `POLE_domain_boundaries.tsv` | Protein domain boundaries for programmatic parsing | UniProt/InterPro |
| `POLE_downstream_methionines.tsv` | All in-frame downstream AUGs with Kozak context scores | Computed from ENST00000320574 |
| `POLE_gnomad_constraints.tsv` | gnomAD constraint metrics (pLI, LOEUF, missense Z) | gnomAD v4 |
| `POLE_clinvar_variants.tsv` | Curated POLE variants with ClinVar classifications | ClinVar |
| `phenotype_hpo.tsv` | Patient phenotype mapped to Human Phenotype Ontology (HPO) terms | HPO (hpo.jax.org) |
| `phenotype_timeline.tsv` | Age-at-onset data for each finding with tissue turnover annotations | Clinical data + published tissue biology |
| `tissue_replication_rates.tsv` | Tissue-specific cell division rates with POLE vulnerability predictions and Model 4 support assessment | Published tissue biology literature |

## Tissue Replication Rate Overlay

The `tissue_replication_rates.tsv` file maps 12 affected tissues to estimated cell division periods, enabling direct testing of Model 4's prediction that high-turnover tissues are most vulnerable to POLE haploinsufficiency. Combined with the temporal onset data in `phenotype_timeline.tsv`, these files generate the visualizations in [`analysis/temporal_phenotype/`](../analysis/temporal_phenotype/).

## HPO Interoperability

The `phenotype_hpo.tsv` file maps all 16 clinical findings across the patient's five phenotype categories to standardized [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) terms. This enables:

- **Phenopacket export:** HPO terms can be directly embedded in [GA4GH Phenopackets](https://phenopacket-schema.readthedocs.io/) for standardized case sharing with collaborators and registries
- **Exomiser/AMELIE integration:** HPO-coded phenotypes are the required input for variant prioritization tools like [Exomiser](https://exomiser.monarchinitiative.org/) and [AMELIE](https://amelie.stanford.edu/)
- **Cross-cohort comparison:** Standardized terms enable phenotype matching across PPAP cohorts and rare disease databases (e.g., Matchmaker Exchange, DECIPHER)

**Note:** Some findings lack exact HPO terms (e.g., PASH, FNH, ultra-hypermutation). In these cases, the closest parent term is used with an explanatory note in the `notes` column. As HPO expands, more specific terms may become available.
