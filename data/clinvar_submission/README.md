# ClinVar Submission Preparation: POLE c.138del (p.Leu46Phefs*8)

## Submission Status

| Database | Status | ID | Date |
|----------|--------|-----|------|
| **ClinVar** | Not yet submitted | — | — |
| **LOVD3** | Submitted (pending curation) | [Search link](https://databases.lovd.nl/shared/variants/POLE?search_position_c_start=138&search_position_c_start_intron=&search_position_c_end=138&search_position_c_end_intron=&search_vot_clean_dna_change=%3D%22c.138del%22&search_transcriptid=00001771) | 2026-04-15 |

## Purpose

This directory contains the materials needed for ClinVar submission of POLE c.138del (p.Leu46Phefs*8) as a **pathogenic** variant associated with Polymerase Proofreading-Associated Polyposis (PPAP).

As of April 2026, this variant is:
- **Absent from ClinVar** — no SCV accession exists
- **Absent from gnomAD v4** (0/1,614,586 alleles)
- **Submitted to LOVD3** (pending curation)
- **Not reported in any published PPAP cohort** with this specific cDNA change

Submitting to ClinVar will make this variant discoverable by other clinical labs encountering POLE truncating variants in patients with polyposis or unexplained ultra-hypermutated tumors.

## Files

| File | Description |
|------|-------------|
| `clinvar_submission_template.json` | ClinVar API submission JSON (Submission API v2 format) |
| `README.md` | This file |

## ACMG/AMP Classification Evidence

| Criterion | Code | Strength | Evidence |
|-----------|------|----------|----------|
| **PVS1** | Null variant in a gene where LoF is a known mechanism of disease | Very Strong | Frameshift at codon 46 of 2,286 — eliminates all major catalytic domains (exonuclease, polymerase). POLE LoF intolerance: pLI = 0.98, LOEUF = 0.22. Heterozygous POLE exonuclease domain variants cause PPAP (OMIM 612591). |
| **PM2** | Absent from controls | Moderate | Not found in gnomAD v4 (0/1,614,586 alleles), ExAC, or any population database |
| **PP4** | Patient phenotype highly specific for the gene | Supporting | Ultra-hypermutated tumor (TMB >100 mut/Mb), progressive adenomatous polyposis (~6 adenomas age 19, accumulating to ~15+ by age 31), Stage I papillary thyroid microcarcinoma (encapsulated, non-invasive, 0.6 cm) — phenotype consistent with PPAP |

**Combined classification: Pathogenic** (PVS1 + PM2 + PP4)

## Important Caveats for ClinVar Submission

1. **Novel variant class for PPAP.** All previously reported pathogenic PPAP variants are missense mutations within the exonuclease domain (P286R, V411L, L424V, S459F). This is the first reported frameshift variant producing a PPAP phenotype. The Mur et al. (2023) gene-specific ACMG/AMP guidelines for POLE/POLD1 were designed for exonuclease domain missense variants and do not cover truncating variants upstream of the exonuclease domain.

2. **Mechanism under investigation.** Six candidate mechanistic models are being evaluated (LOH, translational reinitiation, NMD escape + holoenzyme poisoning, replication stress-dependent haploinsufficiency, isoform-specific effects, second-site somatic POLE mutation). The phenotype is unambiguous; the molecular mechanism by which a truncating variant produces a dominant PPAP phenotype is the subject of active research.

3. **47-gene panel negative.** No pathogenic or likely pathogenic variants in APC, MUTYH, MLH1/MSH2/MSH6/PMS2, POLD1, BRCA1/2, TP53, PTEN, or 38 other cancer predisposition genes — isolating POLE c.138del as the sole genetic driver.

## Submission Checklist

- [ ] Register as ClinVar submitter (if not already registered) at https://www.ncbi.nlm.nih.gov/clinvar/docs/submit/
- [ ] Obtain organization ID (OrgID) from ClinVar
- [ ] Review and customize `clinvar_submission_template.json` with OrgID
- [ ] Verify variant coordinates against GRCh38 reference
- [ ] Submit via ClinVar Submission API or web portal
- [ ] Record SCV accession number upon acceptance
- [ ] Update LOVD3 entry with ClinVar SCV cross-reference
- [ ] Update `POLE_clinvar_variants.tsv` with SCV accession

## Associated Disease

- **OMIM:** 612591 — Colorectal cancer, susceptibility to, 12 (PPAP)
- **Orphanet:** ORPHA:447877 — Polymerase proofreading-associated polyposis
- **MedGen:** C4015260

## References

- Mur P, Viana-Errasti J, et al. (2023) Gene-specific ACMG/AMP guidelines for POLE and POLD1. *Genome Medicine* 15:85. PMID: 37848928
- Palles C, et al. (2022) Polymerase proofreading-associated polyposis. *Best Practice & Research Clinical Gastroenterology* 58-59:101797
- Richards S, et al. (2015) Standards and guidelines for the interpretation of sequence variants. *Genetics in Medicine* 17:405-424. PMID: 25741868
