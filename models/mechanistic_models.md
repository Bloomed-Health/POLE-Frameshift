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

### Exclusion Criteria

Model 1 is **excluded** if: tumor shows no LOH at POLE locus AND no promoter methylation AND wild-type allele is expressed at normal levels in tumor tissue.

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

### Exclusion Criteria

Model 4 is **excluded** if: normal tissue mutation rates are completely normal AND/OR tumor shows LOH at the POLE locus (indicating a two-hit rather than dosage mechanism).

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

## Discriminatory Power Matrix

This matrix shows which experiments most efficiently discriminate between models.

| Experiment | M1 (LOH) | M2 (Reinitiation) | M3 (Poisoning) | M4 (Haplo.) | M5 (Isoform) | Priority |
|-----------|----------|-------------------|----------------|-------------|-------------|----------|
| **Tumor WGS + LOH** | ✅ Definitive | — | — | ✅ Rules out if LOH | — | **Immediate** |
| **Mutational signatures** | ✅ Confirms POLE mechanism | ✅ Confirms POLE mechanism | — | — | — | **Immediate** |
| **Blood NanoSeq** | ✅ Normal = somatic | ✅ Elevated = germline | — | ✅ Elevated = threshold | — | **Immediate** |
| **Allele-specific RNA-seq** | — | ✅ Transcript present | ✅ NMD escape test | — | ✅ Isoform ratios | **Immediate** |
| **Ribo-seq** | — | ✅ Definitive | — | — | — | **Medium-term** |
| **Co-IP / structural modeling** | — | — | ✅ Definitive | — | — | **Medium-term** |
| **Replication timing analysis** | — | — | — | ✅ Enrichment pattern | — | **Medium-term** |
| **Isoform-specific RT-PCR** | — | — | — | — | ✅ Definitive | **Medium-term** |
