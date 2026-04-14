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

### Cancer Presentation

- **Ultra-hypermutated tumor** with TMB >100 mutations/Mb
- **Polyposis** consistent with PPAP spectrum
- **Multi-system phenotype** involving cancer-predisposed tissues

### Genomic Profile

| Feature | Result |
|---------|--------|
| **Tumor mutational burden** | >100 mutations/Mb (ultra-hypermutated) |
| **Microsatellite status** | To be characterized |
| **MMR IHC** | To be characterized |
| **Mutational signatures** | Pending WGS analysis (SBS10a/b/28 status critical) |
| **LOH at POLE locus** | Pending allele-specific analysis |

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

If the two-hit / LOH model is confirmed, truncating POLE variants currently classified as VUS may need reclassification as pathogenic cancer predisposition alleles. This would expand the population recognized as carrying cancer risk from POLE mutations.

---

*This clinical summary is intended for research purposes and does not constitute medical advice.*
