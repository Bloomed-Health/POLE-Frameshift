# Research plan after the audit

Written 2026-11-20 with the Fischbach & Walsh problem-selection framework (Cell 2024,
doi:10.1016/j.cell.2024.03.012). It replaces the experiment ranking that assumed a hypermutated tumour.

## Goals, as set by the repository owner

1. Understand what the variant does, and publish it in a form that survives peer review (these two should coincide).
2. Find the real cause of the patient's polyps.
3. Find other carriers.

## Reframing the problem

The former question was "how does a truncation that removes both catalytic domains cause the hypermutation of
PPAP?" It assumed three things that are not in evidence: that a tumour is hypermutated, that the phenotype is
PPAP, and that the variant is the cause. A project built on it needs several unlikely events in a row
(the framework's "multiple miracles" warning), and for two years the cheapest decisive test, sequencing one
lesion, was never done.

The questions that replace it need no miracle and pay off whichever way the data fall:

| Aim | Question | Why it is worth answering | Outcome if "yes" | Outcome if "no" |
|---|---|---|---|---|
| **A. Fate of the allele** | Does the c.138del transcript survive, and does translation restart at Met66? | Nobody has measured it; the sequence context is unusual; four near-identical alleles and thirty related ones exist | Start-proximal POLE truncations are hypomorphs, not nulls. Relevant to carrier counselling for the recessive syndromes | They are true nulls; the class is closed with data |
| **B. Somatic consequence** | Is the mutation rate or spectrum altered in this carrier's normal tissue or tumour? | Tests the dominant-disease idea directly; no measurement exists for any heterozygous POLE loss-of-function carrier that the audit could find | A new finding, and the first evidence for a dosage effect of POLE on fidelity | Direct evidence that one null allele is silent, which supports reclassification |
| **C. Cause of the polyps** | What explains them? | The patient's care depends on it | A diagnosis | A documented unexplained polyposis with the usual causes excluded |

Aim A can be finished in a laboratory within months, without patient tumour tissue. It is the lowest-risk route to goal 1.

## Assumptions and their risk

Risk: 1 = near certain to hold, 5 = likely to fail.

| Assumption | Risk | Evidence | Cheapest test |
|---|---|---|---|
| The variant call is real and heterozygous | 1 | Accredited laboratory, signed report (owner statement) | `panel_bam_checks.py variant` |
| The HGVS name is right | 1 | Re-derived three ways | done |
| The mutant transcript is measurable in blood RNA | 2 | POLE is expressed in dividing cells; resting blood may give low signal | Pilot RT-PCR; fall back to stimulated lymphocytes or fibroblasts |
| Translation restarts at Met66 | 3 | Geometry fits published reporter data; untested for POLE | Reporter assay |
| A POLE lacking residues 1-65 is stable and functional | 4 | Residues 1-30 are annotated as disordered; nothing more is known | Degron-rescue experiment (needs a collaborator with that cell line) |
| The thyroid tumour is hypermutated | 5 | No evidence; contradicted by what is known of loss-of-function carriers | Exome of the stored block |
| The polyps are caused by POLE | 5 | See `polyposis_differential.md` | Polyp sequencing |
| Other carriers can be reached | 3 | Three laboratories have reported the variant; none publishes contact routes | Registry enrolment; laboratory inquiry |

## Experiments, ranked by information per unit cost

### 1. Paper and files (now, no cost)

- Collect every pathology report; fill `data/templates/lesion_table_template.tsv`.
- Read the methods and limitations section of the 47-gene report: transcript, reference build, copy-number coverage of APC promoter 1B and the GREM1 region.
- Run `analysis/panel_bam_checks/` on the BAM.
- Update the LOVD entry (`data/lovd_update_2026-11-20.md`).

### 2. Reporter assay for re-initiation (Aim A; weeks)

Construct: the POLE 5′ leader and the first 240 nt of the coding sequence, fused in the POLE reading frame to a
reporter that has no start codon of its own.

| Construct | Purpose |
|---|---|
| Wild type | Reference signal from the annotated start |
| c.138del | Any signal comes from a restart downstream of the stop |
| c.138del with the Met66 codon changed to a non-start codon | Shows whether that signal depends on Met66 |
| c.137del, c.141del | Do the neighbours behave the same? |
| c.1A>T | The IMAGe allele: restart or leaky scanning to Met44 |
| Wild type with the Met44 codon changed | How much normal translation starts at Met44 |

Read out reporter activity against a co-transfected control, and reporter mRNA by RT-qPCR so that changes in
RNA level are not mistaken for changes in translation. A reporter without introns is not subject to
exon-junction-dependent decay, so this assay isolates translation; decay is measured in experiment 3.

Go / no-go: if the c.138del construct gives a signal that disappears when Met66 is changed, re-initiation is real
and experiment 5 becomes worthwhile. If it gives background only, the allele is a null at the level of
translation and Aim A is answered.

### 3. Allele-specific RNA from the patient (Aim A; weeks)

One blood draw: a tube for DNA, an RNA-stabilising tube, and cells for short-term culture. Amplify across
exons 1 to 3 from cDNA and count mutant and wild-type reads; use the same amplicon on genomic DNA as the
50:50 reference, because a 1-bp deletion can bias amplification. Repeat on cultured cells with and without an
NMD inhibitor. A skin biopsy gives fibroblasts for the same measurement in a dividing cell type and for experiment 5.

Readout: mutant fraction near 50% means the transcript escapes decay; a low fraction that rises with the
inhibitor means it is degraded.

### 4. The stored thyroid tumour (Aims B and C; weeks to months)

Tumour block with blood as the matched normal: exome sequencing for mutation count, signature fit, loss of the
wild-type POLE allele, and drivers; β-catenin immunostain on a section. Formalin-fixed tissue adds artefacts,
so the analysis should use a pipeline that filters them. This yields the first measured mutation count in the
patient. Papillary thyroid carcinomas ordinarily carry few mutations (not re-verified in the audit), so a
raised count would be conspicuous.

### 5. Protein and replication in patient cells (Aims A and B; months)

In fibroblasts: POLE protein level against controls, with one antibody whose epitope lies within residues 1-65
and one beyond them. A null allele predicts about half the control level with both. A Met66 product predicts
about half with the first and more with the second. Logan et al. 2018 measured POLE1 in fibroblasts with an
antibody raised against residues 1-176, which would detect both forms and cannot separate them by size
(2,221 versus 2,286 residues). S-phase progression can be compared with their published method.

### 6. Somatic mutation rate in normal tissue (Aim B; months)

Duplex sequencing of blood now, and of normal colonic lining at the next endoscopy, against age-matched
reference values. Carriers of exonuclease-domain variants show raised burdens in normal tissue
(Robinson et al. 2021, doi:10.1038/s41588-021-00930-y). A null allele predicts a normal burden.

### 7. Germline genome (Aim C)

The existing data are a 47-gene panel. A genome adds structural and deep-intronic APC variants and the genes
the panel lacks (MBD4, MLH3, RNF43 among them).

### 8. Family (Aims B and C)

Parents cannot be tested. Test siblings for c.138del and record their colonoscopy history.

### 9. Next endoscopy (Aim C; more than a year away)

Prepare the protocol in advance: two or more polyps and normal lining, fresh-frozen, with blood on the same
day; consent and ethics approval in place. This is the decisive test for mosaic APC and for any polymerase signature.

## Decision points

| Result | Meaning | Next |
|---|---|---|
| Reporter shows Met66-dependent restart and patient RNA near 50% mutant | The allele is a hypomorph | Experiment 5; write up Aim A with the neighbours as a class |
| Reporter negative and patient RNA low | The allele is a null | Write up Aim A as a negative result; Aim B still stands |
| Thyroid tumour with an ordinary mutation count and no polymerase signature | The hypermutation premise is refuted in the one tumour available | Remove the premise from the repository; Aim C continues |
| Thyroid tumour hypermutated with a polymerase signature | Unexpected and important | Confirm in a second lab; look for a second POLE hit; sequence polyps at the earliest opportunity |
| Polyps share an APC variant | Mosaic APC; the POLE variant is incidental to the polyps | Report as a cautionary case |

## What can be published

- **Aim A alone:** a short functional paper on translation re-initiation and decay for start-proximal POLE truncations, with c.138del, c.137del, c.141del and c.1A>T.
- **Aims B and C:** a case report with tumour sequencing that separates coincidence from causation in a carrier of a POLE truncation classified Pathogenic. It is informative either way.
- **Not publishable as it stands:** a claim that the variant causes PPAP, that it is absent from databases, or that a tumour is hypermutated.

Before any of it: written consent for publication, and ethics approval for research use of samples. The owner did not state what is in place.

## Finding other carriers

- Enrol the patient in ClinGen's patient registry, which shares variant-level data with ClinVar and matches participants (check current enrolment terms; not verified in the audit).
- Ask the reporting laboratory whether it runs a contact or matching programme for people with the same variant.
- Submit the phenotype, corrected, to LOVD (done once the entry is updated) and consider Matchmaker Exchange through a clinical or research partner.
- Widen the search to the class: any carrier of a truncation in POLE exons 1-2 is informative.

## Where single-cell methods fit

Nothing in this repository is single-cell data, and none was analysed in the audit. If single-cell RNA
sequencing is ever run on this patient's cells, note that the variant lies 165 nt from the 5′ end of the mRNA:
only 5′ or full-length chemistries read it; 3′ chemistries do not.

## Data hygiene

BAM, CRAM, FASTQ, VCF files and reports are excluded by `.gitignore` and must stay out of this public repository.
