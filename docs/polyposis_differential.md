# The polyps: a new POLE c.138del finding, or an independent cause?

Written 2026-11-20. Sources are in [`data/claims_ledger.tsv`](../data/claims_ledger.tsv) (rows E01-E18, P01-P09).
The author is not a clinician. Everything under "Questions for the care team" is a question, not advice.

## Answer

On present evidence an independent cause is the more likely explanation, and a link to POLE cannot be claimed.
It cannot be excluded either. The question is testable, and both outcomes would be publishable.

Three things stand between this case and a "new finding":

1. **The phenotype is not yet defined.** About 20 polyps were removed and examined, mostly from the colon, with
   high-grade dysplasia in at least one (owner statement). No pathology report is on file, so it is not known
   which were adenomas, serrated lesions, hyperplastic, hamartomatous or fundic gland polyps. Each type points
   to different genes.
2. **No lesion has been sequenced.** The mutation count and mutational signatures that would show a polymerase
   fault have never been measured in this patient.
3. **The allele cannot do what PPAP alleles do.** PPAP is caused by an enzyme that copies DNA and fails to
   proofread. c.138del yields no protein, a 52-residue peptide, or (if translation restarts at Met66) an enzyme
   with its proofreading domain intact. See the audit, section 3.

## Reasoning, step by step

