# ClinVar Submission Preparation: POLE c.138del (p.Leu46Phefs*8)

## Submission Status

| Database | Status | ID | Date |
|----------|--------|-----|------|
| **ClinVar** | Not yet submitted | ; | ; |
| **LOVD3** | Submitted (pending curation) | [Search link](https://databases.lovd.nl/shared/variants/POLE?search_position_c_start=138&search_position_c_start_intron=&search_position_c_end=138&search_position_c_end_intron=&search_vot_clean_dna_change=%3D%22c.138del%22&search_transcriptid=00001771) | 2026-04-15 |

## Purpose

This directory contains the materials needed for ClinVar submission of POLE c.138del (p.Leu46Phefs*8), documenting a frameshift variant in a patient with features overlapping PPAP. Laboratory classified as pathogenic; independent assessment supports VUS (PM2 + PP4).

As of April 2026, this variant is:
- **Confirmed as germline** ; heterozygous call from blood/saliva-derived DNA on accredited clinical germline assay with orthogonal confirmation
- **Absent from ClinVar** ; no SCV accession exists
- **Absent from gnomAD v4.1.0** (0/1,614,586 alleles; accessed April 2026)
- **Submitted to LOVD3** (pending curation)
- **Not reported in any published PPAP cohort** with this specific cDNA change
- **Genomic coordinates:** GRCh38 chr12:132681203–132681204 (repository default); GRCh37 chr12:133249847 (clinical report coordinate system)

Submitting to ClinVar will make this variant discoverable by other clinical labs encountering POLE truncating variants in patients with polyposis or unexplained ultra-hypermutated tumors.

## Files

| File | Description |
|------|-------------|
| `clinvar_submission_template.json` | ClinVar API submission JSON (Submission API v2 format) |
| `README.md` | This file |

## Classification Status

**This variant cannot be classified under existing POLE-specific guidelines.** The Mur et al. (2023) gene-specific ACMG/AMP framework for POLE/POLD1 was designed for non-disruptive (missense/in-frame) variants within the exonuclease domain. The c.138del variant ; a truncating variant upstream of all functional domains ; falls entirely outside that framework's scope.

Under the **general ACMG/AMP framework**, the following evidence codes apply:

| Criterion | Code | Strength | Evidence |
|-----------|------|----------|----------|
| ~~**PVS1**~~ | ~~Null variant in a gene where LoF is a known mechanism of disease~~ | ~~Very Strong~~ | **Not applied.** POLE c.138del is a null variant, but POLE is not LoF-intolerant (gnomAD pLI ≈ 0, LOEUF = 0.76; 188 LoF variants observed vs. 279 expected ; heterozygous LoF is tolerated). The mechanism by which this variant produces the PPAP phenotype does not match the canonical dominant-negative model. PPAP pathogenicity has only been established for missense variants that produce an error-prone polymerase ; a gain-of-function mechanism incompatible with PVS1. Applying PVS1 would contradict the Mur et al. (2023) framework. The presence of 188 LoF variants in gnomAD without apparent PPAP suggests a second somatic hit (LOH) or other non-canonical mechanism is required. |
| **PM2** | Absent from controls | Moderate | Not found in gnomAD v4.1.0 (0/1,614,586 alleles, accessed April 2026), ExAC, or any population database |
| **PP4** | Patient phenotype highly specific for the gene | Supporting | Reported TMB >100 mut/Mb (assay platform pending clarification), progressive adenomatous polyposis (~6 adenomas age 19, accumulating to ~15+ by age 31), Stage I papillary thyroid carcinoma (1.2 cm, isthmus) ; phenotype clinically consistent with PPAP. **Limitation:** PP4 is Supporting-level evidence and does not include functional data; the phenotype-genotype link would be strengthened by confirming POLE mutational signatures (SBS10a/b) or LOH at the POLE locus in the tumor |

**Clinical laboratory classification: Pathogenic.** The Pathogenic classification rests on standard ACMG criteria for null variants in a gene with established loss-of-function disease mechanism, plus population database absence ; **not** on observed phenotype-genotype correlation in other patients. The laboratory explicitly notes this variant has not been previously reported in individuals with POLE-related conditions. Independent ACMG evidence assessment: PM2 + PP4 supports VUS under strict point counting; pathogenicity is a working hypothesis pending functional or segregation data. The clinical pathogenicity call and the mechanistic novelty answer different questions, and both can be true simultaneously ; this strengthens rather than weakens the research case. PVS1 applicability is debated (see above). Mechanistic resolution (POLE mutational signatures, LOH analysis) would clarify which ACMG evidence codes fully apply and strengthen the evidence base for this novel variant class.

## Important Caveats for ClinVar Submission

1. **Novel variant class for PPAP.** All previously reported pathogenic PPAP variants are missense mutations within the exonuclease domain (P286R, V411L, L424V, S459F). This is the first reported frameshift variant producing a PPAP phenotype. The Mur et al. (2023) gene-specific ACMG/AMP guidelines for POLE/POLD1 were designed for exonuclease domain missense variants and do not cover truncating variants upstream of the exonuclease domain.

2. **Mechanism under investigation.** Seven candidate mechanistic models are being evaluated (null hypothesis, LOH, translational reinitiation, NMD escape + holoenzyme poisoning, replication stress-dependent haploinsufficiency, isoform-specific effects, second-site somatic POLE mutation). The phenotype is clinically consistent with PPAP (molecular confirmation via mutational signatures pending); the molecular mechanism by which a truncating variant produces a dominant PPAP phenotype is the subject of active research.

3. **47-gene panel negative.** No pathogenic or likely pathogenic variants in APC, MUTYH, MLH1/MSH2/MSH6/PMS2, POLD1, BRCA1/2, TP53, PTEN, or 38 other cancer predisposition genes ; isolating POLE c.138del as the sole identified genetic driver among genes tested. Note: panel does not cover GREM1 regulatory variants, connective tissue genes, or all structural variation.

## Submission Checklist

- [ ] Register as ClinVar submitter (if not already registered) at https://www.ncbi.nlm.nih.gov/clinvar/docs/submit/
- [ ] Obtain organization ID (OrgID) from ClinVar
- [ ] Review and customize `clinvar_submission_template.json` with OrgID
- [ ] Verify variant coordinates against GRCh38 reference (GRCh38 chr12:132681203–132681204; clinical report uses GRCh37 chr12:133249847 ; verify liftover)
- [ ] Submit via ClinVar Submission API or web portal
- [ ] Record SCV accession number upon acceptance
- [ ] Update LOVD3 entry with ClinVar SCV cross-reference
- [ ] Update `POLE_clinvar_variants.tsv` with SCV accession

## Associated Disease

- **OMIM:** 612591 ; Colorectal cancer, susceptibility to, 12 (PPAP)
- **Orphanet:** ORPHA:447877 ; Polymerase proofreading-associated polyposis
- **MedGen:** C4015260

## References

- Mur P, Viana-Errasti J, et al. (2023) Gene-specific ACMG/AMP guidelines for POLE and POLD1. *Genome Medicine* 15:85. PMID: 37848928
- Palles C, et al. (2022) Polymerase proofreading-associated polyposis. *Best Practice & Research Clinical Gastroenterology* 58-59:101797
- Richards S, et al. (2015) Standards and guidelines for the interpretation of sequence variants. *Genetics in Medicine* 17:405-424. PMID: 25741868
