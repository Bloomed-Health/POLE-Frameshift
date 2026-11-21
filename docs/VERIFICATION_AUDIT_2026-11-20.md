# Verification audit, 20 November 2026

An independent check of what this repository says about POLE c.138del (p.Leu46Phefs\*8). Every statement below
has a row in [`data/claims_ledger.tsv`](../data/claims_ledger.tsv) with its source and status. The auditor is
not a clinician; clinical points are questions for the patient's care team.

## Summary

The variant call and its name are sound. Most of what the repository built on top of them is not supported:

- the "transcript discrepancy" came from a sequence file that was not POLE;
- the variant is already in ClinVar, dbSNP and gnomAD;
- no tumour has been sequenced, so the hypermutation that the mechanistic models try to explain has never been observed;
- published evidence does not support one loss-of-function POLE allele as a cause of polyposis.

What is new and worth pursuing is different from what the repository claimed: no carrier's phenotype has been
published, nobody has measured what this allele does, and its sequence context makes that an interesting question.

## 1. Findings that change conclusions

| # | Repository said | Verified finding | Ledger |
|---|-----------------|------------------|--------|
| 1 | MANE Select has Glu (GAA) at codon 46; the HGVS name needs reconciliation (caveat C7, Model 7) | Codon 46 is TTG (Leu). c.138del is exactly p.Leu46Phefs\*8: stop at codon 53, predicted 52-residue product (45 native + FGLVLSG). Ensembl VEP agrees | V01, V06 |
| 2 | `data/POLE_coding_sequence.fa` is the POLE coding sequence | It shared 32% nucleotide identity with POLE over the first 480 nt. Removed; replaced by fixtures in `data/reference/` | V06 |
| 3 | Re-initiation could occur at M497 or M530, giving a polymerase without proofreading (Model 2) | Those positions came from the wrong sequence. The first AUG after the stop is Met66 (c.196), 35 nt downstream and in frame. A product starting there keeps both catalytic domains | V07, V10 |
| 4 | GRCh37 chr12:133249847 | That is c.1376 (the p.Ser459Phe site). c.138del is NC_000012.11:g.133257790del | V04, V05 |
| 5 | Absent from ClinVar; novel | ClinVar VCV000548779 since 2018, three clinical laboratories, conflicting: Pathogenic (Labcorp Genetics/Invitae), Uncertain significance (Ambry Genetics; Counsyl) | D01, D02 |
| 6 | Absent from gnomAD (0 of 1,614,586 alleles) | rs1555230420 is present twice: 1 of 1,461,874 gnomAD v4.1 exome alleles and 1 of 31,386 gnomAD v2.1.1 genome alleles (the "gnomAD 0.00003" that ClinVar displays), both non-Finnish European; absent from v3.1/v4.1 genomes. The two sample sets do not overlap, so these are most likely two carriers (gnomAD API, queried during the review of this audit) | D04, D05 |
| 7 | OMIM 612591 for PPAP | CRCS12 is OMIM 615083; 612591 is CRCS10 (POLD1) | D08 |
| 8 | Tumour mutational burden above 100 per megabase | Never measured. Inferred from the literature (owner statement). No tumour or polyp has been sequenced | P01 |
| 9 | Tissue turnover predicts age at onset; "Model 4 prediction validated" | Six data points with one finding entered twice; exact two-sided p = 0.067. Not a validation | P09 |
| 10 | The Pathogenic classification supports a PPAP diagnosis | The Pathogenic submission reasons from loss of function and cites the recessive POLE-deficiency literature. The same template text is used for other POLE truncations | D01, C03 |
| 11 | 34 bibliography entries | Wrong author, title, journal, identifier or all four. Rewritten from PubMed | B01 |

## 2. The variant, re-derived

Run `python3 analysis/variant_verification/verify_c138del.py`. It uses only the fixtures in `data/reference/`.

| Representation | Value |
|----------------|-------|
| Transcript | ENST00000320574.10 = NM_006231.4 (MANE Select), 49 exons, minus strand |
| Coding | c.138del (third base of codon 46; no homopolymer, so the name cannot shift) |
| Protein | p.Leu46Phefs\*8 (ENSP00000322570.5 / NP_006222.2) |
| GRCh38 | NC_000012.12:g.132681204del; VCF 12-132681203-GC-G |
| GRCh37 | NC_000012.11:g.133257790del; VCF 12-133257789-GC-G |
| Exon | 2 of 49 (c.63 to c.204); 75 nt from the exon's 5′ end, 66 nt from its 3′ end |
| Identifiers | ClinVar VCV000548779; dbSNP rs1555230420; ClinGen CA658821754; LOVD POLE_000381 |

