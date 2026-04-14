# Duplex Sequencing / NanoSeq Analysis Pipeline

## Overview

Ultra-high-accuracy somatic mutation detection in normal (non-tumor) cells to determine whether POLE c.138del causes elevated mutation rates in the germline — the key prediction of the haploinsufficiency model (Model 4).

## Rationale

Robinson et al. (2021, *Nature Genetics*) demonstrated that germline POLE/POLD1 carriers have elevated SBS10a/b signatures in normal somatic cells detectable by NanoSeq. If c.138del causes haploinsufficiency, the same elevation should be present in blood cells.

## Pipeline

```
Input:  PBMCs (and ideally colonic epithelium) from patient + age-matched controls
Method: NanoSeq (duplex sequencing at single-molecule resolution)
Output: Per-cell somatic mutation rate; trinucleotide spectrum; SBS signature decomposition
```

## Protocol

1. **DNA extraction** from PBMCs (minimum 1 μg high-molecular-weight DNA)
2. **NanoSeq library preparation** (2025 protocol: Pich et al., *Nature* 647:411–420)
3. **Sequencing** to achieve duplex consensus depth
4. **Error correction** using duplex consensus calling (<5 errors per billion bp)
5. **Variant calling** with NanoSeq pipeline
6. **Signature decomposition** of somatic mutations in normal cells

## Expected Results

| Outcome | Mutation rate | SBS10a/b | Interpretation |
|---------|-------------|----------|----------------|
| **Haploinsufficiency pathogenic** | Elevated vs. age-matched controls | Present in normal cells | 50% POLE dosage insufficient for proofreading fidelity |
| **LOH model confirmed** | Normal | Absent in normal cells | Mutagenesis is somatic (tumor-specific) event |
| **Intermediate** | Mildly elevated | Low-level SBS10a/b | Threshold model — partial haploinsufficiency |

## Complementary Assay

**CHIP profiling** (DNMT3A, TET2, ASXL1, TP53) provides indirect evidence of elevated mutation rate by measuring clonal hematopoiesis burden relative to age.

## Data Requirements

- Patient PBMCs (fresh or cryopreserved)
- Age- and sex-matched control PBMCs (minimum 3 controls)
- Colonic epithelial cells (if available from surveillance colonoscopy)
