# Mechanistic Models: Formal Hypotheses and Falsification Criteria

This document states each candidate model as a formal hypothesis with specific, falsifiable predictions and the experiments that test them.

---

## Model 1: Somatic Loss of Heterozygosity (LOH)

### Hypothesis

The wild-type POLE allele is somatically deleted or silenced in tumor tissue. Cells with no functional POLE rely on lower-fidelity compensatory polymerases (e.g., Polδ), producing ultra-hypermutation. This follows Knudson's two-hit tumor suppressor model.

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 1a | Tumor WGS will show LOH at 12q24.33 (deletion or copy-neutral LOH) | ASCAT/FACETS on paired tumor-normal WGS | Strongly supports Model 1 | Weakens Model 1 (but epigenetic silencing still possible) |
| 1b | Mutational signatures will show SBS10a/b/28 (POLE proofreading failure) | SigProfiler decomposition | Consistent with Model 1 | If non-POLE signatures: different mechanism entirely |
| 1c | Normal tissue (blood) NanoSeq will show **wild-type mutation rates** | Duplex sequencing on PBMCs | Supports Model 1 (mutagenesis is somatic event) | Elevated rates suggest haploinsufficiency (Model 4) |
| 1d | Wild-type POLE promoter may show methylation in tumor | Bisulfite sequencing of POLE promoter | Epigenetic two-hit mechanism | Rules out epigenetic silencing |

### Clinical Evidence Bearing on Model 1

The patient's **congenital duplicated inferior vena cava** argues against Model 1 as the *sole* explanation. LOH is a stochastic somatic event — it cannot explain a congenital vascular anomaly present from embryonic development. Additionally, the multi-system non-neoplastic findings (bilateral PASH, severe endometriosis, liver FNH) suggest germline-level tissue dysfunction beyond what somatic LOH in individual tumors would produce. Model 1 may still explain the ultra-hypermutation in specific tumors, but the systemic phenotype requires a complementary germline mechanism (likely Model 4).

### Exclusion Criteria

Model 1 is **excluded** as the sole mechanism if: congenital anomalies or multi-system proliferative findings are confirmed as POLE-related AND normal tissue mutation rates are elevated. Model 1 is excluded entirely if: tumor shows no LOH at POLE locus AND no promoter methylation AND wild-type allele is expressed at normal levels in tumor tissue.

---

## Model 2: Translational Reinitiation

### Hypothesis

Ribosomes encountering the premature stop codon at residue 54 reinitiate translation at a downstream in-frame AUG codon. If reinitiation occurs between the exonuclease domain (residue 268) and polymerase domain (residue 580), the resulting N-terminally truncated protein retains polymerase activity but lacks proofreading — phenocopying classical dominant-negative PPAP.

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 2a | Ribo-seq will show ribosome footprints at a downstream AUG in the POLE transcript | Ribosome profiling on patient cells | Strongly supports Model 2 | Weakens Model 2 |
| 2b | Western blot will show a truncated POLE protein band (predicted size depends on reinitiation site) | Anti-POLE antibody (C-terminal epitope) on patient cell lysates | Confirms aberrant protein product | No band = no reinitiation product |
| 2c | Mutational signatures will show SBS10a/b (canonical POLE proofreading failure) | SigProfiler decomposition | Consistent — reinitiation product acts like exo-dead POLE | Non-POLE signatures: different mechanism |
| 2d | Normal tissue mutation rates will be **elevated** (reinitiation occurs in all cells) | NanoSeq on PBMCs | Supports Model 2 (germline effect) | Normal rates favor Model 1 (somatic event) |

### Exclusion Criteria

Model 2 is **excluded** if: Ribo-seq shows no ribosome footprints downstream of codon 54 AND no truncated POLE protein is detected by proteomics AND mutant transcript undergoes complete NMD.

---

## Model 3: NMD Escape + Holoenzyme Poisoning

### Hypothesis