**Step 1. What do carriers of POLE loss-of-function alleles look like in published data?**
According to PubMed, Mur et al. 2020 ([doi](https://doi.org/10.1038/s41436-020-0922-2)) found such variants in
0.22% of 2,309 hereditary cancer patients and 0.20% of 59,095 controls; breast tumours from carriers of a POLE
frameshift held 1.09 to 1.70 mutations per megabase with no POLE signature. Logan et al. 2018
([doi](https://doi.org/10.1016/j.ajhg.2018.10.024)) found loss-of-function alleles in the unaffected parents of
children with recessive POLE deficiency. The one case report that attributed polyposis to a POLE truncation
(Yamaguchi et al. 2019, [doi](https://doi.org/10.1038/s10038-019-0611-7)) was contested in the same journal
([doi](https://doi.org/10.1038/s10038-019-0701-6)).

**Step 2. How much room do those numbers leave?** *(inference)*
The odds ratio from Mur's counts is 1.08 with a 95% interval of 0.44 to 2.63. For a carrier who has the disease,
the chance that the variant is responsible is (RR − 1)/RR: about 7% at the point estimate and at most about 62%
at the upper bound. The cohort was hereditary cancer in general, not polyposis alone, so this is a guide.

**Step 3. How often would the two simply coincide?** *(inference)*
If about 1 person in 1,000 carries a POLE loss-of-function allele (an assumption; Mur's control figure of 0.20%
covers POLE and POLD1 together), then among patients with unexplained polyposis:

| True relative risk | Share of patients expected to carry such an allele | Expected carriers among 541 patients (the size of Terlouw 2026) |
|---|---|---|
| 1 (no effect) | 0.10% | 0.5 |
| 2 | 0.20% | 1.1 |
| 5 | 0.50% | 2.7 |
| 10 | 0.99% | 5.4 |
| 50 | 4.8% | 26 |

A single carrier with polyposis is what chance predicts in a few hundred polyposis patients. Published cohorts
of this size do not report an excess of POLE loss-of-function carriers, which argues against a large effect and
cannot rule out a small one.

**Step 4. What usually explains polyposis when a blood panel is negative?**
Much of it stays unexplained. Where a cause is found, the commonest is a mosaic APC variant: 14.3% of patients
within guideline criteria and at least 10% of those with 20 or more adenomas before age 60 (Terlouw et al. 2026,
[doi](https://doi.org/10.1053/j.gastro.2025.10.028)); 19% in a second series (Sommer et al. 2026,
[doi](https://doi.org/10.1053/j.gastro.2025.10.011)). Blood testing misses most of these: in Spier et al. 2016
([doi](https://doi.org/10.1136/jmedgenet-2015-103468)) three of five mosaic variants were at 0.1 to 1% or
undetectable in blood. A quarter of mosaic patients who had an upper endoscopy also had gastroduodenal polyps,
which matches this patient's distribution. Genome sequencing adds structural APC variants that panels miss
(Karstensen et al. 2024, [doi](https://doi.org/10.1038/s41431-024-01585-z)).

**Step 5. Does the rest of the history point to a syndrome?**

- *Papillary thyroid carcinoma in a young woman with polyps.* The cribriform-morular type is tied to APC: it
  occurs almost only in women, at a median age of 24, and precedes the bowel findings in about half of cases
  (Lam & Saremi 2017, [doi](https://doi.org/10.1530/ERC-17-0014)). This tumour was reported as cystic and
  encapsulated with squamous metaplasia, and no β-catenin stain or BRAF test was done. The block is retrievable.
- *PTEN hamartoma tumour syndrome.* Polyps of mixed type are found in 93% of carriers who have an endoscopy
  (Heald et al. 2010, [doi](https://doi.org/10.1053/j.gastro.2010.06.061)). PTEN was negative on the panel and
  none of the usual physical signs was noted. Benign breast disease does not count towards the diagnosis
  (Pilarski et al. 2013, [doi](https://doi.org/10.1093/jnci/djt277)).
- *Benign breast, liver and skin lesions.* Each is common on its own. Together they do not match a defined
  syndrome that the panel covers.

**Step 6. What does each explanation predict in tissue?**

| Explanation | Polyp mutation count | Signatures | Shared variant across polyps | Blood |
|---|---|---|---|---|
| POLE proofreading fault (not expected from this allele) | raised | SBS10a/b, SBS28, as in the POLD1 family of Buchanan et al. 2025 ([doi](https://doi.org/10.1007/s10689-025-00506-3)) | none required | germline variant only |
| Mosaic APC | ordinary | ageing-type | the same APC variant in two or more polyps | low fraction or absent |
| Biallelic base-excision repair defect (MUTYH, NTHL1, MBD4) | raised | gene-specific | none required | two germline variants; MBD4 is not on the panel |
| Colibactin-associated | ordinary | colibactin-type | recurrent APC splice change | absent |
| No single cause | ordinary | ageing-type | none | nothing |

Only the first row would make POLE the cause. It is also the row this allele is least able to produce.

## Where the 47-gene panel stops

The panel covered APC, MUTYH, NTHL1, MSH3, POLD1, POLE, PTEN, SMAD4, BMPR1A, STK11, GREM1, AXIN2 and the
mismatch-repair genes, among others (ledger row L02). It did not test MBD4, MLH3 or RNF43. A blood panel does
not detect mosaic variants confined to the bowel, and it usually does not report deep-intronic variants.
Whether its copy-number analysis reaches APC promoter 1B (Rohlin et al. 2011,
[doi](https://doi.org/10.1038/onc.2011.201)) and the duplication upstream of GREM1 (Jaeger et al. 2012,
[doi](https://doi.org/10.1038/ng.2263)) is stated in the methods section of the report and should be read there.

## What would make it a finding

Any one of these would change the assessment; the first is the strongest:

1. a polyp or tumour from this patient with a raised mutation count and a polymerase-type signature;
2. a second, unrelated carrier of c.138del or a neighbouring truncation (c.137del, c.137dup, c.141del) with a similar history;
3. RNA or protein evidence that the allele makes an abnormal product;
4. a raised somatic mutation rate in this patient's normal tissue.

And these would close it: a shared APC variant across polyps, or an ordinary mutation count and signature
profile in the thyroid tumour and in polyps.

## What can be done with what is available

Constraints (owner statements): polyp blocks sit in several institutions, some abroad; the next endoscopy is
more than a year away; the thyroid and breast blocks can be retrieved; blood and a skin biopsy can be obtained;
siblings can be tested; a research laboratory is available.

| Order | Step | What it settles |
|---|---|---|
| 1 | Request every pathology report and fill `data/templates/lesion_table_template.tsv` | Which syndrome class the polyps belong to. Reports travel more easily than tissue |
| 2 | Run `analysis/panel_bam_checks/` on the panel BAM | Confirms the variant in reads; shows whether the two recessive POLE alleles were covered; scans APC in blood for a mosaic variant at the depth the panel reached |
| 3 | Thyroid tumour block with blood as the normal: exome sequencing, plus a β-catenin stain | The first measured mutation count in this patient; signatures; whether the second POLE allele is lost; whether the tumour is the APC-linked type |
| 4 | Blood RNA and a reporter assay (see `research_plan_2026-11.md`) | What the allele makes |
| 5 | Test siblings for c.138del and ask for their colonoscopy history | Whether the variant and the polyps travel together in the family |
| 6 | A germline genome | Structural and deep-intronic APC variants; genes outside the panel |
| 7 | At the next endoscopy: fresh polyp, normal lining and blood on the same day | The decisive test for mosaic APC and for any polymerase signature |

## Questions for the care team

- With about 20 polyps and high-grade dysplasia, what surveillance interval does the phenotype itself call for, whatever the POLE result means?
- If the reports show adenomas, does the patient meet the threshold at which testing polyps for APC mosaicism is advised?
- Can a β-catenin stain and BRAF testing be added to the thyroid tumour block?
- Any treatment plan that assumes a hypermutated tumour rests on a number that has not been measured. Can it wait for a sequenced specimen?
- The Pathogenic result does carry one firm implication: the patient is a carrier of a recessive POLE-deficiency allele. Is partner testing for POLE relevant to family planning?
