# Neoantigen Prediction Pipeline

## Overview

Computational prediction of tumor neoantigens from the ultra-hypermutated POLE c.138del tumor to inform immunotherapy strategy and neoantigen vaccination potential.

## Pipeline

```
Input:  Tumor VCF + patient HLA typing + tumor RNA-seq
Tools:  HLA typing (OptiType/HLA-HD) → pVACseq / NetMHCpan 4.1 → filtering
Output: Ranked neoantigen candidates with predicted HLA binding, expression, clonality
```

## Analysis Steps

1. **HLA typing** ; Class I (HLA-A, -B, -C) and Class II (HLA-DR, -DQ, -DP) from WGS or dedicated typing
2. **Somatic variant annotation** ; VEP/SnpEff for protein consequence prediction
3. **Peptide generation** ; 8-11mer (Class I) and 15-25mer (Class II) from mutant sequences
4. **Binding prediction** ; NetMHCpan 4.1 (Class I), NetMHCIIpan 4.0 (Class II)
5. **Expression filtering** ; RNA-seq TPM for variant allele expression
6. **Clonality assessment** ; Cancer cell fraction (CCF) from variant allele frequency
7. **Ranking** ; Prioritize clonal, expressed, strong-binding neoantigens

## Tools

| Tool | Purpose |
|------|---------|
| **pVACseq** | Integrated neoantigen prediction pipeline |
| **NetMHCpan 4.1** | MHC Class I binding prediction |
| **NetMHCIIpan 4.0** | MHC Class II binding prediction |
| **OptiType / HLA-HD** | HLA typing from WGS |
| **VEP / SnpEff** | Variant annotation |

## Clinical Application

- **ICI response prediction:** Neoantigen quality (not just quantity) predicts response
- **Neoantigen vaccination:** High-quality candidates for mRNA vaccine design (mRNA-4157/V940 platform)
- **Immune monitoring:** Peptide-MHC multimers for tracking neoantigen-reactive T cells

## Data Requirements

- Tumor WGS VCF with somatic mutations
- Patient HLA typing (Class I and II)
- Tumor RNA-seq (for expression filtering)
- Tumor purity and variant CCF estimates