The premature termination codon escapes nonsense-mediated mRNA decay. The truncated 54-amino-acid peptide retains partial binding capacity for the POLE2 (p59) accessory subunit, competitively inhibiting holoenzyme assembly — a dominant-negative mechanism through stoichiometric poisoning rather than catalytic dysfunction.

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 3a | Mutant POLE mRNA will be detectable (NMD escape) | Allele-specific RNA-seq from blood | NMD escape confirmed | Complete NMD = no truncated peptide produced |
| 3b | The 54-residue peptide will co-immunoprecipitate with POLE2 | Co-IP of synthetic peptide with recombinant POLE2 | Binding confirmed — poisoning mechanism plausible | No binding = no stoichiometric competition |
| 3c | AlphaFold predicts structured interaction between residues 1–54 and POLE2 | Computational structural modeling | Structural basis for binding | Unstructured N-terminus unlikely to bind |
| 3d | Overexpression of the 54-residue peptide in cell lines reduces functional POLE holoenzyme levels | Transfection + POLE activity assay | Dominant-negative poisoning confirmed | No effect = peptide is inert |

### Exclusion Criteria

Model 3 is **excluded** if: mutant mRNA undergoes complete NMD AND/OR the 54-residue peptide shows no binding to any holoenzyme component AND/OR AlphaFold predicts the N-terminal region is unstructured with no interaction surfaces.

---

## Model 4: Replication Stress-Dependent Haploinsufficiency

### Hypothesis

50% POLE dosage is adequate under basal conditions but becomes rate-limiting under replicative stress in rapidly dividing tissues (colonic crypts, endometrium). POLE proofreading operates near a threshold rather than a linear dose-response, and half-dosage tips specific tissues below this threshold.

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 4a | NanoSeq on PBMCs will show **mildly elevated** somatic mutation rates with SBS10a/b | Duplex sequencing vs. age-matched controls | Haploinsufficiency in blood (moderate turnover tissue) | Normal rates = haploinsufficiency insufficient |
| 4b | NanoSeq on colonic epithelium will show **more strongly elevated** rates than blood | Duplex sequencing on colonoscopy biopsies | Tissue-specific threshold effect in high-turnover tissue | Same rate as blood = no tissue specificity |
| 4c | Mutations will be enriched in late-replicating genomic regions | Mutation density vs. Repli-seq replication timing | Replication stress model supported | Uniform distribution = non-replication-dependent mechanism |
| 4d | No LOH at POLE locus in tumor | ASCAT/FACETS analysis | Consistent with haploinsufficiency (no second hit needed) | LOH present = Model 1 |
| 4e | Endometrial tissue from endometriosis lesions will show elevated mutation rates | NanoSeq on endometriotic tissue vs. eutopic endometrium | POLE haploinsufficiency drives endometrial tissue dysregulation | Normal rates = endometriosis unrelated to POLE |

### Clinical Evidence Supporting Model 4

The patient's phenotype provides the strongest clinical support for this model among all five candidates:

- **Congenital duplicated IVC:** A developmental anomaly present from embryogenesis cannot be caused by somatic LOH. Robinson et al. (2021) demonstrated germline POLE mutations affect mutation rates during early embryogenesis. This suggests POLE haploinsufficiency has **developmental consequences** — either through elevated embryonic mutation rates creating somatic mosaicism that disrupts vascular patterning, or through non-replicative POLE roles in developmental signaling.
- **Severe endometriosis + adenomyosis:** The endometrium is a rapidly cycling tissue with high cell turnover — exactly where replicative stress from half-dose POLE would be most consequential. The aggressive endometrial phenotype (Stage IV+ with diaphragmatic extension) without formal malignant transformation suggests POLE dysfunction alters endometrial biology at a **pre-malignant level**. Novel research question: does POLE haploinsufficiency contribute to endometriosis severity?
- **Multi-system vascular/stromal proliferation:** Bilateral PASH, liver FNH/hemangioma, and duplicated IVC collectively indicate a pattern of vascular-stromal proliferative abnormalities that cannot be explained by somatic events in individual organs — consistent with a germline dosage effect.
- **Tissue-specific cancer spectrum:** Polyposis in high-turnover GI epithelium + thyroid cancer (high mitotic rate gland) aligns with the threshold model where rapidly dividing tissues are preferentially affected.

### Exclusion Criteria

