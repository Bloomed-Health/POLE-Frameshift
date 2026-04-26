# Mutational Signature Analysis Pipeline

> **STATUS: Not yet performed.** Mutational signature decomposition is the **single most diagnostic readout available** for this case ; it directly discriminates between POLE-driven hypermutation (SBS10a/b/28) and MMR-deficient phenocopy (SBS6/15/21/26). This analysis should be treated as the **highest-priority immediate experiment**. Until signature decomposition is performed, the assumption that the ultra-hypermutation is POLE-driven remains unverified. Archived tumour specimens (FFPE thyroidectomy, ~2019; hysterectomy, ~2021) are potential input material.

## Overview

SigProfiler-based decomposition of tumor whole-genome sequencing data to identify the mutational processes driving ultra-hypermutation in the POLE c.138del tumor.

## Pipeline

```
Input:  VCF from paired tumor-normal WGS (≥60x tumor / ≥30x normal)
Tools:  SigProfilerMatrixGenerator → SigProfilerExtractor → SigProfilerAssignment
Output: Signature contribution weights (COSMIC v3.4 SBS, DBS, ID)
```

## Key Signatures to Quantify

| Signature | Associated Process | Significance |
|-----------|--------------------|-------------|
| **SBS10a** | POLE exonuclease domain mutation (C>A in TCT) | Canonical POLE proofreading failure |
| **SBS10b** | POLE exonuclease domain mutation (C>T in TCG) | Canonical POLE proofreading failure |
| **SBS28** | POLE-associated (secondary) | Supports POLE-driven mutagenesis |
| SBS6/15/21/26 | MMR deficiency | Alternative mutational mechanism |
| SBS2/13 | APOBEC activity | Non-POLE mechanism |
| SBS1/5 | Clock-like (age-related) | Tumor age estimation |

## Interpretation Framework

- **SBS10a/b ≥50%:** Canonical POLE mechanism ; favors LOH or reinitiation models
- **SBS10a/b <10%, MMR signatures dominant:** Non-POLE mechanism ; would require reassessment of the PPAP hypothesis for this case
- **Novel signature:** Previously undescribed mutational process ; requires further characterization
- **POLE signature ≥78.5%:** Predicts ICI response (Pietrantonio et al., Annals of Oncology 2024)

## Additional Tools

- **MutationalPatterns** (R/Bioconductor): Alternative decomposition and visualization
- **deconstructSigs**: Signature weight estimation
- **COSMIC v3.4**: Reference signature database

## Data Requirements

- Paired tumor-normal WGS (VCF format)
- Reference genome: GRCh38
- Minimum tumor purity: 30% (recommended >50%)
