# Clinical Case Summary: POLE c.138del (p.Leu46Phefs*8)

---

## Variant Details

| Field | Value |
|-------|-------|
| **Gene** | *POLE* (DNA Polymerase Epsilon, catalytic subunit) |
| **Genomic location** | Chromosome 12q24.33 |
| **Transcript** | ENST00000320574 (NM_006231) |
| **cDNA change** | c.138del |
| **Protein change** | p.Leu46Phefs\*8 |
| **Variant type** | Frameshift deletion |
| **Predicted consequence** | Premature termination at ~residue 54 of 2,286 amino acids |
| **gnomAD frequency** | Absent (0/1,614,586 alleles in gnomAD v4) |
| **ClinVar** | Not reported |
| **ACMG classification** | Pathogenic (PVS1, PM2, PP4) |

---

## Patient Phenotype

The presentation spans four distinct categories — neoplastic, proliferative/stromal, endometrial/hormonal, and congenital developmental — suggesting that POLE dysfunction in this variant is truly systemic, affecting tissue biology at a level deeper than tumor mutation accumulation alone.

### 1. Neoplastic Findings (Classical PPAP Spectrum)

| Finding | Details | PPAP Relevance |
|---------|---------|----------------|
| **Gastrointestinal polyposis** | ~15 sessile adenomatous polyps distributed across stomach, cecum, and sigmoid colon | Consistent with attenuated polyposis in PPAP (Palles et al. 2022: most patients present with 10–100 polyps; gastric involvement characteristic of POLE heterozygotes) |
| **Rectal mucosal changes** | Erythematous, edematous, friable mucosa | Suggests diffuse inflammatory/proliferative process beyond discrete polyps |
| **Chronic gastric gastritis** | Diffuse gastric inflammation | Part of broader GI field effect |
| **Stage II papillary thyroid carcinoma** | Cystic variant with squamous metaplasia | **Not part of established PPAP tumor spectrum.** If confirmed to carry POLE signatures (SBS10a/b) or LOH at POLE locus, would expand the recognized PPAP tumor spectrum. Squamous metaplasia may reflect aberrant differentiation from genomic instability |

> **Note on thyroid cancer:** Classical PPAP-associated malignancies are colorectal, endometrial, duodenal, and (less frequently) brain tumors. Thyroid cancer has not been systematically reported in PPAP carriers. Determining whether this tumor carries POLE mutational signatures is a high-priority analysis.

### 2. Proliferative and Stromal Findings

| Finding | Details | Significance |
|---------|---------|-------------|
| **Bilateral breast changes** | Left: fibroadenomatous change with dense stromal fibrosis. Right: columnar cell change, cystic/papillary apocrine metaplasia, stromal fibrosis, focal pseudoangiomatous stromal hyperplasia (PASH) | Pattern across both breasts suggests a **field effect** rather than focal lesion. PASH is a benign vascular-stromal proliferation associated with hormonal influences and, in some contexts, genomic instability |
| **Liver FNH and/or hemangioma** | Benign vascular proliferative lesion(s) | FNH arises from hyperplastic response to vascular malformation. Combined with PASH and duplicated IVC, reveals a pattern of **vascular and stromal proliferative abnormalities across multiple organ systems** |

### 3. Endometrial/Hormonal Findings

| Finding | Details | Significance |
|---------|---------|-------------|
| **Stage IV+ deep infiltrating endometriosis** | Extension into thoracic diaphragm; adhesion lesions on intestines | Extraordinarily severe; diaphragmatic and intestinal involvement represents the most advanced form, is rare, and indicates an extremely aggressive endometrial tissue phenotype |
| **Diffuse asymmetric adenomyosis** | Endometrial tissue invading the myometrium | Combined with endometriosis, indicates systemic endometrial tissue dysregulation |

> **Research significance:** The endometrium is one of the tissues most vulnerable to POLE proofreading deficiency (endometrial cancer is a major PPAP-associated malignancy; somatic POLE mutations found in 7–12% of sporadic endometrial cancers). The endometrium is a rapidly cycling tissue with high cell turnover — exactly where haploinsufficiency under replicative stress (Model 4) would be most consequential. Severe endometriosis + adenomyosis without formal malignant transformation suggests POLE dysfunction may alter endometrial biology at a **pre-malignant level** — increasing mutation rates or altering proliferative signaling, driving aggressive invasive behavior without classical carcinogenesis. **Novel research question:** Does POLE haploinsufficiency contribute to endometriosis severity? This has never been investigated and could have implications beyond this patient, given that endometriosis affects ~10% of reproductive-age women.

### 4. Congenital Developmental Finding

| Finding | Details | Significance |
|---------|---------|-------------|
| **Duplicated inferior vena cava** | Congenital vascular anomaly present from embryonic development | **Cannot be explained by somatic mutations or tumor-related processes** — reflects a developmental error during embryogenesis |

> **Mechanistic implications:** This is the most conceptually important finding for the mechanistic paradox. POLE is required for DNA replication in every dividing cell during embryonic development. Robinson et al. (2021) demonstrated that germline POLE mutations affect mutation rates during early embryogenesis. A congenital vascular anomaly in a POLE frameshift carrier raises the possibility that **POLE haploinsufficiency affects developmental morphogenesis** — either through elevated mutation rates in embryonic progenitor cells creating somatic mosaicism that disrupts vascular patterning, or through non-replicative roles of POLE in developmental signaling or chromatin regulation. This finding **argues against the pure LOH model (Model 1) as the sole explanation** — LOH is a stochastic somatic event and should not cause a congenital anomaly. If the duplicated IVC is genuinely related to POLE dysfunction, it supports Model 4 (haploinsufficiency has developmental consequences).