Model 4 is **excluded** if: normal tissue mutation rates are completely normal AND congenital anomaly and proliferative findings are confirmed as coincidental AND/OR tumor shows LOH at the POLE locus as the sole mechanism.

---

## Model 5: Isoform-Specific Effects

### Hypothesis

The c.138del differentially affects alternative POLE transcript variants. A tissue-specific isoform whose first exon doesn't include the deletion site would be unaffected, while the canonical isoform is eliminated. Alternatively, alternative splicing around the deletion site produces an aberrant transcript with neomorphic properties.

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 5a | Multiple POLE transcript isoforms exist with different first exons | GENCODE/RefSeq annotation + GTEx expression data | Isoform-specific effects possible | Single predominant isoform = Model 5 unlikely |
| 5b | Tissue-specific expression of POLE isoforms correlates with cancer spectrum | GTEx tissue-specific isoform expression analysis | Explains why specific tissues develop cancer | Uniform isoform expression = no tissue specificity |
| 5c | Isoform-specific RT-PCR shows differential expression of mutant vs. wild-type isoforms | RT-PCR with isoform-specific primers across tissues | Isoform-dependent variant effect | All isoforms equally affected |
| 5d | Proteomics detects isoform-specific truncated products | Mass spectrometry across multiple tissues | Aberrant isoform-specific products | No aberrant products |

### Exclusion Criteria

Model 5 is **excluded** if: POLE has a single predominant coding isoform across all relevant tissues AND c.138del falls in an exon shared by all isoforms.

---

## Temporal Sequence as Model Discriminator

The resolution of specific ages-at-diagnosis provides a powerful new discriminatory dataset. The chronological order of clinical manifestations can be compared against tissue-specific cell division rates to test Model 4's core prediction: that faster-dividing tissues should cross the proofreading fidelity threshold and present clinically *earlier*.

### Observed Temporal Sequence (Non-Congenital Findings)

| Age | Diagnosis | Tissue Turnover (days) |
|-----|-----------|----------------------|
| ~19 | Colonic adenomas (~6 at first colonoscopy) | 3–5 (very rapid) |
| ~19 | Chronic gastric gastritis | 2–8 (rapid) |
| ~22 | Endometriosis clinically significant | ~28/monthly (rapid) |
| ~26 | POTS | N/A (neural) |
| ~27 | Stage IV endometriosis diagnosed | ~28/monthly (rapid) |
| ~27 | Benign breast tumor (PASH) | Variable/hormonal (~60) |
| ~28 | Thyroid microcarcinoma (0.6 cm, encapsulated, non-invasive) | ~2,920 (~8 years; slow) |
| ~28 | Adenomyosis (severe → hysterectomy) | ~28/monthly (rapid) |

### Correlation Analysis

Plotting tissue turnover period (log scale) against age-at-diagnosis reveals a positive correlation: **tissues with faster cell division are diagnosed at younger ages**. The colonic epithelium (3–5 day turnover) produced detectable adenomas by age 19; the thyroid epithelium (~8-year turnover) produced carcinoma by age 28 — a 9-year latency difference that directly tracks the ~730-fold difference in cell division rate.

See `analysis/temporal_phenotype/turnover_vs_age_diagnosis.svg` for the visualization.

### Model-Specific Temporal Predictions

| Model | Temporal Prediction | Consistent with Observed Sequence? |
|-------|--------------------|------------------------------------|
| **M1 (LOH)** | No predicted temporal order — LOH is stochastic; any tissue could be affected first | **Partially inconsistent** — would predict random order, not turnover-correlated |
| **M2 (Reinitiation)** | All tissues affected simultaneously (reinitiation is constitutive); diagnosis order depends on tissue sensitivity and clinical detection | **Partially consistent** — but does not predict turnover-rate correlation |
| **M3 (Poisoning)** | All tissues affected simultaneously; no turnover prediction | **Inconsistent** — cannot explain turnover-correlated onset |
| **M4 (Haploinsufficiency)** | Faster-dividing tissues cross the threshold first → diagnosed at younger ages | **Strongly consistent** — observed sequence correlates with turnover rate |
| **M5 (Isoform)** | Depends on tissue-specific isoform expression, not turnover rate | **Neutral** — would predict expression-correlated, not turnover-correlated |