```
codon      44   45   46   47   48   49   50   51   52   53
wild type  ATG  GAT  TTG  CGG  TTT  GGT  TTT  GAG  CGG  CTG
           Met  Asp  Leu  Arg  Phe  Gly  Phe  Glu  Arg  Leu
c.138del   ATG  GAT  TTC  GGT  TTG  GTT  TTG  AGC  GGC  TGA
           Met  Asp  Phe  Gly  Leu  Val  Leu  Ser  Gly  stop
```

## 3. What the allele can and cannot make

Computed from the sequence; no experiment exists.

- The annotated start codon sits in a weak context (TCCATGT). Four more AUGs lie between it and the deletion:
  c.47, c.65 and c.68 (out of frame) and c.130 (Met44, in frame, strong context).
- On the mutant mRNA every one of those five AUGs opens an ORF that ends by c.160 (52, 34, 28, 27 and 9 codons).
- The next AUG is Met66 at c.196, in the POLE reading frame, 35 nt after the stop.
- Exon 2 holds 142 nt, so skipping it would also shift the frame. There is no in-frame escape by exon skipping.

Three outcomes are possible, and none of them is a polymerase that lacks proofreading:

| Outcome | Product from this allele | Consequence |
|---------|--------------------------|-------------|
| Efficient nonsense-mediated decay | none | null allele; about half the normal POLE dose |
| Decay escaped, no restart | 52-residue peptide with no known domain | null allele in practice |
| Restart at Met66 | POLE lacking residues 1-65, exonuclease and polymerase domains intact | hypomorphic or near-normal allele |

Whether decay happens is borderline by published rules: the frameshift lies inside the 150-nt start-proximal
window in which decay is inefficient, and the stop begins 8 nt beyond it (Lindeboom et al. 2019,
doi:10.1038/s41588-019-0517-5). Reporter work on p53 found re-initiation after stops up to 126 codons from the
start, with the restart codon 6 to 243 nt downstream (Cohen et al. 2019, doi:10.1093/nar/gkz319); c.138del is
inside both ranges. Attenuated-polyposis alleles of APC are a clinical precedent for 5′ truncations rescued by
an internal AUG (Heppner Goss et al. 2002, doi:10.1073/pnas.112072199).

## 4. Loss of function and cancer risk

| Evidence | Finding | Source |
|----------|---------|--------|
| Case-control | Loss-of-function variants in POLE or POLD1: 0.22% of 2,309 hereditary cancer patients, 0.20% of 59,095 controls (odds ratio 1.08, 95% CI 0.44-2.63) | Mur et al. 2020, doi:10.1038/s41436-020-0922-2 |
| Tumours of a carrier | 1.09-1.70 mutations per megabase, no POLE signature | same |
| Field position | Disruptive variants generally do not predispose to cancer | Mur et al. 2022, doi:10.1038/s41431-021-00926-6 |
| Recessive disease families | Loss-of-function alleles found in unaffected parents; cancer risk in carriers "cannot be assumed" | Logan et al. 2018, doi:10.1016/j.ajhg.2018.10.024 |
| Database curators | Loss-of-function variants cannot cause ultramutated cancers | Tsarin & Shcherbakova 2025, doi:10.1093/database/baaf076 |
| Dosage curation | Haploinsufficiency: little evidence | ClinGen, as displayed by ClinVar |
| One contrary case report | p.Tyr1398\* with adenomas and cancers, contested in the same journal | Yamaguchi et al. 2019, doi:10.1038/s10038-019-0611-7; doi:10.1038/s10038-019-0701-6 |

Model 1 (loss of the wild-type allele producing a hypermutating clone) does not transfer from POLD1 to a null
POLE allele: after loss of the wild-type copy the cell would have no Pol ε catalytic subunit, and depleted
cells fail DNA synthesis (Vipat et al. 2022, doi:10.1038/s41467-022-34911-4).

## 5. The phenotype

See [`polyposis_differential.md`](polyposis_differential.md). In short: the polyps are real and clinically
important (about 20 removed, high-grade dysplasia reported), but their histological type is undocumented here,
no lesion has been sequenced, and the 47-gene blood panel cannot exclude the commonest hidden causes of
unexplained polyposis.

## 6. What was changed in the repository

Fixed in place: the items in section 1; `data/POLE_downstream_methionines.tsv`; `data/POLE_clinvar_variants.tsv`
(c.138del row; p.Ser297Phe label); the phenopacket (now IN_PROGRESS / CANDIDATE / UNKNOWN_ACTIONABILITY, with
the unmeasured tumour feature removed); the ClinVar submission template; the bibliography; in-text
attributions; the variant landscape figure.