### Genomic Profile

| Feature | Result |
|---------|--------|
| **Tumor mutational burden** | >100 mutations/Mb (ultra-hypermutated) |
| **Microsatellite status** | To be characterized |
| **MMR IHC** | To be characterized |
| **Mutational signatures** | Pending WGS analysis (SBS10a/b/28 status critical) |
| **LOH at POLE locus** | Pending allele-specific analysis |
| **Thyroid tumor POLE signatures** | Pending — would expand PPAP tumor spectrum if positive |

---

## POLE Domain Architecture and Variant Position

```
POLE Catalytic Subunit (p261) — 2,286 amino acids

|===|                    |=============|              |=======================|                              |
 1-54                    268----------471             580-------------------1260                           2286
  ↑                      Exonuclease                  Polymerase
  STOP                   (Proofreading)               (DNA Synthesis)
  p.Leu46Phefs*8         Domain                       Domain

  ■ Truncated peptide    ■ Classical PPAP variants     ■ Polymerase activity
    (no catalytic           (P286R, V411L, L424V,
    function)               S459F)
```

The variant terminates the protein at residue 54, which is:

- **214 residues upstream** of the exonuclease domain start (residue 268)
- **526 residues upstream** of the polymerase domain start (residue 580)
- Eliminates **100%** of all known functional domains

---

## The Mechanistic Paradox

### Why this variant challenges current models

All previously reported pathogenic PPAP variants are **missense substitutions** within the exonuclease active site (P286R, V411L, L424V, S459F). Their mechanism is dominant-negative: the polymerase retains DNA synthesis capability but loses proofreading, producing an error-blind replicase that outcompetes mismatch repair.

**p.Leu46Phefs\*8** eliminates the entire protein — both polymerase and proofreading domains. Under orthodox models:

1. The wild-type allele should compensate (haploinsufficiency alone should not produce TMB >100 mut/Mb)
2. Complete POLE loss is embryonic lethal in mice
3. Yet the patient presents with unambiguous PPAP

### Five candidate mechanistic models

1. **Somatic LOH** — Wild-type allele lost in tumor; cells rely on lower-fidelity polymerases (Knudson two-hit model)
2. **Translational reinitiation** — Ribosomes reinitiate at downstream AUG, producing polymerase-only protein lacking proofreading
3. **NMD escape + holoenzyme poisoning** — Truncated 54-residue peptide competes for POLE2 binding, disrupting holoenzyme assembly
4. **Replication stress-dependent haploinsufficiency** — 50% POLE is rate-limiting in rapidly dividing tissues
5. **Isoform-specific effects** — Variant differentially affects tissue-specific transcript isoforms

---

## Comparison with Known PPAP Variants

| Variant | Type | Domain | Mechanism | TMB |
|---------|------|--------|-----------|-----|
| P286R | Missense | Exonuclease | Dominant-negative (proofreading loss, polymerase gain) | >100 mut/Mb |
| V411L | Missense | Exonuclease | Dominant-negative | >100 mut/Mb |
| L424V | Missense | Exonuclease | Dominant-negative | High |
| S459F | Missense | Exonuclease | Dominant-negative | High |
| **c.138del** | **Frameshift** | **N-terminal (pre-domain)** | **Unknown — paradoxical** | **>100 mut/Mb** |

---

## Key Discriminating Experiments

| Priority | Experiment | What it tests | Expected if LOH model | Expected if reinitiation model |
|----------|-----------|---------------|----------------------|-------------------------------|
| **1** | Tumor-normal WGS + LOH analysis | Wild-type allele status in tumor | LOH at 12q24.33 | No LOH |
| **2** | Mutational signature decomposition | Source of ultra-hypermutation | SBS10a/b/28 present | SBS10a/b/28 present |
| **3** | Allele-specific RNA-seq (blood) | NMD escape status | N/A (LOH is somatic) | Mutant transcript detectable |
| **4** | NanoSeq on normal blood cells | Germline mutation rate | Normal (LOH is somatic event) | Elevated SBS10a/b |
| **5** | Ribo-seq on patient cells | Translational reinitiation | No downstream ribosome footprints | Ribosome footprints at downstream AUG |

---

## Clinical Relevance

### Therapeutic implications

- **Immunotherapy eligibility:** TMB >100 mut/Mb far exceeds the FDA tissue-agnostic threshold (≥10 mut/Mb) for pembrolizumab
- **Published POLE ICI data:** 82.4% clinical benefit rate, 15.1 month PFS, 29.5 month OS in pathogenic POLE carriers (Garmezy et al., JCO Precision Oncology 2022)
- **Mutational signature threshold:** POLE signature ≥78.5% predicts ICI response (Pietrantonio et al., Annals of Oncology 2024)

### Implications for variant classification

The definitive gene-specific ACMG/AMP classification guidelines for POLE/POLD1 (Mur, Viana-Errasti et al., *Genome Medicine* 2023, Valle lab at IDIBELL) were designed for non-disruptive (missense) variants within the exonuclease domain. The c.138del variant — a truncating variant upstream of the exonuclease domain — falls entirely outside that framework's scope. If the mechanistic paradox is resolved, the classification guidelines would need to be extended to accommodate truncating variants acting through LOH, reinitiation, or haploinsufficiency mechanisms.

If the two-hit / LOH model is confirmed, truncating POLE variants currently classified as VUS may need reclassification as pathogenic cancer predisposition alleles. Notably, Valle et al. (2020) identified 6 loss-of-function POLE variants in a cohort of 2,813 hereditary cancer probands — these represent a critical comparator set for understanding whether truncating variants outside the exonuclease domain can produce PPAP phenotypes.

---

*This clinical summary is intended for research purposes and does not constitute medical advice.*
