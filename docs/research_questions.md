# Research questions for POLE c.138del and the early POLE truncations

Written 2026-11-21 from full-text readings of eight papers and a re-review of this repository at commit 59a82b3; file and line references are to that commit. Each question states why it matters, the smallest step that would answer it, the result that would change this repository's conclusions, and the paper page or repository line that raised it. *Inference* marks reasoning that is not a statement of a paper; *not stated* means absent from the full text; *outside the paper* marks material from PubMed, PubMed Central or the web, and statements from a PubMed record open with According to PubMed and carry the DOI link; *not verified* marks something nobody checked. Facts about the carrier are owner statements as recorded in `data/claims_ledger.tsv`. Nothing here is medical advice: wherever a question touches diagnosis, screening or treatment it reports evidence and is addressed to the carrier's care team.

| Tag | Paper | DOI | Page numbers refer to |
|---|---|---|---|
| K | Kozak 1986, *Cell* 44:283-292 | [10.1016/0092-8674(86)90762-2](https://doi.org/10.1016/0092-8674(86)90762-2) | journal pages |
| C | Coclet et al. 1989, *Clin Endocrinol* 31:655-665 | [10.1111/j.1365-2265.1989.tb01290.x](https://doi.org/10.1111/j.1365-2265.1989.tb01290.x) | journal pages |
| P | Pilarski et al. 2013, *J Natl Cancer Inst* | [10.1093/jnci/djt277](https://doi.org/10.1093/jnci/djt277) | Page N of 10, Advance Access PDF |
| VP | Vande Perre et al. 2019, *Fam Cancer* | [10.1007/s10689-018-0102-6](https://doi.org/10.1007/s10689-018-0102-6) | PDF pages 1-6, online-first version |
| Y | Yamaguchi et al. 2019, *J Hum Genet* | [10.1038/s10038-019-0611-7](https://doi.org/10.1038/s10038-019-0611-7) | PDF pages 1-12 |
| M | Mur, Palles, Tomlinson and Valle, reply, *J Hum Genet* | [10.1038/s10038-019-0701-6](https://doi.org/10.1038/s10038-019-0701-6) | PDF pages 1-2 |
| W | Weber et al. 2024, *Lancet* 403:632-44 | [10.1016/S0140-6736(23)02268-7](https://doi.org/10.1016/S0140-6736(23)02268-7) | journal pages |
| Rev | Joo, Viana-Errasti, Buchanan and Valle 2025, *Fam Cancer* 24:38 | [10.1007/s10689-025-00460-0](https://doi.org/10.1007/s10689-025-00460-0) | Page N of 14 |

## The most decisive questions, in order

| Rank | Question | Cost | Why it is decisive |
|---|---|---|---|
| 1 | RQ3.1 What is each polyp, histologically? | Paperwork | Decides which literature applies (adenomatous, hamartomatous or serrated) and feeds three sets of criteria; every statement about the polyps waits on it |
| 2 | RQ6.1 What does the laboratory report say it tested? | Paperwork | Turns nine owner statements into documents and defines what a negative result excluded for APC, PTEN and copy number |
| 3 | RQ2.1 Are the stored lesions mismatch-repair proficient? | Stains on existing blocks | The first tumour-level datum of any kind, and a precondition for reading any later mutation count |
| 4 | RQ3.6 Is the thyroid tumour the APC-linked type? | A stain and one test on the stored block | One result could tie polyps and thyroid tumour to a cause other than POLE |
| 5 | RQ1.1 How much c.138del transcript survives? | One blood draw | Converts ledger V12 from inference to measurement and decides whether the restart questions are live |
| 6 | RQ2.2 What does an exome of the thyroid tumour show, against rules fixed in advance? | One exome | The first measured burden, spectrum and second-hit status; a direct test of the hypermutation premise |
| 7 | RQ3.2 Do two archived polyps share an APC variant? | Targeted sequencing of stored blocks | The review's own test for mosaic APC; a positive result explains the polyps without POLE |
| 8 | RQ1.2 Does translation restart at Met66, and by which route? | A reporter assay over weeks | Decides null against hypomorph for the ten alleles whose next start codon is Met66 |
| 9 | RQ4.1 Does the carrier meet the PTEN criteria once examined? | Three clinical observations | Opens or closes a second, independent explanation |
| 10 | RQ5.1 Do the variant and the polyps travel together in the siblings? | Sibling testing | The only segregation evidence that can be had |

Two look-ups take minutes and remove open contradictions: RQ1.7 (a splice prediction) and the first step of RQ5.2 (one ClinVar record).

## 1. Fate of the allele and translation restart

**RQ1.1 What fraction of POLE transcripts in the carrier's blood carries c.138del?**

*Why it matters.* Whether the transcript is degraded separates a null allele from one that could restart translation; ledger V12 is an inference and calls decay borderline. The only published measurement for a germline POLE truncation found the mutant in 41.9% of leukocyte transcript reads against 50.4% of DNA reads, with decay assumed and no inhibitor control (Y p. 5).

*Smallest step.* One blood draw; deep amplicon sequencing across exons 1-3 on cDNA, with the same amplicon on genomic DNA as the 50:50 reference; a repeat in cultured cells with and without a decay inhibitor (`docs/research_plan_2026-11.md:76-84`).

*Would change the conclusions.* A mutant fraction near 50% means the transcript escapes decay and the restart questions become live. A low fraction that rises with the inhibitor means a null allele at the RNA level and closes the hypomorph idea with data.

*Raised by.* `data/claims_ledger.tsv:13`; Y p. 5.

**RQ1.2 Does translation restart at Met66, and after which upstream ORF?**

*Why it matters.* Ledger V11 is an inference. The one restart experiment in Kozak 1986 used a minicistron of five codons with a 10-nt gap (K p. 287; Fig. 7, K p. 289). The c.138del mRNA presents five ORFs ahead of Met66, of 52, 34, 28, 27 and 9 codons (ledger V10), and later work ties restart to ORF length (RQ1.3).

*Smallest step.* The planned reporter set (`docs/research_plan_2026-11.md:54-74`), with two additions: a c.138del construct in which the Met44 codon is changed, which separates restart after the 9-codon ORF from restart after the longer ones (*inference*), and an engineered earlier stop as a length control. The allele c.76del does not serve as that control, because it runs into the same stop codon (`docs/pole_variant_comparison.md:37`).

*Would change the conclusions.* A signal that disappears when Met66 is changed makes the allele a candidate hypomorph, to be written up with its neighbours as a class; background alone makes it a null at the level of translation (`docs/research_plan_2026-11.md:126-127`).

*Raised by.* `data/claims_ledger.tsv:11-12`; K p. 283, 287, 289.

**RQ1.3 Which published evidence governs restart after a stop 52 codons into an ORF?**

*Why it matters.* Ledger rows V11 and E09 rest on the abstract of a study of p53 reporters that saw re-initiation after stops up to 126 codons from the start ([doi:10.1093/nar/gkz319](https://doi.org/10.1093/nar/gkz319)). The upstream-ORF literature points the other way. *Outside the paper*: Kozak's 2002 review, read through PubMed Central, describes restart as often seen after 10-12 codons and substantially reduced from 13 to 33 ([doi:10.1016/S0378-1119(02)01056-9](https://doi.org/10.1016/S0378-1119(02)01056-9)), and According to PubMed, Luukkonen et al. found inhibition proportional to upstream-ORF length ([doi:10.1128/JVI.69.7.4086-4094.1995](https://doi.org/10.1128/JVI.69.7.4086-4094.1995)). Neither body of work has been read in full for the ledger.

*Smallest step.* Read the p53 study, Kozak 2001 ([doi:10.1093/nar/29.24.5226](https://doi.org/10.1093/nar/29.24.5226)) and Kozak 2002 in full; tabulate ORF length, stop-to-ATG gap and experimental system for every positive and negative construct.

*Would change the conclusions.* If the positive cases in the p53 work share a feature that c.138del lacks, the ledger's statement that the geometry lies inside a published range has to be narrowed. If they include ORFs of about 50 codons, the doubt raised by the upstream-ORF work is answered.

*Raised by.* `data/claims_ledger.tsv:12`, `:55`; K p. 289.

**RQ1.4 Does the annotated POLE start behave like Kozak's construct B145?**

*Why it matters.* Its context, TCCATGT (ledger V09), is the exact sequence of mutants B145 and B147, measured at least four-fold above the all-pyrimidine floor with no value printed (K p. 285; Fig. 5, K p. 287). The repository labels it `weak`, the bucket of constructs that scored below 0.2. How leaky the start is sets how many ribosomes ever reach the downstream ATGs. The leader is short (27 nt, `analysis/variant_verification/verify_c138del.py:44`) and the coding region behind it is 91.7% GC over c.11-c.46, and both could shift the balance. *Outside the paper*: According to PubMed (PMID 1820208; the notes give no DOI), shortening the cap-to-ATG distance from 32 to 3 nt moved initiation progressively to the second ATG.

*Smallest step.* On the wild-type reporter with its native leader, vary only the 5′ UTR bases at −3 to −1 (native TCC, then ACC, GCC and TTT). Position +4 cannot be changed silently, because c.4 lies in codon 2 (*inference*, computed from the fixture).

*Would change the conclusions.* A native start close to the constructs with A at −3 makes leaky scanning a minor route and products from Met44 or Met66 unlikely in normal cells. A start near the floor makes downstream initiation more important than the repository assumes.

*Raised by.* `data/claims_ledger.tsv:10`; `models/mechanistic_models.md:97`; K p. 285, 287.

**RQ1.5 Is Met44 used in normal cells, or is it shielded by the out-of-frame ATG at c.68?**

*Why it matters.* The repository asks whether Met44 is a natural second start (`docs/pole_variant_comparison.md:78`). The ATG at c.68 is out of frame and has A at −3 and G at +4; an upstream out-of-frame ATG with A at −3 cut downstream initiation ten-fold (K p. 287; Fig. 6, K p. 288). Its ORF ends 28 nt past the Met44 ATG, so ribosomes that start there cannot restart at Met44 (*inference* from K p. 283).

*Smallest step.* First, at no cost, look for footprints or N-termini at Met44 and Met66 in public data. *Outside the paper*: According to PubMed, GTI-seq maps initiation sites in human cells at single-nucleotide resolution ([doi:10.1073/pnas.1207846109](https://doi.org/10.1073/pnas.1207846109)), GWIPS-viz carries aggregated human ribosome-profiling tracks ([doi:10.1093/nar/gkt1035](https://doi.org/10.1093/nar/gkt1035)), and a proteome survey identified more than 1,700 alternative protein N-termini ([doi:10.1074/mcp.M113.036442](https://doi.org/10.1074/mcp.M113.036442)). Then, in the reporter, remove each out-of-frame ATG synonymously (c.48T>C, c.66T>C, c.69T>C, each of which keeps Asp), singly and together, against a control in which Met44 is ablated.

*Would change the conclusions.* Evidence of initiation at Met44 or Met66 on wild-type POLE would make start-proximal truncations less likely to be nulls. Its absence in several cell types would answer the repository's question in the negative.

*Raised by.* `docs/pole_variant_comparison.md:78`; K p. 283, 287-289.

**RQ1.6 Would a POLE lacking residues 1-65 be stable and active, and could it meet the review's definition of a PPAP variant?**

*Why it matters.* Stability of such a product is the plan's riskiest assumption about the allele (`docs/research_plan_2026-11.md:40`). The review defines an actionable variant as one that impairs exonuclease activity and leaves replication intact (Rev p. 5). A product starting at Met66 keeps the whole exonuclease domain, so the expected answer is that it does not qualify (*inference*).

*Smallest step.* A fibroblast immunoblot with one epitope inside residues 1-65 and one beyond them (`docs/research_plan_2026-11.md:94-100`); if a shorter product exists, exonuclease and polymerase assays.

*Would change the conclusions.* A stable product with impaired proofreading would reopen a dominant mechanism, against expectation. A stable, normal product makes the allele a hypomorph relevant to recessive disease only. No product makes it a null.

*Raised by.* `docs/research_plan_2026-11.md:24`, `:40`; Rev p. 5.

**RQ1.7 Has a splice predictor been run on c.138del, and what did it return?**

*Why it matters.* `README.md:61` reports all-zero SpliceAI scores, and ledger V13 says no predictor was run (`data/claims_ledger.tsv:14`). The two cannot both stand.

*Smallest step.* Rerun the Ensembl VEP query in `tests/live/test_external_sources.py:73-80` and restore the ledger row; the RT-PCR of RQ1.1 settles the matter experimentally.

*Would change the conclusions.* A non-zero score would reopen the splice branch of the closed Model 7. Zeros remove a contradiction between the README and the ledger.

*Raised by.* `README.md:61`; `data/claims_ledger.tsv:14`.

**RQ1.8 Is there any other route around the stop?**

*Why it matters.* Model 5, on isoform-specific effects, is listed as untested (`README.md:59`). The repository also says that a polymerase-only product has no sequence basis (`docs/clinical_case_summary.md:328`), yet `data/POLE_all_methionines.tsv` lists in-frame M487 and M506 between the exonuclease domain and the polymerase core. What is missing is a mechanism to reach them, about 1.3 kb and more than ten in-frame ATGs past the stop (an assessment made in the re-review).

*Smallest step.* One transcript-table look-up (Ensembl or GENCODE) with isoform expression, and a check of N-terminal proteomics for products that begin at residue 487 or 506.

*Would change the conclusions.* An expressed isoform that skips the deletion, or any sign that M487 or M506 is used, would revive ideas the audit retired. Their absence lets Model 5 close and lets the statement rest on mechanism.

*Raised by.* `README.md:59`; `docs/clinical_case_summary.md:328`.

## 2. Tumour and tissue evidence

**RQ2.1 Are the stored lesions microsatellite stable, with all four mismatch-repair proteins retained?**

*Why it matters.* The repository describes these tests as pending although none is ordered (`FAQ.md:62`; ledger P02). The N363K family had exactly this first-line tumour data (VP p. 2), and Yamaguchi's carrier had a cancer made hypermutated by MLH1 methylation (Y p. 5-9).

*Smallest step.* A question for the care team and the pathology laboratory: can microsatellite testing and immunostains for MLH1, PMS2, MSH2 and MSH6 (the last was omitted by Yamaguchi, Y p. 3) be run on the stored thyroid block and on any polyp block that can be retrieved?

*Would change the conclusions.* Mismatch-repair loss in a lesion means that a high mutation count there cannot be credited to POLE. Retained proteins give the baseline that every later sequencing result needs. An isolated loss of one protein, as in one N363K polyp (VP p. 2), would need careful reading.

*Raised by.* `data/claims_ledger.tsv:39`; VP p. 2; Y p. 3, 5.

**RQ2.2 What mutation count, spectrum and signatures does the thyroid tumour show, judged by rules fixed in advance?**

*Why it matters.* Burden and signatures have never been measured (ledger P01, P02). The reply supplies the tests: a burden frequently above 100 per megabase, an excess of C:G to A:T changes, signature 10 or 14, and mismatch-repair deficiency excluded as the source (M p. 1).

*Smallest step.* An exome of the block against blood (`docs/research_plan_2026-11.md:88-92`), reporting raw counts, callable megabases, the six-class spectrum and a signature fit that includes indel signatures, with the pass-or-fail rules committed to the repository before the data arrive.

*Would change the conclusions.* An ordinary count with no polymerase signature refutes the hypermutation premise in the one tumour available (`docs/research_plan_2026-11.md:128`). A raised count with SBS10a or SBS10b would be unexpected and leads to RQ2.3 and RQ2.4.

*Raised by.* `data/claims_ledger.tsv:38-39`; M p. 1.

**RQ2.3 Does any lesion carry a second hit at POLE, including copy-neutral loss of heterozygosity?**

*Why it matters.* Models 1 and 6 predict one. Yamaguchi found no single-nucleotide or copy-number change at POLE in two cancers and did not address copy-neutral loss (Y p. 5); ledger E19 records the one published tumour with a somatic exonuclease-domain mutation over a germline frameshift.

*Smallest step.* From the data of RQ2.2: somatic POLE and POLD1 calls, copy number and allelic imbalance at 12q24.33, and the fraction of c.138del reads in tumour DNA.

*Would change the conclusions.* Loss of the wild-type allele in a viable tumour would contradict the audit's argument that a null allele plus such loss leaves no Pol ε (`docs/VERIFICATION_AUDIT_2026-11-20.md:94-96`), or would show that the allele is not null. A somatic exonuclease-domain variant would be the configuration of Model 6.

*Raised by.* Y p. 5; `data/claims_ledger.tsv:32`.

**RQ2.4 If a lesion is hypermutated, is the cause mismatch-repair loss, or a somatic or mosaic exonuclease-domain variant, and not c.138del?**

*Why it matters.* The first item of the repository's list of what would make the case a finding (`docs/polyposis_differential.md:103`) could credit the wrong variant. The review expects mosaicism in polyposis genes other than APC (Rev p. 4).

*Smallest step.* On the same lesion, and before any signature claim: microsatellite status, immunostains, MLH1 promoter methylation and BRAF. In every lesion: exonuclease-domain POLE and POLD1 calls, tested for sharing between lesions and for presence in normal tissue.

*Would change the conclusions.* It decides attribution; without it a positive result cannot be interpreted.

*Raised by.* Y p. 5-9; M p. 1; Rev p. 4.

**RQ2.5 Is the somatic mutation rate raised in the carrier's normal tissue?**

*Why it matters.* This is the direct test of a dosage effect on fidelity. The plan says no measurement was found for any heterozygous loss-of-function carrier (`docs/research_plan_2026-11.md:25`).

*Smallest step.* Duplex sequencing of blood against age-matched reference values (`docs/research_plan_2026-11.md:102-106`).

*Would change the conclusions.* A raised rate would be the first evidence that POLE dosage affects fidelity. A normal rate is direct evidence that one null allele is silent.

*Raised by.* `docs/research_plan_2026-11.md:25`.

**RQ2.6 Does the thyroid tumour count for or against Model 4, and is adult turnover the right exposure?**

*Why it matters.* By Coclet 1989 adult thyroid cells divide about five times, with a turnover time of 8.5 to 14.4 years, and the one adolescent measured turned over in about 167 days (C p. 655, 661-663). The repository still scores the thyroid as a high-mitotic-rate gland in support of the model (`models/mechanistic_models.md:169`, `:338`) and compares tissues on mixed metrics (`models/mechanistic_models.md:287`).

*Smallest step.* Remove the high-mitotic-rate statements; label each row of `data/tissue_replication_rates.tsv` by metric and re-base the comparison on cumulative divisions up to the age at diagnosis; treat RQ2.2 as the falsification test. A further question for the pathology laboratory is a Ki-67 stain on non-tumour tissue of the thyroidectomy block, since nodular hyperplasia is reported (`docs/clinical_case_summary.md:37`) and nodules labelled far above normal tissue (C p. 662). *Outside the paper*: According to PubMed, an autopsy series gives a Ki-67 index of 0.08 ± 0.04% at 20-60 years ([doi:10.1210/jc.2006-0417](https://doi.org/10.1210/jc.2006-0417)).

*Would change the conclusions.* Few replication-type mutations in a tumour of a slowly dividing tissue fit a cause unrelated to replication fidelity. The rank correlation itself does not move with any thyroid value from the paper (rho 0.821, exact p 0.067), so it cannot be rescued this way.

*Raised by.* C p. 655, 661-663; `models/mechanistic_models.md:169`, `:338`.

**RQ2.7 How will mutation rates be computed so that they compare across papers?**

*Why it matters.* Yamaguchi's 81.5 and 2.8 per 10⁶ bases imply a denominator near 6,000 Mb that the paper does not state (*inference*; Y p. 5), and the papers use different signature catalogues (Y p. 7; M p. 1).

*Smallest step.* Fix the definition in `analysis/mutational_signatures/README.md`: the variant types counted, the callable territory and the catalogue version.

*Would change the conclusions.* It prevents a threshold being met or missed by arithmetic.

*Raised by.* Y p. 5, 7.

**RQ2.8 What do the published tumours of POLE truncation carriers show at source?**

*Why it matters.* The statement that Yamaguchi's unstable tumour lacks the POLE signature rests on the reply's reading of a supplementary figure (M p. 1); whether the somatic mutation of ledger E19 lay in cis or in trans is unknown; and an earlier frameshift carrier is cited without tumour data (Y p. 10).

*Smallest step.* Download the twelve supplementary files listed on the article page of Y; read in full the three papers behind ledger E19, ledger E02 and the earlier carrier.

*Would change the conclusions.* It confirms or corrects the signature claim at source and yields a second-hit table (none in Yamaguchi; none in the E02 cohort according to a web fetch, *not verified* in the full text; a somatic exonuclease-domain mutation in E19) against which Models 1 and 6 can be scored.

*Raised by.* Y p. 5, 7, 10; M p. 1; `data/claims_ledger.tsv:32`.

## 3. Cause of the polyps

**RQ3.1 What is the histology, site, size and dysplasia grade of each of the roughly 20 polyps?**

*Why it matters.* Histology is undocumented (ledger P03), yet several files call the polyps adenomatous (`README.md:35`). The review covers adenomatous polyposis only (Rev p. 2); the PTEN criteria count hamartomas and ganglioneuromas and exclude hyperplastic polyps (P p. 7); flat or sessile lesions raise the serrated question, for which Yamaguchi's group screened RNF43 (Y p. 4-5).

*Smallest step.* Request every pathology report and fill `data/templates/lesion_table_template.tsv`, after adding the histology classes it lacks.

*Would change the conclusions.* Adenomas bring the review's differential into play (RQ3.2 to RQ3.5). Three or more hamartomas or ganglioneuromas meet a major PTEN criterion (RQ4.1). Serrated lesions point to the serrated polyposis criteria (ledger E17, unverified) and to RNF43, which the panel lacks. The reports also settle whether there were about 15 polyps or about 20.

*Raised by.* `data/claims_ledger.tsv:40`; Rev p. 2, 6; P p. 3, 7.

**RQ3.2 Do two archived polyps share an APC variant, and is it present in other tissues?**

*Why it matters.* Mosaic APC is the repository's leading alternative (`docs/polyposis_differential.md:56-62`). The review's standard is at least two independent lesions, a threshold of 5% or less in blood data, and digital PCR across tissues (Rev p. 4). Ledger P08 records polyp blocks at several institutions, so the test need not wait for the next endoscopy (*inference*).

*Smallest step.* APC sequencing of two or more stored blocks; for a shared variant, digital PCR in blood, in normal mucosa and in the non-tumour tissue of the thyroid and breast blocks.

*Would change the conclusions.* A shared APC variant means mosaic APC, with the POLE variant incidental to the polyps (`docs/research_plan_2026-11.md:130`). One guard applies: a shared APC c.835-8A>G has to be checked in normal tissue first, because that change can recur independently in colibactin-exposed tissue (*inference* from Rev p. 4, 8).

*Raised by.* Rev p. 4; `data/claims_ledger.tsv:45`.

**RQ3.3 Do the polyps carry the signature of any named alternative cause?**

*Why it matters.* The review ties about 30% of unexplained adenomatous polyposis to at least one tumour with APC c.835-8A>G, and gives SBS88 and ID18 for colibactin, SBS18 with SBS36 for MUTYH, SBS30 for NTHL1, SBS1 or SBS96 for MBD4 (SBS96 as named in the review's reference 114; COSMIC gives that name to a different signature, so the reference set has to be chosen to match), ID2 and ID7 for mismatch-repair deficiency, and tetranucleotide instability for MSH3 (Fig. 1, Rev p. 2; Rev p. 7-8). The repository names none of these (`docs/polyposis_differential.md:84-85`).

*Smallest step.* Targeted APC sequencing that covers c.835-8 on archived polyps; a signature fit that includes these signatures on any polyp that is sequenced.

*Would change the conclusions.* A positive result documents a cause that a negative blood panel cannot exclude, second alleles the panel missed included.

*Raised by.* Rev p. 2, 7-8.

**RQ3.4 Does the germline carry an APC variant that the panel could not report?**

*Why it matters.* `docs/clinical_case_summary.md:252` lists APC as excluded. The review names deep-intronic variants, point variants at the YY1 site of promoter 1B, a 5′UTR variant and structural variants as beyond standard panels, with MLPA finding large changes in about 24% of patients in one small study (Rev p. 3-5).

*Smallest step.* Read the report's methods for promoter, 5′UTR, intronic and copy-number coverage (RQ6.1); analyse APC transcripts in the blood RNA drawn for RQ1.1; a germline genome, long-read if short-read is negative; MLPA.

*Would change the conclusions.* A finding is a diagnosis. Without one, the statement about APC can list exactly what was tested.

*Raised by.* `docs/clinical_case_summary.md:252`; Rev p. 3-5.

**RQ3.5 Does the carrier have a germline variant in MBD4, MLH3 or RNF43?**

*Why it matters.* None of the three is on the panel (ledger L02). MLH3 tumours show no microsatellite instability and no known signature, so tissue cannot exclude that gene (Rev p. 7; *inference*). One carrier of a single MBD4 variant had about 30 adenomas with a somatic second hit (Rev p. 6).

*Smallest step.* A germline genome or a wider panel.

*Would change the conclusions.* A diagnosis, or a documented exclusion in place of an untested gap.

*Raised by.* `data/claims_ledger.tsv:36`; Rev p. 6, 7.

**RQ3.6 Is the thyroid carcinoma the APC-linked cribriform-morular type, and does it share an APC variant with the polyps?**

*Why it matters.* That type is listed among the cancers of familial adenomatous polyposis (Rev p. 2). Thyroid is not listed under PPAP (Rev p. 3) and is absent among the 33 tabulated members of the N363K families (VP p. 3-4). No ancillary test has been done (ledger P06).

*Smallest step.* A question for the care team, already posed at `docs/polyposis_differential.md:131`: can a β-catenin stain and BRAF testing be added to the block? Then APC sequencing of the block beside the polyps.

*Would change the conclusions.* One APC variant in the polyps and in the thyroid tumour would close the case for an independent cause.

*Raised by.* Rev p. 2, 3; VP p. 3-4; `data/claims_ledger.tsv:43`.

**RQ3.7 How is unexplained adenomatous polyposis divided among mosaic APC, colibactin, non-coding APC variants and no finding?**

*Why it matters.* The repository ranks mosaic APC as the commonest cause, with 14.3%, at least 10% and 19% (`docs/polyposis_differential.md:56-58`; ledger E13, E15). The review gives up to one-third unexplained, 10-25% of de novo APC cases mosaic, about 30% with the colibactin hotspot, and no ranking (Rev p. 4, 8, 9). *Outside the paper*: According to PubMed, the abstract of another 2025 review puts mosaicism at up to 50% of unexplained cases ([doi:10.1007/s10689-025-00464-w](https://doi.org/10.1007/s10689-025-00464-w)).

*Smallest step.* Read the review's references 130 and 131 and the 2026 cohort papers in full; tabulate each figure with its denominator.

*Would change the conclusions.* It replaces a ranking with numbers and may reorder the differential.

*Raised by.* `docs/polyposis_differential.md:56-58`; Rev p. 4, 8, 9.

**RQ3.8 Which guidance sets the threshold for testing polyps for APC mosaicism?**

*Why it matters.* The repository asks the care team whether the patient meets that threshold (`docs/polyposis_differential.md:130`). The review gives no threshold, algorithm or surveillance schedule (*not stated*) and points to two guidance papers the repository lacks, its references 1 and 12.

*Smallest step.* Read both (as printed in the review's reference list: doi 10.1016/S2468-1253(23)00240-6 and doi 10.1093/bjs/znae070); bring the question to the care team.

*Would change the conclusions.* It supplies the missing threshold, or shows that none exists.

*Raised by.* `docs/polyposis_differential.md:130`; Rev references 1 and 12.

## 4. This carrier's phenotype

**RQ4.1 Once examined, does the carrier meet the revised clinical criteria for PTEN hamartoma tumour syndrome?**

*Why it matters.* On documented features the carrier has no major criterion and one minor criterion (papillary thyroid carcinoma); three major criteria have never been assessed, and a negative PTEN test does not settle a clinical diagnosis (P p. 2, 7). `docs/clinical_case_summary.md:259` lists the syndrome as excluded. This is a comparison for the care team to check, not a diagnosis (*inference*).

*Smallest step.* Three observations, as questions for the care team: head circumference in centimetres (the criterion is 58 cm or more in women); a skin and oral examination with lesion counts, and a biopsy if a papule is found; and polyp histology from RQ3.1.

*Would change the conclusions.* Three major criteria that include macrocephaly or hamartomas, or two major and three minor, would make the syndrome a second, independent explanation for polyps with thyroid cancer and give it a row in the differential. A normal head size and no lesions take weight off that branch, since macrocephaly is reported in 80-100% of carriers once measured (P p. 2; *inference*, the paper gives no likelihood ratio).

*Raised by.* P p. 2, 6, 7; `docs/clinical_case_summary.md:259`.

**RQ4.2 What does the thyroidectomy report show beyond the tumour?**

*Why it matters.* Follicular carcinoma is a major criterion, papillary carcinoma a minor one, and adenoma or multinodular goitre another minor one (P p. 6, 7). The repository notes that the pathologist saw overlap with benign follicular lesions and adenomatoid nodular hyperplasia (`docs/clinical_case_summary.md:37`), and nodular tissue does not follow normal-adult kinetics (C p. 662).

*Smallest step.* Retrieve the report; a re-review of tumour type and background gland if the care team agrees.

*Would change the conclusions.* It decides which thyroid criterion applies, and whether a literature turnover figure describes this gland at all.

*Raised by.* P p. 6, 7; C p. 662.

**RQ4.3 What did the endoscopy and radiology records document?**

*Why it matters.* Three or more lesions of oesophageal glycogenic acanthosis are a minor criterion, and gastric hamartomas count towards the major one (P p. 3, 7). Fundic polyposis of the gastric corpus is the picture of APC promoter 1B variants (Rev p. 3). Whether the liver lesion, the splenoportal shunt and the duplicated vena cava amount to a vascular anomaly in the sense of the criteria is a judgement for a radiologist; the paper calls the haemangioma link uncertain (P p. 5).

*Smallest step.* Collect the upper-endoscopy reports and images and the imaging reports.

*Would change the conclusions.* Up to two minor criteria; the type of the gastric polyps; a test of the repository's multi-organ vascular pattern.

*Raised by.* P p. 3, 5, 7; Rev p. 3.

**RQ4.4 Are the simple physical signs present that the review ties to APC, to PPAP or to constitutional mismatch-repair deficiency?**

*Why it matters.* Retinal pigment lesions, osteomas, dental anomalies and desmoids point to APC; café-au-lait macules to PPAP and to constitutional mismatch-repair deficiency; oligodontia to AXIN2 (Rev p. 2-4). Ledger P05 holds owner statements only, and eye, skin-pigment and dental findings are unrecorded.

*Smallest step.* Questions for the care team: an eye examination, a skin examination and a dental panoramic radiograph.

*Would change the conclusions.* Each shifts the odds within the differential at low cost; none is specific alone.

*Raised by.* Rev p. 2-4; `data/claims_ledger.tsv:42`.

**RQ4.5 What allele fraction does c.138del have in the panel reads?**

*Why it matters.* The call is taken as real and heterozygous on the strength of the signed report (`docs/research_plan_2026-11.md:36`); nobody who wrote the ledger has seen the reads (ledger L03).

*Smallest step.* Run `analysis/panel_bam_checks/panel_bam_checks.py variant` on the panel's alignment file.

*Would change the conclusions.* A fraction well below 50% would suggest mosaicism for c.138del itself and change the implications for relatives. A fraction near 50% confirms a constitutional heterozygote.

*Raised by.* `data/claims_ledger.tsv:37`; `docs/research_plan_2026-11.md:36`.

**RQ4.6 Which dates, blocks and non-neoplastic findings are documented at all?**

*Why it matters.* The files disagree on when the thyroidectomy and the hysterectomy took place (`analysis/mutational_signatures/README.md:5` against `docs/clinical_case_summary.md:185-188`); ledger P08 lists no hysterectomy block; and no ledger row covers the antinuclear antibody result, the hypermobility diagnosis or any other non-neoplastic finding on which the causal statements rest (for example `docs/clinical_case_summary.md:28`).

*Smallest step.* Collect the reports; ask whether a hysterectomy block exists.

*Would change the conclusions.* A retrievable endometrial block would let the endometriosis hypothesis be tested and not asserted, and documented findings can enter the ledger as more than owner statements.

*Raised by.* `data/claims_ledger.tsv:45`; `docs/clinical_case_summary.md:185-188`.

## 5. The class of early truncations, population and family

**RQ5.1 Do c.138del and the polyps travel together in the siblings?**

*Why it matters.* The reply treats co-segregation as a necessary test (M p. 1). Parents cannot be tested, siblings can, and whether any sibling has had a colonoscopy is unknown (ledger P07).

*Smallest step.* Test the siblings; record colonoscopy history and age; write down beforehand which outcomes count for and against.

*Would change the conclusions.* A carrier sibling of similar age with a clean colonoscopy weighs against a causal link, and a non-carrier sibling with polyps points to another cause. With few siblings the result can refute more easily than it can confirm (*inference*).

*Raised by.* M p. 1; `data/claims_ledger.tsv:44`.

**RQ5.2 What do patients with recessive POLE disease show about start-proximal alleles?**

*Why it matters.* In the ClinVar snapshot, c.141del, which ends at the same stop codon as c.138del, is classified Pathogenic or Likely pathogenic with no conflict and with the recessive IMAGe syndrome as its condition (`data/reference/POLE_clinvar_PLP_2026-11-21.tsv:489`), whereas c.138del is conflicting; three IMAGe patients carried the start-loss allele c.1A>T (`docs/pole_variant_comparison.md:69`). The review places loss-of-function alleles within recessive disease (Rev p. 5).

*Smallest step.* Open ClinVar record VCV000587359 and read each submission; re-read in full the patient table of the paper behind ledger E04 and the case series behind the review's references 73-76.

*Would change the conclusions.* An affected patient who carries c.141del or c.1A>T opposite a hypomorphic allele is in-vivo evidence that this class is functionally deficient. A systematically milder phenotype with start-proximal alleles would be patient-level evidence for a hypomorph.

*Raised by.* `data/reference/POLE_clinvar_PLP_2026-11-21.tsv:489`; `docs/pole_variant_comparison.md:69`, `:80`; Rev p. 5.

**RQ5.3 Which cohorts sequenced all of POLE, and do polyposis cohorts in particular show an excess of loss-of-function carriers?**

*Why it matters.* The repository argues from the absence of an excess in published cohorts (`docs/polyposis_differential.md:51-53`). The N363K study screened exonuclease codons only (VP p. 2), and a cohort built that way could not have reported an exon 2 truncation (*inference*). The reply's cases are familial or early-onset colorectal cancer, with three case alleles (M p. 2).

*Smallest step.* Read the methods of each cohort the repository leans on; count POLE truncations in unexplained-polyposis cohorts that did sequence the whole gene, or ask their authors.

*Would change the conclusions.* If most cohorts covered the exonuclease domain only, the argument weakens to one of not having looked. An excess in whole-gene cohorts would be the first class-level signal, and its absence there would firm up Model 0.

*Raised by.* VP p. 2; M p. 2; `docs/polyposis_differential.md:51-53`.

**RQ5.4 How many carriers of exon 1-2 truncations exist in phenotyped cohorts, and what do their colonoscopies show?**

*Why it matters.* The repository's coincidence table assumes a carrier rate of about 1 in 1,000 (`docs/polyposis_differential.md:40`); the reply gives 0.12% of alleles for POLE and POLD1 pooled (M p. 2); and the two gnomAD observations are probably two people of unknown phenotype (ledger D05, an inference).

*Smallest step.* Sum gnomAD loss-of-function allele frequencies for POLE alone; one exome-biobank query for the 34 exon 1-2 alleles with colonoscopy findings (`docs/pole_variant_comparison.md:81`); ask the reporting laboratory about a matching programme (`docs/research_plan_2026-11.md:143`).

*Would change the conclusions.* It rescales the coincidence table (`docs/polyposis_differential.md:43-49`) and could supply the second carrier with a similar history that the repository names as a finding (`docs/polyposis_differential.md:104`).

*Raised by.* `docs/polyposis_differential.md:40`; M p. 2; `data/claims_ledger.tsv:19`.

**RQ5.5 Do c.137del, c.137dup and c.141del behave as c.138del does in the reporter?**

*Why it matters.* A result that holds for the four near-identical alleles turns a single case into a class (`docs/pole_variant_comparison.md:63-64`).

*Smallest step.* The neighbour constructs already in the plan (`docs/research_plan_2026-11.md:64`).

*Would change the conclusions.* Agreement makes the finding publishable as a class; disagreement shows that the result depends on the exact new tail.

*Raised by.* `docs/pole_variant_comparison.md:63-64`.

**RQ5.6 Do carriers of exonuclease-domain variants develop thyroid cancer at all?**

*Why it matters.* None appears among the 33 tabulated members of the N363K families (VP p. 3-4), and the review does not list thyroid under PPAP (Rev p. 3). The repository asserts that none has been reported (`therapeutics/surveillance_protocol.md:126`) with no search on record.

*Smallest step.* Tabulate tumour types across the published PPAP pedigrees; log the search.

*Would change the conclusions.* It strengthens or weakens the reading that the thyroid carcinoma points away from POLE.

*Raised by.* VP p. 3-4; Rev p. 3.

**RQ5.7 Is there any mouse or human study of a heterozygous Pole null allele and cancer?**

*Why it matters.* Ledger E18 is `NOT_FOUND` after 10 of 14 records were examined.

*Smallest step.* A mouse-phenotype database look-up for heterozygous Pole knock-outs; read the remaining four records.

*Would change the conclusions.* A tumour phenotype in heterozygous null mice would count against Model 0, and a normal phenotype would support it.

*Raised by.* `data/claims_ledger.tsv:64`.

**RQ5.8 Is Yamaguchi's exact allele in ClinVar or gnomAD, and how is it classified?**

*Why it matters.* The protein name p.Tyr1398\* is shared with c.4193_4194del, the allele that the aggregator pages show; Yamaguchi's c.4191_4192del was not located (searched 2026-11-21, aggregator pages only).

*Smallest step.* Query both databases by coordinate (12-132643934-TAG-T on GRCh38, computed in the notes and *not verified* against an external database).

*Would change the conclusions.* It shows whether laboratories call that allele Pathogenic by the same loss-of-function rule seen for c.138del (ledger C03).

*Raised by.* Y p. 3, 5; `data/claims_ledger.tsv:67`.

## 6. Classification and reporting

**RQ6.1 What does the laboratory report say it tested?**

*Why it matters.* Nine ledger rows (L01-L03, P03-P08) are owner statements about documents that nobody who wrote the ledger has seen. The report's methods decide what a negative result excluded: APC promoter 1B and the GREM1 region (ledger E16), and the scope of the PTEN assay, since a missed mutation is one explanation the criteria paper gives for patients who meet criteria and test negative (P p. 7).

*Smallest step.* Obtain the report and the pathology reports. The research plan ranks this first (`docs/research_plan_2026-11.md:49-52`) and the README's list omits it (`README.md:69-73`).

*Would change the conclusions.* Owner statements become documents, and the repository can say exactly what was tested in place of listing genes as excluded.

*Raised by.* `data/claims_ledger.tsv:35-37`, `:62`; P p. 7.

**RQ6.2 What should the public records assert, and for which condition?**

*Why it matters.* The live LOVD entry still carries a dominant pathogenic label (`data/lovd_update_2026-11-20.md:8`; ledger D07) and ClinVar is conflicting (ledger D01). The reply offers published wording for the dominant condition, uncertain significance at most for PPAP (M p. 1); the review separates recessive congenital disease and notes that expert-panel rules for POLE are in preparation (Rev p. 5-6).

*Smallest step.* Apply the LOVD update and confirm it by hand; cite the reply and the authors' response in it and in the ClinVar template; decide the recessive wording after RQ1.1 and RQ1.2; consider sending the evidence to the expert panel.

*Would change the conclusions.* One consistent public position: uncertain for the dominant condition, with carrier status for recessive disease stated separately.

*Raised by.* M p. 1-2; Rev p. 5-6; `data/lovd_update_2026-11-20.md:8`.

**RQ6.3 Which kinds of evidence carried each accepted exonuclease-domain variant, and which can be had for c.138del?**

*Why it matters.* p.Asn363Lys was accepted on family genetics alone, with no tumour sequencing (VP p. 4, 6), whereas the repository says that tumour sequencing is the test (`docs/pole_variant_comparison.md:21`).

*Smallest step.* Extend the evidence ladder to L424V, V411L, Y458F and A456P from the primary papers and from the classification recommendations the review cites as its reference 18. *Outside the paper*: According to PubMed, a later cell-line study of N363K exists ([doi:10.1093/narcan/zcad011](https://doi.org/10.1093/narcan/zcad011)); read it in full for any tumour data from the families.

*Would change the conclusions.* A sourced ladder in `docs/pole_variant_comparison.md`, showing that a singleton truncation can be moved only by tissue and functional data.

*Raised by.* VP p. 3, 4, 6; `docs/pole_variant_comparison.md:10`, `:21`.

**RQ6.4 Should the machine-readable files code adenomatous polyposis and a hepatic haemangioma before histology and imaging are settled?**

*Why it matters.* The phenopacket and the HPO table carry both terms (`data/phenopacket/pole_c138del_phenopacket.json:12`, `:51`; `data/phenotype_hpo.tsv:2`, `:5`), while histology is undocumented and the imaging differential is open (`docs/clinical_case_summary.md:46`).

*Smallest step.* Histology-neutral terms until RQ3.1 is answered.

*Would change the conclusions.* It stops an unverified diagnosis from propagating to registries that ingest the phenopacket.

*Raised by.* `data/claims_ledger.tsv:40`.

**RQ6.5 Should the three-level start-codon label be kept?**

*Why it matters.* Kozak 1986 defines no such classes and describes a gradient (K p. 289), and 33 of POLE's 56 in-frame ATGs fall in one bucket (`data/POLE_all_methionines.tsv`).

*Smallest step.* Either keep the rule under the repository's own name with a limits block, as `data/claims_ledger.tsv:10` already words it, or replace the label with a measured score. *Outside the paper*: According to PubMed, one study measured all 65,536 contexts from −6 to +5 ([doi:10.15252/msb.20145136](https://doi.org/10.15252/msb.20145136)).

*Would change the conclusions.* Nothing changes in the sequence facts or the translation map; a misattribution goes, and every ATG gains a number.

*Raised by.* `models/mechanistic_models.md:97`; K p. 289.

**RQ6.6 What consent and ethics approval cover publication of this dataset and of relatives' histories?**

*Why it matters.* The plan records that the owner did not state what is in place (`docs/research_plan_2026-11.md:138`), while ages, calendar years, operative detail and a three-generation family history are public (`docs/clinical_case_summary.md:268-285`).

*Smallest step.* Record the consent and approval position in the repository; review the remaining Word document, which carries operative detail.

*Would change the conclusions.* It is a precondition for every publication the plan envisages.

*Raised by.* `docs/research_plan_2026-11.md:138`.

**RQ6.7 Which sources are still cited at abstract depth or less?**

*Why it matters.* The ledger records abstract-only reading for several rows and a preview for the reply (`data/claims_ledger.tsv:54`); rows N01, B02 and E17 are unverified; and the authors' response to the reply was read only as a publisher's preview. *Outside the paper*: According to PubMed, that response is in *J Hum Genet* 2020;65(6):515-516 ([doi:10.1038/s10038-020-0752-8](https://doi.org/10.1038/s10038-020-0752-8)).

*Smallest step.* Update the reading depth for the eight papers now read in full; obtain the two-page response; read the full texts behind N01, B02 and E17.

*Would change the conclusions.* It completes the record of the Yamaguchi exchange and may surface the original authors' view on mechanism.

*Raised by.* `data/claims_ledger.tsv:54`, `:63`, `:69-70`.

## 7. Therapy and surveillance claims: evidence and questions for the care team

**RQ7.1 Should the brain-imaging line stay?**

*Why it matters.* The paper cited for it questions the value of brain imaging screening, says that no recommendation exists and that the benefit needs careful assessment, and ties the glioblastoma excess to one missense variant (VP p. 1, 5, 6). Nothing in it concerns truncating alleles (*inference*).

*Smallest step.* Put those statements to the care team; reword `therapeutics/surveillance_protocol.md:93` as a question.

*Would change the conclusions.* It removes a recommendation that its cited source does not make.

*Raised by.* VP p. 1, 6; `therapeutics/surveillance_protocol.md:93`.

**RQ7.2 Does the phase 3 trial show any interaction between treatment and mutational burden?**

*Why it matters.* The repository expects stronger responses at higher burden (`therapeutics/immunotherapy_strategy.md:42`). The phase 2b trial found hazard ratios of 0.652 above and 0.586 below its threshold, with wide intervals, and a product capped at 34 neoantigens (W p. 633, 638).

*Smallest step.* Read the full phase 3 report and its supplement. *Outside the paper*: According to PubMed, it randomised 1,137 patients ([doi:10.1056/NEJMoa2609762](https://doi.org/10.1056/NEJMoa2609762)); its abstract gives no burden subgroup.

*Would change the conclusions.* No interaction in a trial seven times larger would undermine the burden-based rationale for melanoma, within the range of burdens seen there (*inference*). An interaction would give that rationale its first empirical footing.

*Raised by.* W p. 638, 641.

**RQ7.3 Has an individualised neoantigen product been tested in any POLE-mutated or mismatch-repair-deficient tumour, or in any polyposis setting?**

*Why it matters.* The repository calls the platform directly applicable to POLE tumours (`therapeutics/immunotherapy_strategy.md:42`). The trial enrolled cutaneous melanoma only (W p. 634), and PubMed searches made on 2026-11-21 found no such study (absence of a hit is not proof of absence).

*Smallest step.* Read the phase 1 report in full (*outside the paper*: According to PubMed, it covers 16 patients; [doi:10.1158/2159-8290.CD-24-0158](https://doi.org/10.1158/2159-8290.CD-24-0158)); search the trial registry; log the queries in `references/search_log.tsv`.

*Would change the conclusions.* It decides whether the applicability statement can ever be more than unsupported.

*Raised by.* W p. 634; `therapeutics/immunotherapy_strategy.md:42`.

**RQ7.4 Under what conditions would the trial evidence bear on this carrier at all?**

*Why it matters.* The files rank the product for a carrier with no known active cancer (`therapeutics/pharmacokinetic_considerations.md:188`). In the trial the product was built from a resected tumour's exome and RNA and given only with pembrolizumab, and people with another malignancy within five years or with active immune disease were excluded (W p. 634). The repository records an antinuclear antibody titre for the carrier (`therapeutics/immunotherapy_strategy.md:63`).

*Smallest step.* Record four conditions in `therapeutics/immunotherapy_strategy.md` (a qualifying malignancy, a sequenced tumour, eligibility or approval, a decision by the care team) and note that a measured high burden is not one of them (*inference*).

*Would change the conclusions.* It turns a ranked option into a conditional statement.

*Raised by.* W p. 634, 636.

**RQ7.5 Can any plan that assumes a hypermutated tumour wait for a sequenced specimen?**

*Why it matters.* The burden is unmeasured (ledger P01), and several files use it as a patient attribute (`therapeutics/surveillance_protocol.md:105`, `:116`). The repository already poses this as a question for the care team (`docs/polyposis_differential.md:132`).

*Smallest step.* The care team's answer; RQ2.2 supplies the measurement.

*Would change the conclusions.* Decisions cease to lean on a number that nobody measured.

*Raised by.* `data/claims_ledger.tsv:38`; `docs/polyposis_differential.md:132`.

**RQ7.6 What surveillance does the phenotype itself call for, whatever the POLE result means?**

*Why it matters.* About 20 polyps with high-grade dysplasia reported are clinically important on their own (`docs/polyposis_differential.md:129`). The review holds that a loss-of-function POLE variant found without congenital disease should not enter clinical decisions (Rev p. 5) and gives no surveillance schedule (*not stated*); the repository's statement that c.138del requires expanded surveillance (`therapeutics/surveillance_protocol.md:7`) finds no support in it.

*Smallest step.* A question for the care team, informed by histology (RQ3.1) and by the guidance papers of RQ3.8.

*Would change the conclusions.* Surveillance reasoning becomes anchored to the documented phenotype and not to the variant.

*Raised by.* Rev p. 5; `therapeutics/surveillance_protocol.md:7`.

**RQ7.7 Should the therapeutics files stay in the main tree with intervals and doses written as fact?**

*Why it matters.* `therapeutics/surveillance_protocol.md:11-101`, `therapeutics/immunotherapy_strategy.md:20-24` and `:71-85`, and `therapeutics/pharmacokinetic_considerations.md:17-191` state intervals, drugs, doses and toxicity rates; two of the four files carry no audit note, and none has a ledger row.

*Smallest step.* Add the banner to every file; rewrite recommendations as questions in the manner of `docs/polyposis_differential.md:127-133`, or move the files to an archive folder.

*Would change the conclusions.* Readers, the carrier among them, can no longer mistake contingency plans for advice.

*Raised by.* `therapeutics/pharmacokinetic_considerations.md:17-191`; `llms.txt:92`.
