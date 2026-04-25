# Loss of Heterozygosity Analysis Framework

## Overview

Allele-specific copy number analysis of the POLE locus (12q24.33) in tumor tissue to test whether the wild-type POLE allele is somatically lost ; the central prediction of the two-hit tumor suppressor model (Model 1).

## Pipeline

```
Input:  Paired tumor-normal WGS BAMs (≥60x tumor / ≥30x normal)
Tools:  ASCAT / FACETS / Sequenza
Output: Allele-specific copy number at POLE locus; genome-wide LOH map
```

## Key Analysis

1. **Allele-specific copy number at 12q24.33** ; Is the wild-type POLE allele deleted?
2. **Copy-neutral LOH detection** ; Mitotic recombination can cause LOH without copy number change
3. **Promoter methylation analysis** ; Epigenetic silencing of the wild-type allele (requires bisulfite sequencing or methylation array)
4. **Genome-wide LOH landscape** ; Compare against published POLE-mutant tumor profiles

## Tools

| Tool | Strengths | Input |
|------|-----------|-------|
| **ASCAT** | Allele-specific copy number, tumor ploidy/purity estimation | WGS BAMs |
| **FACETS** | Copy-neutral LOH detection, joint segmentation | WGS/WES BAMs |
| **Sequenza** | Allele-specific copy number with GC correction | WGS BAMs |
| **PURPLE** (GRIDSS/LINX) | Structural variant-aware copy number | WGS BAMs |
| **Battenberg** | Subclonal copy number estimation; handles polyclonal tumors | WGS BAMs |
| **HATCHet** | Copy number and clone proportions jointly across multiple samples; designed for multi-region or hypermutated tumors where standard tools may fail | WGS BAMs |

> **Note on hypermutated tumors:** Ultra-hypermutated tumors (TMB >100 mut/Mb) can confound standard allele-specific copy number tools due to the density of somatic variants affecting allele frequency distributions. Battenberg and HATCHet are more robust in this setting. Running multiple tools and comparing results is recommended.

## Expected Results

- **If LOH present:** Confirms Knudson two-hit model for this variant; reclassifies POLE truncation as tumor-suppressor mechanism
- **If no LOH:** Rules out Model 1; redirects focus to reinitiation, NMD escape, or haploinsufficiency models
- **If copy-neutral LOH:** Indicates mitotic recombination ; requires specific analytical tools to detect

## Data Requirements

- Paired tumor-normal WGS BAMs (minimum 30x normal, 60x tumor)
- SNP heterozygosity data across chromosome 12
- Tumor purity estimate