### Progressive Polyp Accumulation

The pattern of ~6 adenomas at age 19 with continued new polyp formation at every colonoscopic surveillance interval (ages 21, 24, 27, 29, ~31) indicates **ongoing mutagenesis** over >12 years. This progressive accumulation is:
- **Consistent with M4:** Constitutive haploinsufficiency produces a continuous elevated mutation rate in colonic stem cells, with new adenomas arising at each surveillance interval as additional stem cells accumulate sufficient driver mutations.
- **Consistent with M2:** If reinitiation produces a constitutive error-prone polymerase, mutation accumulation would also be continuous.
- **Less consistent with M1 as sole mechanism:** A single LOH event in one colonic stem cell would produce a clonal expansion, not geographically distributed new polyps at each interval. Multiple independent LOH events would be required — possible but requiring extraordinary coincidence.

---

## Clinical Phenotype as Model Discriminator

The patient's multi-system phenotype provides immediate discriminatory evidence even before experimental results.

| Finding | M1 (LOH) | M2 (Reinitiation) | M3 (Poisoning) | M4 (Haplo.) | M5 (Isoform) |
|---------|----------|-------------------|----------------|-------------|-------------|
| **Duplicated IVC (congenital)** | ❌ Cannot explain (LOH is somatic) | Neutral | Neutral | ✅ Supports (germline developmental effect) | Neutral |
| **Stage IV+ endometriosis** | Neutral | Neutral | Neutral | ✅ Supports (high-turnover tissue threshold) | Possible (isoform-specific endometrial effect) |
| **Bilateral PASH + liver FNH** | ❌ Unlikely (multi-organ, non-neoplastic) | Neutral | Neutral | ✅ Supports (systemic stromal/vascular proliferation) | Neutral |
| **Thyroid carcinoma** | Possible (organ-specific LOH) | Possible | Neutral | ✅ Supports (high mitotic rate gland) | Possible |
| **GI polyposis** | Possible | Possible | Possible | ✅ Supports (high-turnover epithelium) | Possible |

**Summary:** The congenital duplicated IVC is the single most important clinical discriminator — it cannot be explained by any somatic mechanism (Models 1–3) and provides direct evidence for a germline-level effect (Model 4). The multi-system non-neoplastic findings (PASH, FNH, severe endometriosis) collectively argue against Model 1 operating alone, as LOH in each organ independently would be an extraordinary coincidence. The clinical phenotype most strongly supports Model 4, potentially in combination with Model 1 for tumor-specific ultra-hypermutation.

---

## Discriminatory Power Matrix

This matrix shows which experiments most efficiently discriminate between models.

| Experiment | M1 (LOH) | M2 (Reinitiation) | M3 (Poisoning) | M4 (Haplo.) | M5 (Isoform) | Priority |
|-----------|----------|-------------------|----------------|-------------|-------------|----------|
| **Tumor WGS + LOH** | ✅ Definitive | — | — | ✅ Rules out if LOH | — | **Immediate** |
| **Mutational signatures** | ✅ Confirms POLE mechanism | ✅ Confirms POLE mechanism | — | — | — | **Immediate** |
| **Blood NanoSeq** | ✅ Normal = somatic | ✅ Elevated = germline | — | ✅ Elevated = threshold | — | **Immediate** |
| **Allele-specific RNA-seq** | — | ✅ Transcript present | ✅ NMD escape test | — | ✅ Isoform ratios | **Immediate** |
| **Endometriosis tissue NanoSeq** | — | — | — | ✅ Elevated = threshold in high-turnover tissue | — | **Medium-term** |
| **Ribo-seq** | — | ✅ Definitive | — | — | — | **Medium-term** |
| **Co-IP / structural modeling** | — | — | ✅ Definitive | — | — | **Medium-term** |
| **Replication timing analysis** | — | — | — | ✅ Enrichment pattern | — | **Medium-term** |
| **Isoform-specific RT-PCR** | — | — | — | — | ✅ Definitive | **Medium-term** |
| **Thyroid tumor signature analysis** | ✅ If LOH at POLE | ✅ If SBS10a/b present | — | — | — | **Immediate** |
