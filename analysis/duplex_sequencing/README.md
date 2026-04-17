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

## Technology Selection: SMaHT Benchmarking (2025)

The SMaHT Network (Somatic Mosaicism across Human Tissues) benchmarked six duplex sequencing technologies — CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq, and VISTA-seq — using cord blood DNA, tumor-normal mixtures, and six human tissue homogenates (Zhang et al., 2025, *bioRxiv*).

Key findings relevant to technology selection:

| Technology | Duplex Recovery | Notes |
|-----------|----------------|-------|
| **ppmSeq** | 44% ± 5.5% | Highest duplex recovery; ultra-high throughput |
| **NanoSeq** | ~5–11% | Original method; well-validated for germline carrier studies (Robinson et al., 2021) |
| **HiDEF-seq** | ~5–11% | Comparable to NanoSeq |
| **CODEC/VISTA-seq** | ~5–11% | Alternative approaches |

Despite differences in library construction and sequencing platforms, mutation rate estimates and mutational signatures were **highly concordant** across all six methods. For this study, NanoSeq remains the preferred method (published POLE carrier data exists for direct comparison), but ppmSeq's 4–8× higher duplex recovery could enable more cost-effective profiling of multiple tissue types.

## Data Requirements

- Patient PBMCs (fresh or cryopreserved)
- Age- and sex-matched control PBMCs (minimum 3 controls)
- Colonic epithelial cells (if available from surveillance colonoscopy)
