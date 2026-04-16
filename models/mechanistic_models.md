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

### Prior Probability Assessment

Model 2 has a **low prior probability**. Translational reinitiation efficiency drops sharply with increasing distance from the premature stop codon. The nearest candidate reinitiation site with strong Kozak context (M497) is ~1.3 kb downstream — far beyond the typical reinitiation window observed for mammalian mRNAs (Sherlock et al., 2023). While reinitiation has been documented in specialized contexts (uORFs, viral internal ribosome entry), efficient reinitiation across >1 kb of coding sequence in a standard mammalian mRNA would be unprecedented. This model remains formally testable but should be considered unlikely absent positive Ribo-seq evidence.

### Exclusion Criteria

Model 2 is **excluded** if: Ribo-seq shows no ribosome footprints downstream of codon 54 AND no truncated POLE protein is detected by proteomics AND mutant transcript undergoes complete NMD.

---

## Model 3: NMD Escape + Holoenzyme Poisoning

### Hypothesis

The premature termination codon escapes nonsense-mediated mRNA decay. The truncated 54-amino-acid peptide retains partial binding capacity for the POLE2 (p59) accessory subunit, competitively inhibiting holoenzyme assembly — a dominant-negative mechanism through stoichiometric poisoning rather than catalytic dysfunction.

### Prior Probability Assessment

Model 3 has a **low prior probability**. Structural studies of the POLE holoenzyme (Yuan et al., 2020; Roske & Yeeles, 2024; He et al., 2024) show that the POLE–POLE2 interaction interface is mediated primarily by the **C-terminal domain** of POLE (residues ~1,265–2,286), not the N-terminal region. The truncated 54-residue peptide would need to engage a binding surface for which there is no structural precedent. AlphaFold modeling of the N-terminal region predicts limited stable secondary structure in isolation. Additionally, even if the peptide were produced, its stoichiometric competition with full-length wild-type POLE protein would require comparable POLE2 binding affinity — unlikely for a 54-residue fragment vs. a 2,286-residue protein with extensive interface contacts. This model is retained for completeness and formal testability but is considered the least likely of the six candidates.

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

The patient's phenotype provides the strongest clinical support for this model among all six candidates:

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

## Model 6: Second-Site Somatic POLE Mutation

### Hypothesis

A somatic pathogenic missense mutation arises on the wild-type POLE allele in a tissue stem cell — specifically within the exonuclease domain (e.g., P286R, V411L, or another activating variant). This would convert the wild-type allele into a canonical dominant-negative, error-prone polymerase. Unlike Model 1 (LOH), the wild-type allele is not lost — instead, it acquires a gain-of-function mutation that produces an active but proofreading-deficient polymerase. This is distinct from LOH because the cell retains two POLE alleles: one truncated (c.138del, non-functional) and one somatically mutated (functional polymerase without proofreading).

### Relationship to Other Models

Model 6 is mechanistically distinct from Model 1 (LOH) and can co-occur with Model 4 (haploinsufficiency):
- **Model 1** eliminates the wild-type allele entirely — cells rely on compensatory polymerases (e.g., Polδ)
- **Model 6** retains the wild-type allele but corrupts its proofreading — the cell has an active, dominant-negative POLE
- **Model 4** may create the elevated baseline mutation rate that makes a second-site POLE mutation more likely (haploinsufficiency → more mutations per division → higher probability of hitting the exonuclease domain on the remaining allele)

### Falsifiable Predictions

| # | Prediction | Experiment | If TRUE | If FALSE |
|---|-----------|------------|---------|----------|
| 6a | Tumor WGS will show a somatic pathogenic missense in the POLE exonuclease domain on the wild-type allele | Paired tumor-normal WGS with phased variant calling | Strongly supports Model 6 | Weakens Model 6 |
| 6b | The somatic variant will be in trans with c.138del (on the wild-type allele) | Long-read sequencing or allele-specific analysis | Confirms compound heterozygosity in trans | If in cis: variant is on the already-truncated allele (irrelevant) |
| 6c | Mutational signatures will show SBS10a/b (canonical POLE proofreading failure) | SigProfiler decomposition | Consistent — dominant-negative POLE produces classical signatures | Non-POLE signatures: different mechanism |
| 6d | Different tumors may carry different second-site POLE mutations | Multi-region or multi-tumor WGS | Independent somatic events in different stem cells | Same mutation across tumors: early clonal event |

### Prior Probability Assessment

Model 6 has a **moderate prior probability**. Somatic POLE exonuclease domain mutations are well-documented in sporadic cancers (7–13% of endometrial cancers, ~3% of CRC per TCGA). The POLE exonuclease domain spans ~200 codons, and only a handful of hotspot positions (P286, V411, S459, etc.) produce the dominant-negative phenotype. In a patient with potentially elevated baseline mutation rates from haploinsufficiency (Model 4), the probability of hitting one of these hotspots somatically is higher than in the general population but still requires a specific gain-of-function event. Shah et al. (2024) documented co-occurring POLE exonuclease and non-exonuclease domain mutations and their impact on TMB, providing direct precedent for compound POLE mutation scenarios.