Figures: six new README figures are generated from the verified data by `analysis/figures/make_figures.py` and stored in `figures/`; the variant landscape figure was regenerated; the tissue-turnover figure is kept with a caption stating that its correlation is not significant. The README lists each figure and what changed.

Flagged, not rewritten: every file that states a tumour mutational burden for this patient now opens with an
audit note. The narrative of the mechanistic models was corrected only where a statement was factually wrong.

Not touched by the audit: `docs/POLE_Comprehensive_Framework.docx` and `docs/POLE_PPAP_Research.pptx`. Both were removed on 2026-11-21 because they carried the retired claims; the test suite now scans any Office document or notebook added later (ledger N04).

## 6a. The companion 3D viewer

[3D-POLE-Modeler](https://bloomed-health.github.io/3D-POLE-Modeler/) (repository `Bloomed-Health/3D-POLE-Modeler`,
commit 0ef69ab) was reviewed on the same day. A separate patch for it accompanies this audit.

What it does well: experimental structures (PDB 9F6D and relatives) are kept apart from the AlphaFold model;
the exonuclease-dead construct, the meaning of pLDDT and the B-factor proxy are disclosed on the page; a
canonical JSON with a schema and a validator sits behind the pages; and the source file for the mutation page
carried a warning that its codons were placeholders.

What was wrong on the c.138del page, and is corrected by the patch:

| Item | Shown | Verified |
|---|---|---|
| Codon 46 | CTG | TTG |
| Codons 43-45 and 47-53 | Glu Ser Ser ... Glu Leu Arg Ala Ala Leu Pro | Lys Met Asp ... Arg Phe Gly Phe Glu Arg Leu |
| New residues | Phe-Gly-Val-Glu-Gly-Ser-Phe | Phe-Gly-Leu-Val-Leu-Ser-Gly |
| Stop codon | TAG | TGA |
| Hypothesis H1 | restart inside the exonuclease domain gives a polymerase without proofreading | the next AUG is Met66; a restart keeps proofreading |
| Phenotype | "PPAP phenotype (polyposis, multiple primaries)" | polyps of undocumented histology and one primary cancer; nothing sequenced |
| Classification | Pathogenic | Pathogenic on the laboratory report; conflicting in ClinVar (VCV000548779) |
| Citations | "Baranovskiy et al.", "Coorens et al.", Yuan "11:3165" | Lisova, Baranovskiy et al.; Robinson, Coorens et al.; 11:3156 |

Open points that the patch does not settle:

- The domain boundaries (NTD 1-222, exonuclease 223-517, palm 518-870 and so on) are attributed to "Atlas of
  Genetics / UniProt convention". The UniProt record for Q07864 fetched during the audit lists no domain
  features, and this repository's `data/POLE_domain_boundaries.tsv` uses different numbers (exonuclease 268-471).
  Pick one map, cite a structural paper for each boundary, and use it in both repositories.
- The variant catalogue attaches likelihood ratios and "absent from gnomAD" statements to several hotspot
  variants. None was checked in the audit.
- Its reference list carries PMIDs, so the PubMed-record check that found 34 wrong entries here can be run there too.
- The modeler's unit tests were not run (its dependencies could not be installed in the audit environment);
  the data validator and a syntax check passed.

A useful addition: show residues 1-43 and 1-65 on the experimental structure, so that the viewer displays what a
restart at Met44 or Met66 would remove and which contacts those residues make.

## 7. Not verified

Listed so that nobody mistakes silence for confirmation (ledger rows marked UNVERIFIED or NOT_FOUND):

- any splice prediction for c.138del (resolved 2026-11-21: SpliceAI via the Ensembl VEP plugin gives all four delta scores of 0; ledger V13);
- allele-specific ClinVar terms for the exon 1-2 neighbours (the ClinVar identifiers in `data/POLE_clinvar_variants.tsv`, HPO identifiers, methionine positions beyond residue 240 and the gnomAD figures were resolved after the audit; ledger rows D04, D05, D10, D12-D15, N03, V07);
- figures quoted from Li 2018, Andrianova 2024, Ambrosini 2024 and Albertson 2009 that are not in their abstracts;
- COSMIC signature assignments used in this repository;
- the WHO serrated polyposis criteria (PubMed holds no abstract for the update);
- the laboratory report, the BAM/CRAM files and every pathology report: none was seen by the auditor;
- `scripts/fetch_reference.py` and the samtools calls in `analysis/panel_bam_checks/` have not been run end to end.

## 8. How to keep it true

`python3 analysis/variant_verification/verify_c138del.py && python3 -m pytest -q tests` re-derives the variant,
checks the data tables against the derivation, and fails if a retired claim returns. The rules for adding new
claims are in [`EVIDENCE_PROTOCOL.md`](EVIDENCE_PROTOCOL.md).
