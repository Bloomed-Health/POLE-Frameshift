# ClinVar Submission Preparation: POLE c.138del (p.Leu46Phefs*8)

> **Audit note, 2026-11-20.** No tumour or polyp from this patient has been sequenced. Wherever this file says the patient's lesions are hypermutated (">100 mut/Mb"), that is an assumption carried over from the PPAP literature, confirmed as such by the repository owner. It is not an observation. Polyp histology is also undocumented here. Read this file with the [verification audit](../../docs/VERIFICATION_AUDIT_2026-11-20.md).
>
> **This variant is already in ClinVar** (VCV000548779, conflicting classifications: Pathogenic from Labcorp Genetics/Invitae; Uncertain significance from Ambry Genetics and Counsyl). Passages below that call it novel or absent from ClinVar are superseded. Do not submit the template as written.

## Submission Status

| Database | Status | ID | Date |
|----------|--------|-----|------|
| **ClinVar** | Not yet submitted | ; | ; |
| **LOVD3** | Submitted (pending curation) | [Search link](https://databases.lovd.nl/shared/variants/POLE?search_position_c_start=138&search_position_c_start_intron=&search_position_c_end=138&search_position_c_end_intron=&search_vot_clean_dna_change=%3D%22c.138del%22&search_transcriptid=00001771) | 2026-04-15 |

## Purpose

This directory contains the materials needed for ClinVar submission of POLE c.138del (p.Leu46Phefs*8), documenting a frameshift variant in a patient with features overlapping PPAP. Laboratory classified as pathogenic; independent assessment supports VUS (PM2 + PP4 (superseded 2026-11-20: the variant is in gnomAD and the phenotype is not established as PPAP)).

As of April 2026, this variant is:
- **Confirmed as germline** ; heterozygous call from blood/saliva-derived DNA on accredited clinical germline assay with orthogonal confirmation
- **Already in ClinVar**: VCV000548779 (SCV000834648 Labcorp Genetics/Invitae, Pathogenic; SCV006397458 Ambry Genetics, Uncertain significance; SCV000785494 Counsyl, Uncertain significance). A submission from this project would be a fourth record
- **Present in gnomAD** (rs1555230420; 1 of 1,461,874 v4.1 exome alleles and 1 of 31,386 v2.1.1 genome alleles, both non-Finnish European; gnomAD API, 2026-11-20)
- **Submitted to LOVD3** (pending curation)
- **Not reported in any published PPAP cohort** with this specific cDNA change
- **Genomic coordinates:** GRCh38 chr12:132681203–132681204 (NC_000012.12:g.132681204del); GRCh37 chr12:133257789–133257790 (NC_000012.11:g.133257790del)

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
| ~~**PM2**~~ | ~~Absent from controls~~ | ~~Moderate~~ | **Not met as written.** The deletion is present in gnomAD (rs1555230420; 1 of 1,461,874 v4.1 exome alleles and 1 of 31,386 v2.1.1 genome alleles). Whether a rarity criterion applies at reduced strength depends on the disease model, which is unsettled |
| ~~**PP4**~~ | ~~Patient phenotype highly specific for the gene~~ | ~~Supporting~~ | **Not met as written (2026-11-20).** The evidence formerly listed here was a tumour mutational burden above 100 mut/Mb that was never measured, "adenomatous" polyposis whose histology is undocumented, and a papillary thyroid carcinoma that is outside the PPAP spectrum. What is documented: about 20 gastric and colonic polyps removed since age 19 (most advanced reported finding high-grade dysplasia) and a stage I papillary thyroid carcinoma. That is not a phenotype specific for POLE; see `docs/polyposis_differential.md` |

**Clinical laboratory classification: Pathogenic.** The Pathogenic classification rests on standard ACMG criteria for null variants in a gene with established loss-of-function disease mechanism, plus population database absence as assessed at the time (the variant is now seen in gnomAD) ; **not** on observed phenotype-genotype correlation in other patients. The laboratory explicitly notes this variant has not been previously reported in individuals with POLE-related conditions. The independent ACMG assessment formerly recorded here (PM2 + PP4 = VUS) is superseded: neither code is met as written (table above), and the public ClinVar record is conflicting (VCV000548779). Pathogenicity for a dominant polyposis phenotype remains a working hypothesis without functional, tumour or segregation data. PVS1 applicability is debated (see above). Mechanistic resolution (POLE mutational signatures, LOH analysis) would clarify which ACMG evidence codes apply.

## Important Caveats for ClinVar Submission

1. **Novel variant class for PPAP.** All previously reported pathogenic PPAP variants are missense mutations within the exonuclease domain (P286R, V411L, L424V, S459F). This is the first reported frameshift variant associated with a PPAP-consistent phenotype. The PPAP designation is a working hypothesis: the observed phenotype (progressive polyposis, reported ultra-hypermutation, multiple primaries) is clinically consistent with PPAP, but the mechanism by which a truncating variant produces this phenotype is under investigation — it is not a canonical exonuclease-domain driver. The Mur et al. (2023) gene-specific ACMG/AMP guidelines for POLE/POLD1 were designed for exonuclease domain missense variants and do not cover truncating variants upstream of the exonuclease domain.

2. **Mechanism under investigation.** Eight candidate mechanistic models are being evaluated (null hypothesis, LOH, translational reinitiation, NMD escape + holoenzyme poisoning, replication stress-dependent haploinsufficiency, isoform-specific effects, second-site somatic POLE mutation, annotation artifact). The phenotype is clinically consistent with PPAP (molecular confirmation via mutational signatures pending); the molecular mechanism by which a truncating variant produces a PPAP-consistent phenotype is the subject of active research. Note: "pathogenic" and "pathogenic via the PPAP mechanism" are distinct claims — the variant may be clinically relevant (e.g., as a carrier allele for a recessive POLE condition, or as an LOH modifier) without being a classical PPAP dominant-negative driver.

3. **47-gene panel negative.** No pathogenic or likely pathogenic variants in APC, MUTYH, MLH1/MSH2/MSH6/PMS2, POLD1, BRCA1/2, TP53, PTEN, or 38 other cancer predisposition genes ; isolating POLE c.138del as the sole identified genetic driver among genes tested. Note: panel does not cover GREM1 regulatory variants, connective tissue genes, or all structural variation.

## Submission Checklist

- [ ] Register as ClinVar submitter (if not already registered) at https://www.ncbi.nlm.nih.gov/clinvar/docs/submit/
- [ ] Obtain organization ID (OrgID) from ClinVar
- [ ] Review and customize `clinvar_submission_template.json` with OrgID
- [x] Variant coordinates verified against GRCh38 on 2026-11-20 (NC_000012.12:g.132681204del; VCF 12-132681203-GC-G; GRCh37 NC_000012.11:g.133257790del)
- [ ] Submit via ClinVar Submission API or web portal
- [ ] Record SCV accession number upon acceptance
- [ ] Update LOVD3 entry with ClinVar SCV cross-reference
- [ ] Update `POLE_clinvar_variants.tsv` with SCV accession

## Associated Disease

- **OMIM:** 615083 ; Colorectal cancer, susceptibility to, 12 (CRCS12; PPAP). The number given here before the audit belongs to CRCS10, the POLD1 entry
- **Orphanet:** ORPHA:447877 ; Polymerase proofreading-associated polyposis
- **MedGen:** C4015260

## References

- Mur P, Viana-Errasti J, et al. (2023) Gene-specific ACMG/AMP guidelines for POLE and POLD1. *Genome Medicine* 15:85. PMID: 37848928
- Palles C, et al. (2022) Polymerase proofreading-associated polyposis. *Best Practice & Research Clinical Gastroenterology* 58-59:101797
- Richards S, et al. (2015) Standards and guidelines for the interpretation of sequence variants. *Genetics in Medicine* 17:405-424. PMID: 25741868
