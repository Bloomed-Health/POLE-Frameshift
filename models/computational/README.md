# Computational Models: Stochastic Crypt Dynamics

## Overview

Agent-based stochastic models of colonic crypt stem cell dynamics under varying POLE dosage to predict mutation accumulation rates, LOH probability, time-to-adenoma, and optimal surveillance intervals.

## Model Specifications

### Parameters

- **Crypt stem cell number:** ~5–7 per crypt (Lgr5+ stem cells)
- **Stem cell division rate:** ~1 division per day
- **Background mutation rate:** ~1.3 mutations per division per genome (SBS1/SBS5)
- **POLE proofreading error correction factor:** ~100-fold reduction in replication errors
- **POLE dosage scenarios:** 100% (wild-type), 50% (heterozygous null), 0% (LOH)

### Key Questions

1. At 50% POLE dosage, how much does the per-division mutation rate increase?
2. What is the probability of LOH at the POLE locus per crypt per year?
3. How long until a crypt accumulates sufficient driver mutations for adenoma initiation?
4. What surveillance colonoscopy interval optimally balances detection sensitivity with patient burden?

### Calibration Data

- Published single-cell WGS mutation rates from normal colonic crypts (Lee-Six et al., 2019)
- NanoSeq data from POLE/POLD1 carriers (Robinson et al., 2021)
- LOH rates from published cancer genomics cohorts (Yoshida et al., 2022)

## Tools

- Python (NumPy, SciPy) or Julia for stochastic simulation
- Gillespie algorithm for continuous-time Markov chain modeling
- ABC (Approximate Bayesian Computation) for parameter inference

## Data Inputs Needed

- Patient-specific somatic mutation rate from NanoSeq (when available)
- Tumor LOH status and copy number profile
- Published crypt dynamics parameters from literature