### Exclusion Criteria

Model 6 is **excluded** if: tumor WGS shows no somatic variants in the POLE exonuclease domain on the wild-type allele. Note: Model 6 can only be definitively tested for individual tumors — it may apply to some tumors but not others in the same patient.

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
| **M6 (Second-site)** | No predicted temporal order — somatic second-site mutation is stochastic; similar to M1 | **Partially inconsistent** — would predict random order, not turnover-correlated |

### Progressive Polyp Accumulation

The pattern of ~6 adenomas at age 19 with continued new polyp formation at every colonoscopic surveillance interval (ages 21, 24, 27, 29, ~31) indicates **ongoing mutagenesis** over >12 years. This progressive accumulation is:
- **Consistent with M4:** Constitutive haploinsufficiency produces a continuous elevated mutation rate in colonic stem cells, with new adenomas arising at each surveillance interval as additional stem cells accumulate sufficient driver mutations.
- **Consistent with M2:** If reinitiation produces a constitutive error-prone polymerase, mutation accumulation would also be continuous.
- **Less consistent with M1 as sole mechanism:** A single LOH event in one colonic stem cell would produce a clonal expansion, not geographically distributed new polyps at each interval. Multiple independent LOH events would be required — possible but requiring extraordinary coincidence.

---

## Clinical Phenotype as Model Discriminator

The patient's multi-system phenotype provides immediate discriminatory evidence even before experimental results.

| Finding | M1 (LOH) | M2 (Reinitiation) | M3 (Poisoning) | M4 (Haplo.) | M5 (Isoform) | M6 (Second-site) |
|---------|----------|-------------------|----------------|-------------|-------------|------------------|
| **Duplicated IVC (congenital)** | ❌ Cannot explain (LOH is somatic) | Neutral | Neutral | ✅ Supports (germline developmental effect) | Neutral | ❌ Cannot explain (somatic event) |
| **Stage IV+ endometriosis** | Neutral | Neutral | Neutral | ✅ Supports (high-turnover tissue threshold) | Possible (isoform-specific endometrial effect) | Neutral |
| **Bilateral PASH + liver FNH** | ❌ Unlikely (multi-organ, non-neoplastic) | Neutral | Neutral | ✅ Supports (systemic stromal/vascular proliferation) | Neutral | ❌ Unlikely (multi-organ) |
| **Thyroid carcinoma** | Possible (organ-specific LOH) | Possible | Neutral | ✅ Supports (high mitotic rate gland) | Possible | Possible (organ-specific second hit) |
| **GI polyposis** | Possible | Possible | Possible | ✅ Supports (high-turnover epithelium) | Possible | Possible |

**Summary:** The congenital duplicated IVC is the single most important clinical discriminator — it cannot be explained by any somatic mechanism (Models 1–3) and provides direct evidence for a germline-level effect (Model 4). The multi-system non-neoplastic findings (PASH, FNH, severe endometriosis) collectively argue against Model 1 operating alone, as LOH in each organ independently would be an extraordinary coincidence. The clinical phenotype most strongly supports Model 4, potentially in combination with Model 1 for tumor-specific ultra-hypermutation.

---

## Discriminatory Power Matrix

This matrix shows which experiments most efficiently discriminate between models.

| Experiment | M1 (LOH) | M2 (Reinitiation) | M3 (Poisoning) | M4 (Haplo.) | M5 (Isoform) | M6 (Second-site) | Priority |
|-----------|----------|-------------------|----------------|-------------|-------------|------------------|----------|
| **Tumor WGS + LOH** | ✅ Definitive | — | — | ✅ Rules out if LOH | — | ✅ Definitive (phased variant calling) | **Immediate** |
| **Mutational signatures** | ✅ Confirms POLE mechanism | ✅ Confirms POLE mechanism | — | — | — | ✅ Confirms POLE mechanism | **Immediate** |
| **Blood NanoSeq** | ✅ Normal = somatic | ✅ Elevated = germline | — | ✅ Elevated = threshold | — | ✅ Normal = somatic | **Immediate** |
| **Allele-specific RNA-seq** | — | ✅ Transcript present | ✅ NMD escape test | — | ✅ Isoform ratios | — | **Immediate** |
| **Endometriosis tissue NanoSeq** | — | — | — | ✅ Elevated = threshold in high-turnover tissue | — | — | **Medium-term** |
| **Ribo-seq** | — | ✅ Definitive | — | — | — | — | **Medium-term** |
| **Co-IP / structural modeling** | — | — | ✅ Definitive | — | — | — | **Medium-term** |
| **Replication timing analysis** | — | — | — | ✅ Enrichment pattern | — | — | **Medium-term** |
| **Isoform-specific RT-PCR** | — | — | — | — | ✅ Definitive | — | **Medium-term** |
| **Thyroid tumor signature analysis** (thyroidectomy specimen available) | ✅ If LOH at POLE | ✅ If SBS10a/b present | — | — | — | ✅ If somatic ExoD mutation | **Immediate** |
