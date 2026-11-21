# Eight full texts recast the c.138del case

**The repository's variant-level facts hold, its most recent commit broke its own guarantees, and the eight papers, read in full, leave the incidental-variant reading (Model 0) in front while removing several borrowed claims that pointed the other way.** At commit 59a82b3 (v0.7.0) the derivation scripts still reproduce p.Leu46Phefs\*8 exactly, but 10 of the 52 offline tests fail, because the commit described as a README trim also overwrote about twenty other files with older copies; the README now reports a SpliceAI result that the ledger marks `UNVERIFIED`, and retired statements (a validated Model 4, a tumour burden above 100 mutations per megabase, a first-of-its-kind frameshift) survive in more than twenty files. None of the eight papers supplies evidence that c.138del causes the carrier's phenotype: the 2025 polyposis review states that "loss-of-function variants in POLE and POLD1 are not associated with cancer predisposition or PPAP" ([Rev p. 5](https://doi.org/10.1007/s10689-025-00460-0)), the reply to Yamaguchi sets out the tumour tests a polymerase-driven cancer has to pass, and Yamaguchi's own two tumour genomes fail them and show no second hit at POLE. Four citations carry more than their papers allow: Kozak 1986 contains no three-level strength rule and tested restart only after a five-codon ORF; Coclet 1989 gives 8.5 to 14.4 years for thyroid turnover, not the repository's 2,920 days; Vande Perre 2019 questions the brain imaging it is cited for; and KEYNOTE-942 found no larger benefit in tumours with a high mutational burden and does not contain the five-year figure attributed to it. The same papers add data the repository lacks: POLE's own start-codon context was one of Kozak's measured constructs, Yamaguchi measured a truncated POLE transcript at 41.9% of leukocyte reads, the review names a tissue signature for almost every alternative cause of polyposis, and the Pilarski criteria show that the carrier's comparison with PTEN hamartoma tumour syndrome is incomplete (one minor criterion met, three major criteria never examined), not negative. The decisive next steps are cheap and mostly paperwork: the pathology reports, the methods section of the laboratory report, stains on the stored thyroid block, one blood draw for allele-specific RNA, and an exome of that block judged by rules fixed in advance. Every statement about the carrier rests on owner statements, because no clinical report has been seen by anyone who wrote the ledger or the notes behind this report; everything touching diagnosis, screening or treatment is set out as evidence and as questions for the carrier's care team, never as advice.

> **Audit note, 2026-11-20.** Tumour mutational burden has never been measured in this carrier (ledger P01). Wherever this report mentions a burden above 100 mutations per megabase for c.138del, it is describing a claim that the audit retired, not a finding.

## How this report cites its evidence

Six sets of notes written on 2026-11-21 underlie this report: a re-review of the public repository [Bloomed-Health/POLE-Frameshift](https://github.com/Bloomed-Health/POLE-Frameshift) at HEAD, and full-text readings of the eight papers the owner supplied. Paper claims are tied to a tag and a page; the tag links to the DOI at first use in a section and the bare tag is used afterwards. Page numbers follow the notes exactly, and they are not the same kind of page for every paper.

| Tag | Paper | DOI | A page number means | Read for the notes |
|---|---|---|---|---|
| K | Kozak 1986, *Cell* 44:283-292 | [10.1016/0092-8674(86)90762-2](https://doi.org/10.1016/0092-8674(86)90762-2) | journal page 283-292 | in full; every number taken from the page image, because the scan's text layer is unreliable |
| C | Coclet et al. 1989, *Clin Endocrinol* 31:655-665 | [10.1111/j.1365-2265.1989.tb01290.x](https://doi.org/10.1111/j.1365-2265.1989.tb01290.x) | journal page 655-665 | in full; all five tables re-added from page images |
| P | Pilarski et al. 2013, *J Natl Cancer Inst* | [10.1093/jnci/djt277](https://doi.org/10.1093/jnci/djt277) | Page N of 10 of the Advance Access PDF; the final typeset pages were not seen | in full |
| VP | Vande Perre et al. 2019, *Fam Cancer* | [10.1007/s10689-018-0102-6](https://doi.org/10.1007/s10689-018-0102-6) | PDF page 1-6 of the online-first version | in full; supplement not available |
| Y | Yamaguchi et al. 2019, *J Hum Genet* | [10.1038/s10038-019-0611-7](https://doi.org/10.1038/s10038-019-0611-7) | PDF page 1-12 (journal 729-740, *inference*) | in full; supplement not available |
| M | Mur, Palles, Tomlinson and Valle, reply to Yamaguchi, *J Hum Genet* | [10.1038/s10038-019-0701-6](https://doi.org/10.1038/s10038-019-0701-6) | PDF page 1-2 (journal 513-514, *inference*) | in full |
| W | Weber et al. 2024, *Lancet* 403:632-44 (KEYNOTE-942) | [10.1016/S0140-6736(23)02268-7](https://doi.org/10.1016/S0140-6736(23)02268-7) | journal page 632-644 | main article in full; appendix and linked Comment not supplied |
| Rev | Joo, Viana-Errasti, Buchanan and Valle 2025, *Fam Cancer* 24:38 | [10.1007/s10689-025-00460-0](https://doi.org/10.1007/s10689-025-00460-0) | Page N of 14 as printed; a bracketed number is the review's own reference number | in full |

Five labels are carried over from the notes unchanged. *Inference* marks reasoning or arithmetic by a note-taker (or by the report writer where it says so), not a statement of a paper. *Not stated* means the item was looked for in the full text and is absent. *Outside the paper* marks anything taken from PubMed, PubMed Central or the web; statements from a PubMed record open with the words According to PubMed and carry the DOI link. *Not verified* marks something nobody checked. *Assessment* marks a note-taker's judgement about the repository.

Repository statements are cited as `file:line` at commit 59a82b3, paraphrased and not quoted. Ledger IDs such as V11 or P03 are rows of `data/claims_ledger.tsv`; a line number written after the word audit refers to `docs/VERIFICATION_AUDIT_2026-11-20.md`, one written after the word phenopacket to `data/phenopacket/pole_c138del_phenopacket.json`, and `[P n]` is the n-th paragraph of the one remaining Word document. Facts about the carrier are owner statements as that ledger records them. As a check on the notes, the report writer re-read more than 150 of the cited repository lines at HEAD (each stood where the notes place it), confirmed the static causes of the failing tests, recomputed the reading frames from `data/reference/POLE_MANE_cds_1-480.fa`, and confirmed the eight short quotations in the extracted paper texts. The report writer did not re-run the test suite, did not re-read the papers in full and made no web or database lookups.

## HEAD re-derives the variant correctly and fails ten of its own tests

### The derivation holds; the suite fell from 52 passed to 10 failed

The sequence-level core is intact. Run at HEAD on 2026-11-21 for the re-review, `analysis/variant_verification/verify_c138del.py` exits 0 and prints codon 46 as TTG (Leu), mutant codons 44-53 as ATG GAT TTC GGT TTG GTT TTG AGC GGC TGA, the name p.Leu46Phefs\*8, a 52-residue product (45 native residues plus FGLVLSG), GRCh38 NC_000012.12:g.132681204del, and Met66 at c.196 as the first in-frame ATG after the stop, 35 nt on. `nterm_truncations.py` exits 0 with 26 truncating and 8 start-loss alleles, five of them ending at the same stop codon, and `exact_spearman_check.py` again returns rho 0.821 with an exact two-sided p of 0.0667 for six points. **The test suite does not pass: 10 failed, 42 passed, 14 skipped at HEAD, against 52 passed, 14 skipped on an export of the previous commit da4df83.** Every failure traces to a file reverted or stripped by the last commit, and none touches the derivation.

| Failing test | What it reports | Cause at HEAD |
|---|---|---|
| `test_repo_claims.py::test_checksums` | hash mismatch for `data/phenotype_timeline.tsv` | stale line at `data/checksums.sha256:6` |
| `test_repo_claims.py::test_readme_figures_exist` | no image where eight are required | the README embeds none (`tests/test_repo_claims.py:136`) |
| `test_scientific_consistency.py::test_clinvar_snapshot_summary_is_reproducible_and_on_locus` | missing attribute `is_pole_record` | the filter function was removed from `fetch_clinvar_pole.py` and is still called at `tests/test_scientific_consistency.py:134` |
| `...::test_phenopacket_and_hpo_table_describe_the_same_findings` | HP:0001382, HP:0002578 and HP:0012173 only in the phenopacket | three rows removed from `data/phenotype_hpo.tsv` |
| `...::test_identifiers_quoted_in_documents_match_the_derivation` | assertion at line 274 | the README lost the genomic names, the VCF string and the rsID |
| `...::test_every_doi_and_pmid_cited_in_text_is_catalogued` | PMID 25741868 and three DOIs in neither bibliography nor ledger | four bibliography entries removed |
| `...::test_every_cosmic_signature_named_in_text_is_catalogued` | SBS13 and SBS2 uncatalogued | two rows removed from `data/cosmic_signatures_cited.tsv` |
| `...::test_checksums_cover_every_data_file` | `data/templates/lesion_table_template.tsv` unlisted | checksum line removed |
| `...::test_phenotype_categories_agree_between_timeline_and_hpo_table` | 7 shared findings where 8 are required | follows from the removed HPO rows |
| `...::test_committed_figures_carry_the_same_labels_as_a_fresh_build` | file not found in the temporary directory | `analysis/figures/make_figures.py:32` writes into `figures/` and ignores the override set at `tests/test_scientific_consistency.py:440` |

Three cautions follow. Running the suite inside a working copy overwrites seven tracked files in `figures/`, for the reason in the last row; the re-review restored them and ran its later tests on exports. The 52 offline tests advertised at `README.md:77` are true as a count and false as an assurance at this commit, and the guard tests scan only `.md`, `.tsv`, `.json`, `.py`, `.cff` and `.yml` files (`tests/test_repo_claims.py:9`), so `llms.txt` is checked by nothing. The 14 live tests could not be run without a network, so the SpliceAI, gnomAD, ClinVar, LOVD and PubMed statements were *not verified* today; on continuous integration the figure test would probably skip, because `.github/workflows/verify.yml:21` installs pytest alone, leaving nine failures (*assessment*; whether GitHub Actions ran on 59a82b3 is not visible offline).

### A commit described as a README trim reverted about twenty other files

Four commits separate the pre-audit state from HEAD. The owner's first commit of 2026-11-21, da4df83, adopted the audit across 95 files and its message records 52 passing tests. It also went beyond the audit, adding `llms.txt`, a 23-test scientific-consistency suite, 14 opt-in live tests with a weekly workflow, the full coding-sequence fixture with all 56 in-frame methionines, a dated ClinVar snapshot, and nine ledger rows (63 in the proposal, 72 at that commit). The second, c3ccb31, carries a message that speaks only of shortening the README, yet it changed **36 files** (+710, −1,479 lines) and was merged as pull request #10 to give HEAD. Compared by byte identity with the pre-audit commit, the auditor's staged proposal and da4df83, the 102 files at HEAD fall into five groups: 11 unchanged since before the audit, 25 identical to the audit proposal, 30 modified by the owner and kept, **14 reverted to the original proposal**, and 22 found in none of the other three; four files are gone. Figures regenerated in this commit carry render times of 11:14 and 11:20, earlier than da4df83's 13:02, which marks the returning files as older snapshots and not new edits. The most likely mechanism is an older working copy laid over the newer tree; intent cannot be confirmed from the repository (*assessment*). No git tag exists, so v0.7.0 lives only as text (`CITATION.cff:9`, `CHANGELOG.md:7`, `llms.txt:5`).

Beyond the README, the commit returned ledger row V13 from `VERIFIED` (SpliceAI delta scores of zero through the Ensembl VEP plugin) to `UNVERIFIED`, deleted the ledger entry N06, brought a P2RX2 record back into the POLE ClinVar snapshot by removing its title filter, cut `data/phenotype_hpo.tsv` from 19 rows to 16 and `data/cosmic_signatures_cited.tsv` from 16 signatures to 14, dropped four bibliography entries (lam2017, pilarski2013, heald2010, richards2015; 89 entries to 85), left the checksum file stale, deleted three changelog sections and duplicated blocks in `CITATION.cff` and `.gitignore`. The README itself shrank from 814 lines to 110 and lost material that no other file holds: the table of key caveats C1-C7 that `llms.txt:17` still advertises, the caption saying the tissue-turnover correlation is not evidence for Model 4, all eight embedded figures with their provenance table, the only link to `docs/endometriosis_hypothesis/`, the line of genomic identifiers, and four sections including the comparison with the classical PPAP cohort that cited Vande Perre 2019. **For this review the net effect is that the README cites none of the eight papers and the Pilarski 2013 entry has left the bibliography.**

### Seventeen places where HEAD contradicts its own ledger, tests or documents

| ID | Where | Problem at HEAD | Fix proposed in the notes |
|---|---|---|---|
| A1 | `README.md:61` | Reports all SpliceAI delta scores as zero; ledger V13 (`data/claims_ledger.tsv:14`) says no predictor was run, as do `models/mechanistic_models.md:254`, `CHANGELOG.md:18` and audit `:161` | Restore the da4df83 row and texts, or drop the clause |
| A2 | `README.md:95` | 89 bibliography entries; the file holds 85 (`tests/test_repo_claims.py:120`); ledger B01 says 78 remain (`data/claims_ledger.tsv:68`) | One number in all three places |
| A3 | `README.md:77`, `:96` | 52 offline tests presented as running on every push; 10 fail | Fix the regressions first |
| A4 | `docs/polyposis_differential.md:69,72,74`; `data/clinvar_submission/README.md:78` | Lam 2017, Heald 2010, Pilarski 2013 and PMID 25741868 cited but in neither bibliography nor ledger | Restore the four entries and the ledger entry N06 |
| A5 | `data/reference/POLE_clinvar_PLP_2026-11-21.tsv:60` | A P2RX2 record in the POLE snapshot; 498 records and 13 missense repeated in the summary file, `docs/pole_variant_comparison.md:56-57`, `data/reference/README.md:14`, `CHANGELOG.md:19` and ledger D16 | Restore the filter; 497 and 12 |
| A6 | `data/README.md:28` | 16 findings mapped; the phenopacket lists 17 present features and three terms are missing from the table | Restore the three rows |
| A7 | `analysis/mutational_signatures/README.md:27` | SBS2 and SBS13 named but absent from the signature table, although ledger N02 says every named signature is catalogued | Restore two rows |
| A8 | `data/checksums.sha256:6` | Stale hash; lesion template unlisted; `llms.txt:62` says checksums are enforced by a test | Regenerate |
| A9 | `CHANGELOG.md:35` vs `:19` | The two removed Office files are described both as still carrying superseded claims and as removed; no entry for `llms.txt`, the new suites, the live workflow or the README shortening | Restore the da4df83 sections; add an entry for pull request #10 |
| A10 | `CITATION.cff:9-12` | Version and release-date keys duplicated; the date precedes the 2026-11-21 commits; no tag | Remove duplicates; tag the release |
| A11 | `.gitignore:46-60`, `:62-76` | Patient-data block duplicated | Remove one |
| A12 | `analysis/figures/make_figures.py:32` | Ignores the output override, so tests overwrite `figures/` | Restore the override |
| A13 | `llms.txt:17` | Advertises README caveats C1-C7 and a verification table that the README no longer has; C1-C7 are defined nowhere | Update, or move the content into a document |
| A14 | `llms.txt:71`; `CHANGELOG.md:31`; audit `:112` | Describe README figures; the README embeds none and no document links to `figures/` | Add a figure index |
| A15 | audit `:112`; `analysis/temporal_phenotype/generate_temporal_analysis.py:436-437` | The caption on non-significance lived only in the old README; the figure still carries a Model 4 prediction annotation | Put the caption in the figure or a folder README |
| A16 | `tests/live/test_external_sources.py:74` | Docstring gives V13 as four zero scores, against the ledger | Follows from A1 |
| A17 | `docs/EVIDENCE_PROTOCOL.md:136`, `:130` | Checklist requires a passing suite and a `references/search_log.tsv` that does not exist | Create the log; fix the build |

### Retired and unmeasured claims that survive

The audit flagged pre-audit prose with a banner and did not rewrite it (audit `:114-115`). That banner sits near the top of ten documents and speaks only of tumour burden and histology, so it carries a heavy load: it does not cover the turnover claim, the causal language or the clinical recommendations. The guard tests work from a fixed list of patterns and miss the statements in rows 1 to 7 and the carrier count in row 16. The statements below survive at HEAD; the highest priorities after A1-A9 are the first row, the misattribution in the third row, the polyp description in row 14 and the unmeasured burden in row 10 (*assessment*).

| # | Where | What survives | Why it conflicts | Fix proposed in the notes |
|---|---|---|---|---|
| 1 | `docs/clinical_case_summary.md:204` | Announces the Model 4 turnover prediction as validated | Ledger P09 `CONTRADICTED` (exact p 0.067); no test pattern covers the wording | Delete, or use the P09 wording |
| 2 | `models/mechanistic_models.md:291`, `:305`, `:341`, `:164` | The turnover correlation used as support for Model 4, with a 730-fold ratio, and the duplicated vena cava as direct evidence | Same retired inference; contradicts `README.md:58` | Rewrite as a non-significant illustration |
| 3 | `docs/pole_carrier_registry_crossref.md:25` | Mur 2020 attributed to Valle as first author | Retired misattribution (`references/bibliography.bib:72-83`); the guard regex at `tests/test_repo_claims.py:24` misses this form | Correct; widen the regex |
| 4 | `docs/AI-Research-Assistance-Framework.md:49` | Reasons from absence from gnomAD and posits a repeat at position 138 | The variant is in gnomAD (D04, D05); audit `:42` found no homopolymer | Rewrite |
| 5 | `CONTRIBUTING.md:3`; `data/clinvar_submission/README.md:51` | A novel variant; the first frameshift reported with a PPAP-consistent phenotype; ultra-hypermutation and multiple primaries as reported | In ClinVar since 2018 from three laboratories (D01); Yamaguchi 2019 predates it; burden unmeasured; one primary cancer | A rare variant; strike the caveat |
| 6 | `docs/clinical_case_summary.md:306-307`; `.github/ISSUE_TEMPLATE/pole-case-report.yml:38` | 214 and about 476 residues upstream of the domains | Arithmetic of the retired stop position, codon 54; with the stop at codon 53 the figures are 215 and 477 | Recompute |
| 7 | `models/mechanistic_models.md:82`, `:95`; `docs/AI-Research-Assistance-Framework.md:11`, `:81` | Model 2 still hypothesises a polymerase without proofreading; says methionines beyond residue 240 were not re-checked | Audit section 3; ledger V07 and `data/POLE_all_methionines.tsv` list all 56 | Rewrite the hypothesis; update `models/mechanistic_models.md:95` |
| 8 | `models/mechanistic_models.md:51`, `:207`; `therapeutics/synthetic_lethality.md:53`, `:61-63`, `:73`; `models/computational/README.md:15`; `models/experimental_protocols/README.md:18` | POLE-null cells rescued by Pol δ and hypermutating; the patient's tumours POLE-null through loss of heterozygosity | Audit section 4 and ledger E06: without Pol ε, DNA synthesis fails; `README.md:55` | Mark as superseded |
| 9 | `models/mechanistic_models.md:369`, `:379` | Model 0 at about 10%; Models 4 plus 1 the highest prior at about 35% | `README.md:50` and `llms.txt:9` put Model 0 in front; `models/mechanistic_models.md:377` admits no re-estimation | Remove the percentages or re-estimate |
| 10 | `models/mechanistic_models.md:24`; `docs/clinical_case_summary.md:320`, `:345`, `:365`; `therapeutics/immunotherapy_strategy.md:7`, `:23`, `:36`, `:136`; `therapeutics/surveillance_protocol.md:105`, `:116` | A tumour burden above 100 mutations per megabase written as reported, tabulated beside real variants, and used as a trial-matching attribute | Ledger P01 `NOT_MEASURED`; `docs/clinical_case_summary.md:212` says so itself | Not measured |
| 11 | `analysis/mutational_signatures/README.md:5`, `:9`; `analysis/neoantigen_prediction/README.md:7`; `therapeutics/pharmacokinetic_considerations.md:188`; `docs/comorbidity_interaction_analysis.md:57`, `:64`, `:83`; `docs/AI-Research-Assistance-Framework.md:17`, `:37` | Hypermutation or an extreme neoantigen load presupposed | P01; the pharmacokinetic and comorbidity files have no banner and the burden regex (`tests/test_repo_claims.py:27-28`) does not match their phrasing | Add banners; widen the guard |
| 12 | `docs/clinical_case_summary.md:198`, `:116`, `:159`; `models/mechanistic_models.md:322`; `docs/systematic_health_history.md:49`; `therapeutics/surveillance_protocol.md:79` | Ongoing mutagenesis; POLE-driven predisposition, polyposis or gastritis | The mutation rate was never measured; causation is asserted | Soften or delete |
| 13 | `docs/clinical_case_summary.md:316`; `data/POLE_domain_boundaries.tsv:3`; `docs/pole_variant_comparison.md:10`; `data/clinvar_submission/README.md:51` | P286R and S459F given as germline PPAP examples | Ledger D17: no germline pedigree located for either; V411L rests on one child | Use L424V, N363K and Y458F |
| 14 | `README.md:5`, `:35`; `FAQ.md:46`; `docs/clinical_case_summary.md:34`; `therapeutics/surveillance_protocol.md:17`; `data/tissue_replication_rates.tsv:2`; `data/phenotype_timeline.tsv:4` | About 15 adenomatous polyps; progressive adenomatous polyposis | Histology undocumented (P03; audit `:101`); about 20 at `llms.txt:3`, P03, phenopacket `:20` and `data/phenotype_hpo.tsv:2`; high-grade dysplasia appears in none of README, FAQ or case summary | About 20 polyps, histology undocumented, high-grade dysplasia reported |
| 15 | `README.md:5`, `:25` | Two carriers in gnomAD; 2 of about 1.5 million alleles | D05 calls two carriers most likely (`INFERENCE`); the pooled denominator mixes v4.1 exomes with v2.1.1 genomes | Quote both counts separately |
| 16 | `README.md:54`; `therapeutics/surveillance_protocol.md:124`; `docs/research_plan_2026-11.md:25` | 188 gnomAD loss-of-function carriers; no published data or measurement for such carriers | 188 counts variants (D10 note), an error `CHANGELOG.md:148` records as fixed in v0.5.4; ledger E01 and E02 hold carrier data | 188 variants; qualify the absence claims |
| 17 | `README.md:24`; `FAQ.md:38` | An independent assessment as a variant of uncertain significance | The repository's own PM2 plus PP4 assessment is superseded (`data/clinvar_submission/README.md:47`; `docs/clinical_case_summary.md:22`) | Conflicting in ClinVar; no classification asserted here |
| 18 | `README.md:44-46` | The paradox framing; overlap with PPAP on count, distribution and multi-system involvement | The paradox rested on unmeasured hypermutation (`data/lovd_update_2026-11-20.md:10`); multi-system involvement is not a PPAP criterion (*assessment*) | Retitle; drop the overlap sentence |
| 19 | `docs/clinical_case_summary.md:28`, `:64`, `:72`, `:130`, `:133`; `FAQ.md:49`; `docs/systematic_health_history.md:101`, `:303`; phenopacket `:124`; `data/phenotype_hpo.tsv:10` | Systemic POLE dysfunction; the duplicated vena cava as proof of a congenital POLE effect | No evidence; the same files give a base rate of 0.6-2.6% | Soften or delete |
| 20 | `docs/clinical_case_summary.md:252-260`, `:274`, `:279`, `:283`; phenopacket `:264` | Genes listed as excluded; no relative has polyposis; parental and cascade testing recommended | A blood panel cannot exclude mosaic or structural causes (`docs/clinical_case_summary.md:262`); ledger P07: sibling colonoscopy status unknown, parents cannot be tested | Negative on the panel; none known; sibling testing |
| 21 | `models/mechanistic_models.md:169`, `:338` vs `:287`; `:318` vs `:361` | The thyroid as a high-mitotic-rate gland and as extremely slow; tumour tissue as unavailable and as available | Self-contradictions inside one file; ledger P08 | Fix; adopt the research-plan order |
| 22 | `FAQ.md:47`; `models/mechanistic_models.md:64`, `:337`; `therapeutics/surveillance_protocol.md:147`; `therapeutics/pharmacokinetic_considerations.md:206` | Liver focal nodular hyperplasia stated | The imaging differential is haemangioma against FNH, with FNH less probable (`docs/clinical_case_summary.md:46`); the phenopacket codes a haemangioma (`:51`) | Hypervascular liver lesion |
| 23 | `FAQ.md:62`; `docs/clinical_case_summary.md:213-217`, `:225-228` | Mismatch-repair stains, microsatellite testing and MLH1 methylation described as pending | Nothing is ordered (ledger P02) | Not done |
| 24 | `README.md:77`; `llms.txt:11`, `:88`, `:92`, `:94`; audit `:3-4`, `:165`, `:167`; `data/README.md:16` | Every factual claim has a ledger row; every pre-audit file opens with a note; the companion viewer page was corrected | Large areas have no row; two therapeutics files have no note; the audit says only that a patch accompanies it (audit `:121-122`); its section 7 is stale against ledger N02 | Reword |
| 25 | `docs/endometriosis_hypothesis/POLE_Endometriosis_Hypothesis.docx` [P11], [P61], [P125] | The variant described as producing PPAP | The claim the audit retired; the regex scan misses the wording | Regenerate as Markdown with a banner, or remove |

### Statements written as clinical fact, novelty claims, and drifting numbers

Several files state clinical actions as fact where the repository's own differential asks questions. `therapeutics/surveillance_protocol.md:11-101` and `:133-137` give intervals for colonoscopy, upper endoscopy, neck and ovarian ultrasound, breast MRI, liver imaging and brain MRI, an aspirin dose and a TSH target (`:28`); `therapeutics/immunotherapy_strategy.md:20-24`, `:71-85`, `:99-112` and `:118-120` name a first-line drug and dose with a pre-treatment work-up; `therapeutics/pharmacokinetic_considerations.md:17-191` lists doses, toxicity rates and a therapeutic prioritisation with no sources, no banner and no ledger rows; `docs/clinical_case_summary.md:74-78`, `:155` and `:159-166`, `docs/comorbidity_interaction_analysis.md:106-111` and `:170-181`, `therapeutics/synthetic_lethality.md:81-88` and the Word document `[P150]` do the same on a smaller scale. By contrast `docs/polyposis_differential.md:127-133` phrases every clinical point as a question. Because the carrier has no active advanced malignancy and no measured tumour burden, the first three files plan for a situation that does not exist, and the re-review judges that they should carry a banner or leave the main tree (*assessment*). Separately, about twenty statements claim novelty or absence from the literature (for example `docs/clinical_case_summary.md:56` and `:80`, `therapeutics/surveillance_protocol.md:126`, `:127`, `:144` and `:149`, `docs/comorbidity_interaction_analysis.md:194`, `models/mechanistic_models.md:224`, `data/clinvar_submission/README.md:23`), whereas `docs/EVIDENCE_PROTOCOL.md:20` requires a `NOT_FOUND` row with the query for each; the ledger holds two such rows (D11, E18) and neither covers them.

| Topic | Where | Values or attributions that disagree |
|---|---|---|
| Bibliography size | `README.md:95`; `tests/test_repo_claims.py:120`; ledger B01 | 89; 85; 78 remain |
| Entries corrected by the audit | audit `:33`, `llms.txt:32` and ledger B01; `references/bibliography_corrections.tsv` | 34 wrong; 38 rewritten in the same ledger row; 40 data rows |
| Mur 2020 counts | `docs/clinical_case_summary.md:373`; `docs/pole_carrier_registry_crossref.md:26-27`, `:99`, `:147`, `:181`; `references/bibliography.bib:82`; Word document [P172]; against ledger E01 and `docs/polyposis_differential.md:26-27` | Six loss-of-function POLE variants in 2,813 probands against 5 of 2,309 (0.22%) for POLE and POLD1; only the second is ledgered |
| Somatic POLE in endometrial cancer | `docs/clinical_case_summary.md:56`; `models/mechanistic_models.md:222`, `therapeutics/surveillance_protocol.md:127`, `data/tissue_replication_rates.tsv:5`; Word document [P164] | 7-12%; 7-13%; 13.14% |
| Size of the turnover analysis | `models/mechanistic_models.md:293`; notebook cell 11; ledger P09 and `llms.txt:72` | n = 7; n = 5-7; n = 6 |
| Anglesio 2017 | `therapeutics/surveillance_protocol.md:36` against `:149`, `references/bibliography.bib:645` and Word document [P12], [P81], [P158] | 79% of patients in at least one lesion against 79% of lesions; `CHANGELOG.md:149` records the patient-level reading as the correction |
| First priority | `README.md:69-73`; `docs/research_plan_2026-11.md:47-120`; `docs/polyposis_differential.md:117-125`; `FAQ.md:60`; `analysis/mutational_signatures/README.md:5`; `models/mechanistic_models.md:318` | Six different orders; the README omits the plan's no-cost first rank |
| Identifiers | `data/clinvar_submission/README.md:72` against ledger D08; phenopacket `:407` against `references/bibliography.bib:152` | MedGen C4015260 against C2675481; Robinson 2021 given the PubMed identifier 34163071 in the phenopacket against 34594041 in the bibliography |
| Signatures of the POLD1 family | `docs/polyposis_differential.md:82` against ledger E12 and `docs/pole_variant_comparison.md:20` | SBS10a/b and SBS28 against SBS10c and SBS10d |
| Yamaguchi's allele | audit `:92` and ledger E08 against `docs/pole_carrier_registry_crossref.md:151-157` and `references/bibliography.bib:112` | Named by protein in one place and by cDNA in another, never linked; recomputed from the fixture as one allele |
| Constraint wording | `README.md:25` against `data/POLE_gnomad_constraints.tsv:3` | Tolerates heterozygous loss of function against moderate constraint for LOEUF 0.76 |
| Model 4 support column | `data/tissue_replication_rates.tsv`, column `model4_support` | The value Strong remains for colon, stomach, endometrium and endothelium after P09 |
| Misattributed citations | `therapeutics/immunotherapy_strategy.md:43`; `analysis/duplex_sequencing/README.md:22`; `docs/clinical_case_summary.md:62` and `models/mechanistic_models.md:166`; `models/mechanistic_models.md:279` | Leoni for D'Alise; Pich for Lawson 2025; Coco dated 2019 for 2016, a single case report used for a prevalence; Karam dated 2010 for 1999 |
| Uncatalogued or unverified sources | text-only citations; DOIs without entries; `therapeutics/synthetic_lethality.md:23`; `data/clinvar_submission/README.md:77` | Nine works cited by name only; sixteen DOI-cited works with no bibliography entry, the Mur reply among them; a reference the audit could not locate still in an evidence list; a Palles 2022 citation that is a different paper from `palles2022`; ledger N01 figures (Ambrosini, Andrianova) still stated without a flag |

### The endometriosis document, `llms.txt` and provenance

`docs/endometriosis_hypothesis/POLE_Endometriosis_Hypothesis.docx` is not new owner content: it was added on 2026-04-15 (commit e11f5fb) and is byte-identical in every version compared. No document links to it at HEAD, and the only mention is ledger N04, whose statement that it carries none of the retired patterns is true of the regex list and misleading about content (*assessment*). Its 154 paragraphs assert three times that the variant produces PPAP, call the co-occurrence with endometriosis the first known case, repeat the 79%-of-lesions reading and the six-carrier Mur count, cite a first author the bibliography has since corrected (key `praetorius2022`), never mention the hypermobility diagnosis that the rest of the repository names as the more parsimonious explanation (`therapeutics/surveillance_protocol.md:9`; `models/mechanistic_models.md:23`), cite no tissue, RNA or sequencing result for any causal link, and carry operative detail from two surgeries (`[P16]` to `[P48]`). The same hypothesis recurs at `docs/clinical_case_summary.md:56`, `models/mechanistic_models.md:154`, `:160`, `:167` and `:336`, `therapeutics/surveillance_protocol.md:127`, `:144` and `:149`, `data/tissue_replication_rates.tsv:5` and `docs/comorbidity_interaction_analysis.md:140-156`, and no ledger row covers any part of it.

`llms.txt`, new in da4df83 and untouched since, is the most accurate summary in the repository at HEAD apart from its descriptions of the README and of the pre-audit files (*assessment*). It makes no causal link between c.138del and any condition, and it is covered by no test.

Sequence-level provenance is strong; patient-level and literature-level provenance is thin. The ledger's 71 claims (72 lines with the header) divide into 44 `VERIFIED`, 9 `OWNER_STATEMENT`, 7 `CONTRADICTED`, 5 `UNVERIFIED` (V13, E17, C02, B02, N01), 2 `INFERENCE` (V11, V12), 2 `NOT_MEASURED` (P01, P02) and 2 `NOT_FOUND` (D11, E18). No row covers the carrier's sex, age band and ancestry (`README.md:31`), any diagnosis other than the polyps, any age in `data/phenotype_timeline.tsv`, the family history (`docs/clinical_case_summary.md:268-285`), the confirmation on two platforms (`README.md:22`), any drug dose or toxicity rate, or the model parameters. Most data tables other than the sequence fixtures are hand-curated or hand-transcribed with no generating script or stored response in the repository, and the search log that `docs/EVIDENCE_PROTOCOL.md:130` prescribes does not exist. No sequence, alignment, VCF or report has ever been tracked, yet quasi-identifiers are dense and public (age at each diagnosis, calendar years, lesion sizes, operative detail, a three-generation family history), so the data are de-identified only as to direct identifiers, and relatives are described with no statement of their consent (*assessment*); `docs/research_plan_2026-11.md:138` records that the owner did not state what consent or ethics approval is in place. The single most useful provenance step is the one the research plan ranks first and the README omits: obtaining the laboratory report and the pathology reports, so that nine owner statements become documents (*assessment*).

## Where the notes disagree with each other or with the repository

The six sets of notes agree on every main finding. They differ on the points below, and several of the differences trace back to the repository contradicting itself. The last column says how each point was resolved, or that it was not.

| # | Point | What the notes or the repository say | Resolution or status |
|---|---|---|---|
| 1 | Files carrying the audit banner | Re-review notes: twelve files. Weber notes: eleven documents | Report writer's check at HEAD: the string occurs in 12 files, one of which is the test that defines it (`tests/test_repo_claims.py:29`); ten documents carry the tumour-burden banner and an eleventh (`docs/pole_carrier_registry_crossref.md:153`, `:163`) carries two different notes. Both sets agree that `therapeutics/pharmacokinetic_considerations.md` has none |
| 2 | Size of the ledger | Re-review notes: 71 rows. Kozak notes: 72 rows. Weber notes: 72 lines | 72 lines, namely a header and 71 claims |
| 3 | Bibliography entries the audit corrected | Kozak notes repeat 34 (ledger B01; audit `:33`). Re-review notes find 38 rewritten in the same ledger row and 40 data rows in `references/bibliography_corrections.tsv` | The repository's own inconsistency; unresolved |
| 4 | Polyposis in relatives | Vande Perre and review notes take `docs/clinical_case_summary.md:274` at face value. Re-review notes flag that line against ledger P07 (`data/claims_ledger.tsv:44`) | The ledger governs: whether any sibling has had a colonoscopy is unknown |
| 5 | Mismatch-repair testing | Vande Perre and review notes list it as present in the plan and pending (`docs/clinical_case_summary.md:223-229`). Re-review notes: nothing is ordered (ledger P02) | Not done |
| 6 | Archived polyp tissue | Yamaguchi notes treat polyps as available only at the next endoscopy. Vande Perre, review and Pilarski notes propose work on stored blocks now | `data/claims_ledger.tsv:45` (P08) records polyp blocks held by several institutions, some abroad. Retrieval is a matter of logistics that the step list at `docs/polyposis_differential.md:117-125` does not include |
| 7 | Lesion template | Yamaguchi notes: clinical columns only. Review notes: it has a field for tests done. Pilarski notes: no ganglioneuroma class | All three hold: `data/templates/lesion_table_template.tsv:1-2` has one free-text `tests_done` column, no result columns and no ganglioneuroma class |
| 8 | Whether restart after the premature stop is plausible | Ledger V11 and E09 (`data/claims_ledger.tsv:12`, `:55`): the geometry lies inside the range where re-initiation was seen in p53 reporters (Cohen 2019, abstract read). Kozak notes: later work says restart falls as the upstream ORF lengthens, and 52 codons lies beyond every length quoted | Unresolved. Both literatures are *outside* Kozak 1986, neither was read in full for the ledger, and the experimental systems differ. Taken up as a research question |
| 9 | The ORF a ribosome translates before Met66 | Kozak notes, in their limits section: 52 codons. The same notes elsewhere, and ledger V10: ORFs of 34, 28, 27 and 9 codons opened at c.47, c.65, c.68 and Met44 also end upstream of Met66 | Report writer's recomputation from the fixture confirms V10. The 52-codon figure applies only to ribosomes that start at c.1 |
| 10 | A short-ORF control for the reporter | Kozak notes propose c.76del as a construct whose stop lies nearer the start | `docs/pole_variant_comparison.md:37` records that c.76del runs into the same stop codon; recomputed here, it gives the same 52-codon ORF as c.138del. It is not a length control |
| 11 | Thyroid turnover | Ledger N05: about 8.5 years, `VERIFIED` from the abstract. Repository elsewhere: 2,920 days and 5-8 years. Coclet notes: 8.5 years is the minimal estimate and 14.4 the strict one | The full text governs: 8.5 to 14.4 years (C p. 663) |
| 12 | Germline p.Ser297Phe | Repository: no germline pedigree located (`data/POLE_clinvar_variants.tsv:8`; ledger D17). Review: p.S297F listed among constitutional variants with aggressive early phenotypes (Rev p. 3) | *Not verified* further: the review does not say which of its references 19-25 carries it |
| 13 | Commonest identifiable cause of unexplained polyposis | Repository: mosaic APC (`docs/polyposis_differential.md:56-58`). Review: no ranking; about 30% of unexplained cases with the colibactin hotspot in at least one tumour (Rev p. 8) | Needs reconciling; the figures use different denominators (*inference*) |
| 14 | The 93% figure for PTEN carriers | Repository: polyps of mixed type (`docs/polyposis_differential.md:71-72`). Pilarski notes, *outside the paper*: polyps of any type | Wording to correct; see the Pilarski section |
| 15 | Year of the reply to Yamaguchi | Repository: 2020. The supplied PDF: 2019 | Both are right: online 11 December 2019; According to PubMed the issue is June 2020 ([doi:10.1038/s10038-019-0701-6](https://doi.org/10.1038/s10038-019-0701-6)) |
| 16 | The five-year figure for KEYNOTE-942 | Repository attributes it to Weber 2024 (`therapeutics/immunotherapy_strategy.md:42`). Weber notes: not in the paper | The paper reports a hazard ratio of 0.561 at about two years (W p. 632); see the Weber section for where the later figure comes from |
| 17 | Depth at which the papers were read | Ledger: abstract for Coclet, Vande Perre and Yamaguchi; a preview for the reply; nothing recorded for Kozak, Pilarski and Weber | The notes now supply full-text readings of all eight |

## What each paper adds, supports and contradicts

At HEAD the repository uses five of the eight papers in running text and none in the README. Two have no bibliography entry (Pilarski 2013, lost in the last commit; the Mur reply, never entered) and the review is cited nowhere in any version. Only three ledger rows depend on these papers (N05; D12 with D17; E08). Two uses carry clinical weight beyond what the paper is about, the brain-imaging suggestion and the vaccine priority, and both rest on premises the audit removed.

### Kozak 1986: a measured gradient, POLE's own start codon, and no three-level rule

The entry `kozak1986` (`references/bibliography.bib:746-757`) matches the paper in every field; According to PubMed the record is PMID 3943125, *Cell* 1986 Jan 31;44(2):283-92 ([doi:10.1016/0092-8674(86)90762-2](https://doi.org/10.1016/0092-8674(86)90762-2)). Its note calls the paper the foundational description of the consensus, whereas the paper presents itself as the mutational test of a consensus that earlier surveys had produced ([K p. 283](https://doi.org/10.1016/0092-8674(86)90762-2)). The repository uses the paper for one thing, the three-level label defined at `models/mechanistic_models.md:97`, and no ledger row cites it.

In a rat preproinsulin reporter driven by the SV40 early promoter in COS cells, single-base changes around the initiator ATG moved proinsulin yield over a 20-fold range (K p. 283, 285). The read-out is relative band density: duplicate plates agreed within 20%, and the author accepted a difference only at two-fold or more (K p. 285, 288). ACCATGG was optimal; position −3 dominates in the order A > G > C > T; a G at +4 helps most when −3 is not A (about 5-fold with T at −3, 4-fold with G, only 2-fold with A); and the contributions are not additive (K p. 285). In one series the measured values were **5.0 for A at −3 with G at +4, 3.1 for G with G, 2.6 for A with T, 0.9 for C or T with G, 0.7 for G with T, and below 0.2 for T with T** (Fig. 2, K p. 286). The paper names no classes. The word moderate does not occur in it, and its Discussion says that "initiation sites are not simply strong or weak" (K p. 289).

Three results bear directly on POLE and are absent from the repository. First, the annotated POLE start, TCCATGT from −3 to +4 (ledger V09), is the exact context of Kozak's mutants B145 and B147, which made **at least four times more** proinsulin than the all-pyrimidine construct B140 (below 0.2); no value is printed for that figure, so the paper supplies a lower bound and not a number (K p. 285; Fig. 5, K p. 287). The Cs at −1 and −2 lift this context off the floor, and on Kozak's measurements the annotated start sits in the same low band as the c.47 and c.65 contexts (about 0.7-0.9), with the real step lying between those and the sites with A at −3 at 2.1-5.0 (*inference*). The repository's label `weak` places it in the bucket of constructs that scored below 0.2. Second, yield and leakiness are different measures: ATTATGT gives a good yield (2.6 against 5.0) and is still bypassed by about 10% of ribosomes (K p. 289), and for c.138del the quantity that matters is the fraction that leaks past. Third, an upstream out-of-frame ATG blocks a downstream start in proportion to its own context: with A at −3 the downstream yield fell ten-fold whatever the base at +4 (K p. 287; Fig. 6, K p. 288). POLE has such a codon. The ATG at c.68 (ATGATGG) is out of frame, carries A at −3 and G at +4, and lies between the annotated start and Met44. Its ORF, like those opened at c.47 and c.65, ends at c.158_160 on the wild-type mRNA, 28 nt past the Met44 ATG, and Kozak's stated condition for reinitiation is a terminator upstream of the second ATG (K p. 283). Ribosomes that start at those three codons therefore cannot restart at Met44, and only ribosomes that bypass all three can use it (*inference*).

On restart itself the paper is thin. Its one experiment placed a minicistron of five codons (counted from the sequence in Fig. 7; *inference*) so that its terminator lay ten nucleotides upstream of the preproinsulin start; yield across four restart contexts varied about 8-fold, with the same preference for a purine at −3, and no values are printed (K p. 287; Fig. 7, K p. 289). The effect of upstream-ORF length, the effect of terminator-to-ATG distance and restart after a premature stop inside a main ORF are *not stated*. Neither is anything about positions −6, +5 or +6, the yield with A or C at +4 (Met66 has C at +4), nonsense-mediated decay, or any human mRNA. *Outside the paper*, the notes point to the literature that does address length. According to PubMed, a 1987 study by Kozak found reinitiation improving as the intercistronic sequence lengthened, reaching at 79 nt the efficiency seen with no upstream ATG ([doi:10.1128/mcb.7.10.3438-3445.1987](https://doi.org/10.1128/mcb.7.10.3438-3445.1987)). Kozak's 2002 review, read through PubMed Central, describes reinitiation as often seen after ORFs of 10-12 codons, substantially reduced from 13 to 33 codons, and seen by Luukkonen and colleagues after a 24-codon but not a 40-codon ORF ([doi:10.1016/S0378-1119(02)01056-9](https://doi.org/10.1016/S0378-1119(02)01056-9)). According to PubMed, Luukkonen et al. found inhibition proportional to upstream-ORF length ([doi:10.1128/JVI.69.7.4086-4094.1995](https://doi.org/10.1128/JVI.69.7.4086-4094.1995)). The 5′ coding region of POLE is also extremely GC-rich (91.7% for c.11-c.46, computed from the fixture), and According to PubMed a companion paper found that a structure of −50 kcal/mol cut yield by 85-95% ([doi:10.1073/pnas.83.9.2850](https://doi.org/10.1073/pnas.83.9.2850)), a confounder for any leaky-scanning prediction in this leader.

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `models/mechanistic_models.md:97` and `CHANGELOG.md:290`: a three-level rule credited to Kozak 1986 and 1987 | Attribution not supported; a defensible simplification presented as the paper's own | K p. 289; the two positions and the direction of every label are right |
| `models/mechanistic_models.md:97`: positions −3 and +4 as the primary determinants | Supported for this system | 10-fold for −3 and 5-fold for +4 (K p. 285), but also at least 4-fold for −1 and −2 together when −3 is T |
| `analysis/variant_verification/verify_c138del.py:105-115`; `data/POLE_all_methionines.tsv`; `data/POLE_downstream_methionines.tsv` | Faithful to the repository's own rule; every context reproduces | The rule merges A and G at −3 (5.0 against 3.1; 2.6 against 0.7; Fig. 2, K p. 286), ignores −1 and −2, and puts 33 of 56 sites in one bucket |
| `data/claims_ledger.tsv:10` (V09) | The best-worded use: it states the sequence fact and names the rule as the repository's own | n/a |
| `figures/c138del_translation_map.svg`, lane labels and caption | The caption's disclaimer is correct; the lane labels carry the rule into a figure, where they read as measured properties | n/a |
| `docs/AI-Research-Assistance-Framework.md:11`: a strong context greatly raises reinitiation probability; consensus written with a leading GCC | Partly supported | Context does affect restart (about 8-fold, four plasmids; K p. 287). The 1986 optimum is (CC)ACCATGG (K p. 289); the GCC form is from a later paper (*outside the paper*; According to PubMed, [doi:10.1093/nar/15.20.8125](https://doi.org/10.1093/nar/15.20.8125)). ORF length was never tested |
| `docs/AI-Research-Assistance-Framework.md:81`: a percentage probability of restart from Kozak scores | Not supported | The paper reports relative densities with a two-fold threshold and no absolute efficiency (K p. 285, 288) |
| `docs/pole_variant_comparison.md:46`: Met44 by leaky scanning, or Met66 after a 37-codon ORF | Mechanism supported; restart after 37 codons not supported by this paper | The paper describes bypass of a start codon and never uses the term leaky scanning (K p. 286-287); it tested a five-codon minicistron only (K p. 289) |
| `docs/pole_variant_comparison.md:78`: is Met44 a natural second start? | Consistent with the paper | It expects a second, inefficient initiation site in most mRNAs (K p. 289) |

### Coclet 1989: 8.5 to 14.4 years, from thirteen labelled cells

The entry `coclet1989` (`references/bibliography.bib:704-715`) is right in every identifying field; According to PubMed the record is *Clin Endocrinol (Oxf)* 1989 Dec;31(6):655-65, PMID 2627756 ([doi:10.1111/j.1365-2265.1989.tb01290.x](https://doi.org/10.1111/j.1365-2265.1989.tb01290.x)). The audit's rewrite shortened five authors to three and others, and the note giving 5-8 years survives from the first version of the entry and is not supported by the paper.

The paper calculates turnover and does not measure it. Turnover time is the S-phase duration divided by the labelling index, under an assumed homogeneous age distribution ([C p. 661](https://doi.org/10.1111/j.1365-2265.1989.tb01290.x)), and the human S phase of 10 hours is assumed from other tissues, not measured in thyroid (C p. 662). Slices from nine adults aged 22-56, most of them histologically normal tissue from glands resected for benign nodules or cysts, were labelled in vitro with tritiated thymidine (C p. 657, 661). Counting follicular cells strictly, 13 of 148,400 were labelled, which gives a labelling index of 7.9 × 10⁻⁵ and a turnover time of about **14.4 years**; counting every ambiguous cell as follicular, 24 of 162,700 were labelled, giving 13.4 × 10⁻⁵ and **8.5 years**, which the authors call "the minimal estimate of the TOT" (C p. 661-662). The Summary prints only the second figure (C p. 655), so a reader of the abstract gets the fast end of a range of 8.5 to 14.4 years (C p. 663). The authors' conclusion is that about five divisions per cell span the whole of adult life (C p. 655, 663). No variance is given for any human value (*not stated*); a Poisson interval on the counts alone spans about 8.4-26.9 years for 13 cells and 5.7-13.3 years for 24 (*inference*). Three further results matter here: the one adolescent, aged 13, had a turnover time of about 167 days (C p. 661-662); benign nodules labelled at 45 to 694 × 10⁻⁵, far above normal tissue (C p. 662); and stromal cells, 21% of the population, turned over in about 4.67 years (C p. 662).

**The repository's 2,920 days is not a number in the paper.** It is exactly 8.0 years, whereas the paper's two values convert to about 3,109 and 5,272 days. Repository history shows the figure entering `data/tissue_replication_rates.tsv` on 2026-04-15 without a source, two days before the Coclet entry was added, so the citation was attached to an existing value (*inference*). The five in the bibliography note is the paper's count of divisions, not a number of years (*inference*). Correcting the value can neither rescue nor sink the turnover correlation, because the test uses ranks: the notes recomputed rho 0.821 and exact p 0.0667 with 2,920, 3,102.5, 5,256 and even 167 days (*inference*). What the paper does change is the reading of the thyroid tumour. An adult gland that completes roughly one population turnover per decade is among the least-dividing tissues, so a carcinoma at 28 is the weakest fit for a model in which fast turnover brings early disease (*inference*). Nothing in the paper concerns POLE, replication fidelity or mutation rate; a turnover time counts replications, not errors per replication, and Model 4 needs both.

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `data/tissue_replication_rates.tsv:7`: 2,920 days with a source note of 8.5 years | The value is not in the paper; value and note disagree with each other | C p. 662 |
| `data/claims_ledger.tsv:33` (N05): about 8.5 years, `VERIFIED` from the abstract | Matches the Summary; incomplete against the full text | C p. 655, 663 |
| `references/bibliography.bib:714`: 5-8 years | Not supported | C p. 662-664 |
| `models/mechanistic_models.md:284`, `:287` | The value is not in Coclet and 5-8 years is contradicted; the text calls the figures stem or progenitor division rates, whereas Coclet measured the whole follicular population; the co-cited Dumont 1992 has no bibliography entry | C p. 663 |
| `models/mechanistic_models.md:291`: a 730-fold difference in division rate | 730 is 2,920 divided by 4; with the paper's values the ratio to a four-day colon is about 780 to 1,310 (*inference*) | C p. 662 |
| `models/mechanistic_models.md:169`, `:338`; `docs/clinical_case_summary.md:130`; `docs/systematic_health_history.md:174`: the thyroid as a rapidly dividing or high-mitotic-rate gland | Contradicted | A labelling index near 10⁻⁴ and a few divisions in a lifetime (C p. 663) |
| `docs/clinical_case_summary.md:187`; `data/phenotype_timeline.tsv:10`: about 8 years | Order of magnitude right | C p. 662-663 |
| `analysis/temporal_phenotype/exact_spearman_check.py:5`; `generate_temporal_analysis.py:100, 391`; the notebook; `tests/test_scientific_consistency.py:396` | 2920 is hard-coded; the rank statistic is unaffected; the test pins the value, so script, notebook and test have to change together | n/a |

*Outside the paper*: According to PubMed (abstract only), a Ki-67 study of 117 autopsy thyroids found indices of 7.4 ± 6.10% in fetal glands, 0.23 ± 0.15% at 0-19 years and 0.08 ± 0.04% at 20-60 years ([doi:10.1210/jc.2006-0417](https://doi.org/10.1210/jc.2006-0417)), an independent and larger series whose abstract gives no turnover time. The unsourced Dumont 1992 beside Coclet at `models/mechanistic_models.md:284` is probably a *Physiological Reviews* article (*inference*); According to PubMed it has no abstract ([doi:10.1152/physrev.1992.72.3.667](https://doi.org/10.1152/physrev.1992.72.3.667)), and it was not read.

### Pilarski 2013: one minor criterion met, three major criteria never examined

No bibliography entry and no ledger row exist at HEAD: the entry present at da4df83 was removed by the last commit, and the single inline citation at `docs/polyposis_differential.md:73-74` is correct in author, year and DOI. According to PubMed the final citation is *J Natl Cancer Inst* 2013 Nov 6;105(21):1607-16, PMID 24136893 ([doi:10.1093/jnci/djt277](https://doi.org/10.1093/jnci/djt277)); the notes read the Advance Access version.

The paper is a systematic review that replaces the 1996 consortium criteria, which its authors judged "too lax" ([P p. 7](https://doi.org/10.1093/jnci/djt277)). Its table lists as **major criteria** breast cancer; epithelial endometrial cancer; follicular thyroid cancer; three or more gastrointestinal hamartomas, with ganglioneuromas included and hyperplastic polyps excluded by name; adult Lhermitte-Duclos disease; macrocephaly at or above the 97th percentile (58 cm in women); macular pigmentation of the glans penis; and multiple mucocutaneous lesions of four defined kinds. The **minor criteria** are autism spectrum disorder, colon cancer, three or more lesions of oesophageal glycogenic acanthosis, three or more lipomas, intellectual disability, renal cell carcinoma, testicular lipomatosis, papillary thyroid cancer (the follicular variant included), thyroid structural lesions and vascular anomalies. A clinical diagnosis in an individual needs three major criteria, one of them macrocephaly, Lhermitte-Duclos disease or gastrointestinal hamartomas, or else two major and three minor criteria (P p. 7). Benign breast disease, uterine fibroids and genitourinary anomalies were dropped for want of evidence (P p. 1, 3, 4, 7).

Five things in the full text matter for this carrier. Papillary thyroid carcinoma is a minor criterion and only follicular carcinoma is major; among carriers with thyroid cancer the split is 56-60% papillary to 25-45% follicular, six of twelve papillary cancers in one series were microcarcinomas, and the authors allow that some papillary diagnoses are incidental (P p. 6). Adenomas are not named in the gastrointestinal criterion, so a patient with adenomas alone scores nothing there however many there are (*inference*), although adenomas made up 27% of polyps in the series the paper cites, beside 29% hamartomatous, 26% ganglioneuromas and 18% inflammatory (P p. 3). Macrocephaly is found in 80-100% of mutation carriers once it is measured (P p. 2). A negative PTEN test does not close the question: only 30-35% of patients meeting the old criteria carried a mutation, and patients who meet criteria without one may have a missed mutation, another gene or a phenocopy (P p. 2, 6, 7). And the validation was one-sided: 44 of 48 mutation carriers met the new criteria, the four who did not being two children and two adults of 33 and 35 who had had no colonoscopy, and specificity was not measured (P p. 6; *inference*). Pseudoangiomatous stromal hyperplasia, endometriosis, adenomyosis, liver lesions, a duplicated vena cava, dysplastic naevi and cribriform-morular thyroid carcinoma are *not stated* anywhere in the paper.

Scored against the table on the documented features alone, the carrier has **no major criterion and one minor criterion**, the stage I papillary thyroid carcinoma. This is a worked comparison for the care team to check and not a diagnosis (*inference*). Three major criteria cannot be scored at all: gastrointestinal hamartomas, because the histology of about 20 polyps is undocumented (ledger P03); macrocephaly, because the head has never been measured; and mucocutaneous lesions, because ledger P05 records that no clinician examined for them. Lhermitte-Duclos disease is unassessed for want of documented brain imaging, and oesophageal glycogenic acanthosis, thyroid structural lesions (the repository mentions adenomatoid nodular hyperplasia at `docs/clinical_case_summary.md:37`) and vascular anomalies await the endoscopy, pathology and radiology reports. Neither rule is met, and at least three new positive findings would be needed under either. The comparison is far from met, and it cannot be closed as negative while three major criteria are unexamined; the paper's own two adult failures were 33 and 35 years old (P p. 6).

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `docs/polyposis_differential.md:73-74`: benign breast disease does not count towards the diagnosis | Supported | P p. 1, 3, 7. The paper analysed fibrocystic change, fibroadenoma and intraductal papilloma; pseudoangiomatous stromal hyperplasia is not mentioned |
| `docs/polyposis_differential.md:71-72`: polyps of mixed type in 93% of carriers who have an endoscopy, credited to Heald 2010 | Wording off | Pilarski prints up to 95% for colonoscopy (P p. 3). *Outside the paper*: According to PubMed, the Heald abstract reports polyps in 64 of 69 endoscoped carriers (93%), half of them with hyperplastic polyps ([doi:10.1053/j.gastro.2010.06.061](https://doi.org/10.1053/j.gastro.2010.06.061)): any polyp, not mixed type |
| `docs/polyposis_differential.md:72-73`: PTEN negative on the panel and none of the usual signs noted | Not supported as a reason to set the syndrome aside | Ledger P05: no clinician examined. The criteria need a measured head circumference and counted, partly biopsied lesions (P p. 7), and a negative test does not settle a clinical diagnosis (P p. 2, 7) |
| `docs/clinical_case_summary.md:259`: Cowden syndrome listed as excluded | Overstated | P p. 2, 6, 7 |
| `docs/polyposis_differential.md:75-76`: the benign breast, liver and skin lesions match no defined syndrome on the panel | Partly at odds | Vascular anomalies are a minor criterion (P p. 7), although the haemangioma link is called uncertain (P p. 5); papillary thyroid carcinoma is a minor criterion, which the repository never says |
| `data/templates/lesion_table_template.tsv:2` | Incomplete for scoring | No ganglioneuroma class (P p. 7) and no lipomatous, leiomyomatous or lymphoid class (P p. 3) |
| `docs/polyposis_differential.md:78-88` | Omission | No row for what this syndrome predicts in tissue |

*Outside the paper*: According to PubMed, Pilarski's 2019 overview states that the 2013 revision was adopted by the US National Comprehensive Cancer Network and reports PTEN mutations in 2.2% of 603 patients with five or more colon polyps including at least one hamartomatous or hyperplastic polyp ([doi:10.3390/cancers11060844](https://doi.org/10.3390/cancers11060844); full text read through PubMed Central). According to PubMed, a 2025 international consensus guideline describes the syndrome as a molecular diagnosis ([doi:10.1158/1078-0432.CCR-24-3819](https://doi.org/10.1158/1078-0432.CCR-24-3819); keyword-searched only). The current NCCN wording was not opened (*not verified*). The paper offers no way to turn a criteria score plus a negative test into a probability, and the notes attempt none.

### Vande Perre 2019: a pedigree proven without tumour sequencing, and no case for brain imaging

The entry `vandeperre2019` (`references/bibliography.bib:933-943`) is correct in every field that can be checked and lacks only the issue number; According to PubMed the final citation is *Fam Cancer* 2019 Apr;18(2):173-178, PMID 30368636 ([doi:10.1007/s10689-018-0102-6](https://doi.org/10.1007/s10689-018-0102-6)). Its note says the variant extends the PPAP tumour spectrum, which is stronger than the paper's own claim that the variant may raise brain-cancer risk and that more observations are needed ([VP p. 1](https://doi.org/10.1007/s10689-018-0102-6)).

This is a clinical report of one family with no tumour genomics. Eleven tested carriers of POLE c.1089C>A, p.Asn363Lys, span three generations (VP p. 2-4); with the first family, reported by Rohlin in 2014, there are 23 carriers, of whom **16 (69.5%) had colorectal cancer** at a mean age of 45 (range 23-67) and **4 (17.4%) had glioblastoma** (VP p. 1, 5, 6). Polyp counts in carriers ran from 3 to more than 50, polyps were recorded from age 19, and histology where given was tubular or tubulovillous adenoma with low-grade dysplasia; carriers also had a gastric adenoma, a gastric carcinoma at 36 and duodenal adenocarcinomas at 48 and 52 (VP p. 3-4). **No thyroid or breast cancer appears among the 33 people tabulated** (VP p. 3-4). All tumours tested were microsatellite stable with mismatch-repair proteins retained, apart from one sigmoid polyp with isolated MSH6 loss and a normal germline MSH6 (VP p. 2). Mutation burden was not performed (Table 2, VP p. 4), signatures were not done, and second-hit analysis and functional testing are named as future work (VP p. 6). The variant was accepted as pathogenic without a stated framework, on its location in the exonuclease domain, its recurrence in a second family, transmission through three generations, stable tumours and the exclusion of seven other genes (VP p. 1-3, 5-6).

Two points change how the repository can use the paper. The POLE assay covered only the exonuclease coding region, printed as codons 304-517 for POLE and 268-471 for POLD1 (VP p. 2); the two ranges look transposed, and an assay limited to either could not detect an exon 2 variant such as c.138del (*inference*). Studies built like this one therefore say nothing about how often truncations occur in such families. And the authors argue against the use to which the repository puts them: the value of brain imaging screening "remains questionable" (VP p. 1), no recommendation exists, the benefit of MRI follow-up needs careful assessment, and heightened vigilance would not improve care and would burden patients and families (VP p. 6). They tie the glioblastoma excess to this one variant, noting that POLE mutations are not all equally associated with extra-gastrointestinal tumours, and they leave open a co-segregating modifier (VP p. 1, 5). The paper also contains several inconsistencies in ages and attributions (one carrier's glioblastoma is dated to 45 in the tables and to 42 in the text, VP p. 2), so its ages should be cited with care.

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `references/bibliography.bib:942`: three carriers with giant cell glioblastoma | Supported | Three carriers and one untested relative (VP p. 4, 5) |
| `data/POLE_clinvar_variants.tsv:9`: a second family with colorectal cancer and giant cell glioblastoma | Supported | VP p. 1, 6. The transcript version NM_006231.2 and the ClinVar status are not from this paper, which prints NM_006231 without a version (VP p. 2) |
| `data/claims_ledger.tsv:26` (D12) and `:31` (D17) | Supported; depth recorded as abstract | VP p. 1; Fig. 1, VP p. 2; Table 1, VP p. 3-4 |
| `docs/pole_variant_comparison.md:10`: p.Asn363Lys in a row whose tumours are ultramutated with SBS10a/b and a retained wild-type allele | Dominant inheritance supported; the tumour description is not shown for this variant by this paper | VP p. 1, 4, 6. Class-level support exists in the review (Rev p. 7-8) |
| `therapeutics/surveillance_protocol.md:93`: a brain MRI row with a yearly interval suggested, citing this paper | The glioblastomas are supported; the interval runs against the source | VP p. 1, 6. Nothing in the paper transfers to a truncating allele outside the exonuclease domain (*inference*) |

*Outside the paper*: According to PubMed, a later study from the same group knocked N363K into human cell lines and reported mutation rates above those of L424V and exonuclease-null cells ([doi:10.1093/narcan/zcad011](https://doi.org/10.1093/narcan/zcad011)). The repository already holds that entry (`references/bibliography.bib:945-956`); whether it reports burden in the families' own tumours is not in the abstract.

### Yamaguchi 2019: the tumour data argue against the paper's own label

The entry `yamaguchi2019` (`references/bibliography.bib:102-113`) matches in every field; According to PubMed the record is PMID 31089268, *J Hum Genet* 2019 Aug;64(8):729-740, with the publication type Case Reports ([doi:10.1038/s10038-019-0611-7](https://doi.org/10.1038/s10038-019-0611-7)). Its note does not record that the PPAP attribution was contested.

The paper reports one patient: a 68-year-old woman with three synchronous colon cancers and adenomatous polyps whose number is never given ([Y p. 1, 2](https://doi.org/10.1038/s10038-019-0611-7)), carrying germline POLE c.4191_4192del, p.Tyr1398\*, in exon 33, found by whole-genome sequencing of blood (Y p. 4-5). Only the proband was genotyped; the word segregation does not occur, and consent is recorded from the patient alone (Y p. 11), although a brother and a niece had colorectal cancer (Y p. 2-3). No polyp was analysed, and the third cancer was not analysed. Checked against the repository's fixture, the deletion leaves 1,397 residues before the stop, 61% of the protein, and a neighbouring change, c.4193_4194del, yields a stop at the same codon, so the protein name alone does not identify the allele (*inference*).

The tumour results are what the repository lacks. The ascending-colon cancer was microsatellite-unstable with loss of MLH1 and PMS2, a hypermethylated MLH1 promoter, BRAF p.Val600Glu and **488,915 somatic mutations (81.5 per 10⁶ bases)**; the sigmoid cancer was microsatellite stable with APC, KRAS and PIK3CA drivers and **16,687 mutations (2.8 per 10⁶ bases)** (Y p. 5-9). **Neither tumour had a second hit at POLE**, by single-nucleotide variant or by copy-number change (Y p. 5); copy-neutral loss of heterozygosity is *not stated*, and MSH6 was not stained (Y p. 3). The printed rates imply a denominator near 6,000 Mb that the paper does not give (*inference*), so the raw counts are the safer figures to quote. The main text describes a signature comparison with 17 TCGA cancers without saying into which group its two tumours fall (Y p. 7); the statement that the unstable tumour lacks the POLE signature comes from the reply's reading of a supplementary figure, and the supplement could not be retrieved for the notes.

The paper also holds one RNA measurement that the repository would want as a benchmark. In leukocytes the deletion made up 1,001 of 1,987 DNA reads (**50.4%**) and 827 of 1,976 transcript reads (**41.9%**), from which the authors wrote that the mutant transcripts "are assumed to be degraded through nonsense-mediated RNA decay" (Y p. 5). The mutant transcript therefore stood at about 71% of the wild-type level, a clear but small reduction, for a stop that lies 2,553 nt upstream of the last exon junction, where position alone predicts decay (*inference*). The method is not described, no decay inhibitor was used and no protein was measured. The authors' case for PPAP is one of exclusion plus gene identity, and no step of it tests causality (*inference*); they absorb the non-hypermutated tumour by proposing a mechanism other than loss of exonuclease activity (Y p. 10). They cite one earlier germline POLE frameshift, c.5621_5622delGT with colorectal cancer at 26, and say it came with no tumour information (Y p. 10); the repository does not hold it.

### The reply by Mur and colleagues: a mechanistic checklist and a small frequency table

The reply has no bibliography entry in any version. It is cited by bare DOI in three documents and one ledger row (`docs/VERIFICATION_AUDIT_2026-11-20.md:92`; `docs/polyposis_differential.md:32`; `docs/pole_carrier_registry_crossref.md:153`; `data/claims_ledger.tsv:54`), and the ledger's depth note records a preview only. According to PubMed it is PMID 31822785, *J Hum Genet* 2020 Jun;65(6):513-514, published online on 11 December 2019 ([doi:10.1038/s10038-019-0701-6](https://doi.org/10.1038/s10038-019-0701-6)). None of its numbers or arguments appears anywhere in the repository.

The reply defines PPAP by mechanism. Aberrant proofreading leaves tumours with mutation counts frequently above 100 per megabase and an excess of C:G to A:T transversions, and only curated missense variants in the exonuclease domain have been tied to it ([M p. 1](https://doi.org/10.1038/s10038-019-0701-6)). It then applies that definition to Yamaguchi's data: the stable tumour is not hypermutated; the unstable tumour owes its burden to mismatch-repair deficiency, with more than 80% of the signature contribution from COSMIC signatures 6 and 15 and no trace of signatures 10 or 14 in the supplementary figure; and there is no co-segregation (M p. 1). Its conclusion is that the variant should have been classified "at most, as a variant of uncertain significance for PPAP" (M p. 1), that the patient should not be regarded as a PPAP case, that the cause of her polyposis remains to be found, and that diagnostic laboratories should take special care, because they habitually call loss-of-function variants in cancer genes pathogenic (M p. 1-2).

Its own data are one table. Counting start-loss, stop-gain and frameshift alleles of POLE and POLD1 together, it finds **122 of 102,460 alleles (0.12%) in non-cancer, non-Finnish European gnomAD v2.1.1 controls against 3 of 1,864 (0.16%) in familial or early-onset colorectal cancer, p = 0.8571** (M p. 2). The notes' arithmetic reproduces the p value and gives an allelic odds ratio of 1.35 with a 95% interval of about 0.43 to 4.26 (*inference*). With three case alleles, two genes pooled, colorectal cancer and not polyposis as the phenotype, and European controls for a patient treated in Tokyo, the table supports the statement that no risk has been shown; it does not establish that there is none. The reply does not address Yamaguchi's RNA measurement, the absence of a second hit, or any route by which a loss-of-function allele could raise risk without a proofreading defect (*not stated*). *Outside the paper*: According to PubMed, the original authors answered in the same journal (Yamaguchi and Furukawa, *J Hum Genet* 2020 Jun;65(6):515-516, PMID 32246048; [doi:10.1038/s10038-020-0752-8](https://doi.org/10.1038/s10038-020-0752-8)). Only the publisher's preview could be read; in it the authors accept classification as a variant of uncertain significance, say that relatives' samples could not be obtained, and decline to call the variant benign. The repository holds no entry for that response.

| Repository statement | Verdict | Basis in the two full texts |
|---|---|---|
| `data/claims_ledger.tsv:54` (E08) | Supported, missing nuance | Give the cDNA name, since the protein name is shared with c.4193_4194del (*inference*); the cancers number three and the polyp count is never given (Y p. 1, 2); the authors later accepted uncertain significance (*outside the paper*); the depth can now read full text for both |
| `docs/VERIFICATION_AUDIT_2026-11-20.md:92`: one contrary case report | Supported, missing nuance | The report is contrary only in its authors' interpretation; its tumour data agree with the other rows of that table (Y p. 5; M p. 1) |
| `docs/polyposis_differential.md:30-32` | Supported | Add the authors' concession and the earlier frameshift the paper cites (Y p. 10) |
| `docs/pole_carrier_registry_crossref.md:151`: a heading that presents the case as a comparator | Overstated; inconsistent with the audit note two lines below, at `:153` | M p. 1-2 |
| `docs/pole_carrier_registry_crossref.md:155`: the case described as a PPAP patient | Overstated in part | It repeats the paper's title without qualification and the reply rejects the label (M p. 2); the variant name and the MLH1 silencing are supported, for one of three cancers (Y p. 1, 7-9) |
| `docs/pole_carrier_registry_crossref.md:157`: asks whether non-neoplastic phenotyping was documented; says the allele preserves both catalytic domains | The question is answered: *not stated* (Y p. 2). The domain statement describes a predicted product | The paper measured RNA only and showed no protein (Y p. 5) |
| `docs/clinical_case_summary.md:228`: MLH1 silencing can co-occur with POLE mutations | The example is supported; the general clause lacks nuance | The unstable tumour had no somatic POLE alteration (Y p. 5) and, per the reply, no POLE signature (M p. 1) |
| `docs/AI-Research-Assistance-Framework.md:21` | Supported for the unstable tumour; the PPAP label is overstated and the sentence carries no citation | Y p. 6-9 |
| `data/clinvar_submission/README.md:51`: the first frameshift reported with a PPAP-consistent phenotype | Wrong as a priority statement | Yamaguchi's report went online on 14 May 2019 (Y p. 1) |
| `docs/pole_variant_comparison.md:60` and `FAQ.md:58`: no truncating variant has been shown to cause PPAP | Supported | M p. 1 |
| `docs/pole_variant_comparison.md:12`: loss-of-function tumours not hypermutated where measured | Missing data | Yamaguchi's two tumour genomes are absent; with them the cell needs a qualifier, since one was hypermutated through mismatch-repair loss (Y p. 5) |

### Weber 2024: no larger benefit at higher mutational burden

The entry `weber2024` (`references/bibliography.bib:887-898`) matches the title page in every bibliographic field; According to PubMed the record is PMID 38246194, issue 10427 ([doi:10.1016/S0140-6736(23)02268-7](https://doi.org/10.1016/S0140-6736(23)02268-7)). Its note, like `therapeutics/immunotherapy_strategy.md:42` and `CHANGELOG.md:227`, attaches a 49% reduction at five years to this paper. **That figure is not in it**, and no ledger row cites the paper.

KEYNOTE-942 is an open-label, industry-sponsored, randomised phase 2b trial in **157 adults with completely resected stage IIIB-IV cutaneous melanoma**, assigned 2:1 to the individualised product mRNA-4157 with pembrolizumab or to pembrolizumab alone ([W p. 632-634](https://doi.org/10.1016/S0140-6736(23)02268-7)). The product was never given without pembrolizumab, and no arm was untreated (W p. 634). Recurrence-free survival gave a **hazard ratio of 0.561 (95% CI 0.309-1.017; two-sided p = 0.053)**, with events in 24 of 107 against 20 of 50 patients at a median follow-up of 23 and 24 months (W p. 632, 637-638). The result counts as positive only against the trial's prespecified one-sided alpha of 0.10 (W p. 635), and the interval includes 1. During the pandemic nine patients were moved by hand to monotherapy and the last 37 were all assigned to the combination (W p. 634, 636), so 46 of 157 allocations (29%) did not follow the randomisation scheme alone (*arithmetic*). Overall survival and T-cell responses are not reported, and the authors themselves ask for longer follow-up and a phase 3 trial (W p. 641-642).

The paper bears directly on the repository's argument that a higher burden means more neoantigens and therefore more benefit. High burden was defined as 175 or more mutations per exome, about 10 per megabase (W p. 635), and 109 of the 154 evaluable patients (71%) were already above it (*arithmetic*). The hazard ratio was **0.652 (0.284-1.494) in the high-burden group and 0.586 (0.243-1.415) in the rest** (W p. 638). Within each arm higher burden went with fewer recurrences, which makes burden a prognostic marker with or without the product (W p. 637), and the authors read the benefit as "irrespective of the size of the TMB" (W p. 641). The product also has a ceiling: it encodes at most 34 neoantigens (W p. 633), 91% of patients received all 34 (W p. 636), and the authors write that the number needed is unknown and that one might suffice (W p. 642). These analyses are exploratory, with a single cut-off, 45 patients and 20 events below it, no interaction p value in the main article, and melanoma only, so the trial cannot exclude a moderate gradient in either direction.

On applicability the paper is equally clear. The product is built from the patient's own tumour by exome and RNA sequencing with a blood sample (W p. 634), and 15 of the 224 people screened failed for an inadequate tumour sample (W p. 636). People with another malignancy in the past five years or with active immune disease were excluded (W p. 634). Grade 3 or higher treatment-related events occurred in 25% against 18% (W p. 632). The words POLE, polyp, prevent, germline and thyroid do not occur in the article. On the paper's evidence four conditions would all have to hold before any of this bore on the carrier: an actual malignancy of a type with trial evidence (in this paper only resected stage IIIB-IV cutaneous melanoma), a sequenced tumour with enough tissue, eligibility for a trial or access through an approval, and a decision by the care team about a product tested only on top of pembrolizumab. None holds now, and a measured high burden is not on the list (*inference*).

*Outside the paper*, later results exist and the repository cites a press release in their place. According to PubMed, a peer-reviewed five-year report gives hazard ratios of 0.510 (95% CI 0.294-0.887) for recurrence-free survival, 0.411 (0.200-0.843) for distant metastasis-free survival and 0.471 (0.165-1.345) for overall survival, all labelled descriptive (Khattak et al., *J Clin Oncol* 2026;44(26):2482-2489, PMID 42223134; [doi:10.1200/JCO-26-00835](https://doi.org/10.1200/JCO-26-00835); abstract read). The 49% therefore corresponds to a hazard ratio of 0.510, which first appeared at three years in a release from the sponsors ([Merck news release, 3 June 2024](https://www.merck.com/news/moderna-merck-announce-3-year-data-for-mrna-4157-v940-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-recurrence-free-survival-distant-metastasis-free-su/)). According to PubMed, the phase 3 trial INTerpath-001 has been published: double-blind, 1,137 patients with resected stage IIB-IV cutaneous melanoma, 24-month recurrence-free survival 82.2% against 70.0% (Long et al., *N Engl J Med*, e-published 11 November 2026, PMID 43013837; [doi:10.1056/NEJMoa2609762](https://doi.org/10.1056/NEJMoa2609762); abstract read, full text not accessible). The repository's statement that phase 3 is ongoing was therefore out of date on the audit date. Subgroup results by burden from the phase 3 trial were not found. The notes' PubMed searches of 2026-11-21 found no neoantigen-vaccine study in POLE-mutated tumours, in POLE carriers or in polyposis of unexplained cause; absence of a hit is not proof of absence.

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `therapeutics/immunotherapy_strategy.md:42`, data cell; `references/bibliography.bib:897`; `CHANGELOG.md:227` | The efficacy figure is not in the cited paper | W p. 632; a hazard ratio over the whole follow-up is also misdescribed as a reduction at five years |
| Same line: phase 3 trials ongoing | Supported at the paper's date; outdated on 2026-11-21 | The paper says a phase 3 trial has been initiated (W p. 633) and names no lung-cancer trial |
| Same line, relevance cell: directly applicable to POLE ultra-hypermutated tumours | Not supported | Cutaneous melanoma only (W p. 634); POLE is never mentioned |
| Same cell: stronger responses expected than in the trial population | Not supported, and against the direction of the data | W p. 638, 641; no measurement of vaccine response is reported |
| `therapeutics/immunotherapy_strategy.md:32-36` | The setting matches the trial for resected melanoma only; the rationale rests on an unmeasured load | W p. 633, 634, 636; ledger P01 |
| `therapeutics/pharmacokinetic_considerations.md:188`: ranked third, with the route given as intramuscular or intravenous | Route imprecise; the ranking presumes a cancer and a measured burden | mRNA-4157 was given intramuscularly at 1 mg, the intravenous drug was pembrolizumab, and the product was never given alone (W p. 634). The file carries no audit note |
| `analysis/neoantigen_prediction/README.md:40`: candidates for vaccine design on this platform | Overstated | Neoantigens were chosen by the sponsor's proprietary in-house system (W p. 634) |
| `therapeutics/surveillance_protocol.md:112` with `:105` and `:116` | Missing nuance | The one randomised trial required resected melanoma, disease-free status and tumour tissue, and excluded another recent malignancy and active immune disease (W p. 634); an unmeasured burden is listed as a patient attribute |
| `FAQ.md:80-82`; `llms.txt:81`, `:94`; `README.md:92` | Accurate conditional framing | The vaccine statements inside the therapeutics files are not themselves written conditionally |

### Joo and colleagues 2025: the review states the repository's central conclusion

The review is in no version of the repository: it has no bibliography entry, no citation and no ledger row. The nearest item, ledger E15, cites a different article; According to PubMed that one is the review by Shur and colleagues of APC mosaicism and promoter variants, the next article in the same issue ([doi:10.1007/s10689-025-00464-w](https://doi.org/10.1007/s10689-025-00464-w)), which has no bibliography entry either. According to PubMed the review read here is PMID 40237887, PMCID PMC12003455, *Fam Cancer* 2025 Apr 16;24(2):38 ([doi:10.1007/s10689-025-00460-0](https://doi.org/10.1007/s10689-025-00460-0)). It is a narrative, open-access review of adenomatous polyposis only, with 147 references, one figure and no tables; it contains no diagnostic algorithm, no polyp-count threshold for testing and no surveillance schedule ([Rev p. 2, 9](https://doi.org/10.1007/s10689-025-00460-0)). For guidance it points to two documents the repository lacks (its references 1 and 12) and to one the repository holds as `mur2023` (its reference 18).

On POLE the review says in plain words what the audit concluded. Cancer-associated variants lie within the exonuclease domain, and clinical action is warranted, in the review's view, only where a variant damages proofreading and spares DNA synthesis, a description that so far fits certain exonuclease-domain missense variants and nothing else (Rev p. 3, 5). Loss-of-function variants, in the sentence quoted at the head of this report, are set apart from every other hereditary cancer gene. The review links constitutional loss-of-function variants, and variants outside the domain, to rare and severe congenital disorders; for a cancer patient who has no such disorder, its rule is that counselling and clinical decisions leave the variant out of account (Rev p. 5). That statement is an assertion with citations and not data: it comes with no carrier counts and no tumour results, and nothing on start-proximal truncations, reinitiation or decay (*not stated*). The typical PPAP picture is fewer than 100 adenomas, diagnoses at 35-60 years, and colorectal, endometrial, ovarian, breast, brain and upper-gastrointestinal cancers; thyroid cancer is not listed, and gastric polyps in PPAP are *not stated* (Rev p. 3). One wording needs care. The review calls POLE proofreading deficiency haploinsufficient, meaning that one exonuclease-domain missense allele suffices without a second hit (Rev p. 7); this is not a statement about null alleles and cannot be cited in support of Model 4. Expert-panel classification rules for POLE and POLD1 are described as under development (Rev p. 5-6). The review's senior author leads the laboratory that the repository proposes to approach about the paradox (`docs/pole_carrier_registry_crossref.md:147`), so the position on Rev p. 5 should be known before that approach is made (*inference*).

For the polyps the review supplies names and numbers the repository lacks. **Up to one-third of adenomatous polyposis has no genetic diagnosis** (Rev p. 9). Each cause has a tissue read-out (Fig. 1, Rev p. 2; Rev p. 7-8): SBS18 with SBS36 for MUTYH, SBS30 for NTHL1, SBS1 or SBS96 with more than 60% of substitutions at methylated CpG sites for MBD4 (SBS96 as named in the review's reference 114, which is not the COSMIC signature of that name; see the checks at the end), SBS6, 15, 21, 26 and 44 with ID2 and ID7 for mismatch-repair deficiency, instability at tetranucleotide repeats for MSH3, SBS88 with ID18 for colibactin, and SBS10a, SBS10b and SBS28 for POLE; MLH3 tumours show no microsatellite instability and have no known signature (Rev p. 7). **About 30% of unexplained adenomatous polyposis had at least one tumour carrying the colibactin-associated splice variant APC c.835-8A>G** (Rev p. 8). For mosaic APC the review gives working rules: lower the allele-fraction threshold to 5% or less in blood data, test normal mucosa or several polyps, analyse at least two independent lesions because most adenomas acquire their own APC mutations, and confirm with digital PCR across tissues; 10-25% of de novo APC cases are estimated to be mosaic (Rev p. 4). Standard panels also miss deep-intronic APC variants, for which paired DNA and RNA testing is recommended, point variants at the YY1 site of promoter 1B, a 5′UTR variant, and structural variants, which one small study found in about 24% of patients tested by MLPA (Rev p. 3-5). One monoallelic MBD4 carrier had about 30 adenomas and a colorectal cancer at 42 with loss of the wild-type allele in the tumour (Rev p. 6). Cribriform-morular papillary thyroid cancer is listed among the cancers of familial adenomatous polyposis, and thyroid nodules as a rare benign feature of MUTYH polyposis (Rev p. 2, 3). Simple physical signs help to separate the causes: congenital hypertrophy of the retinal pigment epithelium, osteomas, dental anomalies and desmoids for APC; café-au-lait macules for PPAP and constitutional mismatch-repair deficiency; oligodontia for AXIN2 (Rev p. 2-4). Serrated and hamartomatous syndromes, RNF43, GREM1, SMAD4 and BMPR1A lie outside the review, and it was accepted in March 2025, before the 2026 mosaicism papers on which the repository relies.

| Repository statement | Verdict | Basis in the full text |
|---|---|---|
| `docs/VERIFICATION_AUDIT_2026-11-20.md:14`; `docs/polyposis_differential.md:19-21`; `docs/pole_variant_comparison.md:12`, `:59-61` | Supported, in plain words, by the group that wrote the POLE and POLD1 classification recommendations | Rev p. 5 |
| `docs/pole_variant_comparison.md:10`: the exonuclease-domain class | Supported at class level | Rev p. 3, 7-8; the review adds SBS28 and SBS14 |
| `docs/polyposis_differential.md:56`: much polyposis stays unexplained | Supported and quantified | Rev p. 9 |
| `docs/polyposis_differential.md:56-58`: mosaic APC as the commonest identifiable cause | Differs; needs reconciling | The review gives no ranking (Rev p. 4, 8). *Outside the paper*: According to PubMed, the Shur 2025 abstract says mosaicism can be found in up to 50% of unexplained adenomatous polyposis ([doi:10.1007/s10689-025-00464-w](https://doi.org/10.1007/s10689-025-00464-w)); the repository quotes only the lower part of a wide range |
| `docs/polyposis_differential.md:67-70`, `:83`, `:84`, `:85`, `:93-94` | Supported; the names and thresholds are missing from the repository | Rev p. 2, 4, 7, 8 |
| `docs/polyposis_differential.md:95-97`: APC promoter 1B as a copy-number question | Incomplete | Point variants and a 5′UTR variant, which copy-number analysis does not detect (Rev p. 3, 5) |
| `docs/clinical_case_summary.md:252`: APC listed as excluded | Too strong | Rev p. 4-5 |
| `docs/clinical_case_summary.md:371-373`; `FAQ.md:68-74`: guidelines would need extending; truncations may need reclassifying as pathogenic | Contradicted in direction | Rev p. 5 |
| `models/mechanistic_models.md:70`: risk dependent on loss of heterozygosity may extend to POLE loss-of-function variants | Not supported | Second-hit dependence is described for POLD1 exonuclease variants, not for POLE and not for null alleles (Rev p. 5, 7) |
| `therapeutics/surveillance_protocol.md:7`: c.138del requires expanded surveillance | Not supported | Rev p. 5 |
| `docs/clinical_case_summary.md:34` and `:39`: gastric involvement as characteristic of POLE heterozygotes; the list of PPAP cancers | Not confirmed by this review | Upper-gastrointestinal cancers only; ovarian and breast cancer added (Rev p. 3) |
| `data/POLE_clinvar_variants.tsv:8` and ledger D17: no germline pedigree for p.Ser297Phe | Differs | Listed among constitutional variants with aggressive early phenotypes (Rev p. 3); *not verified* further |
| `analysis/mutational_signatures/README.md:19-28` | Incomplete | SBS18, SBS36, SBS30, SBS96, SBS88, ID2, ID7 and ID18 occur nowhere in the repository (Fig. 1, Rev p. 2; Rev p. 7-8) |

### What to add and where, in priority order

The three tables below turn the eight comparisons into a work list. The first corrects statements that a cited paper does not support, which matters most because those statements sit beside clinical content. The second adds data that change reasoning or planning. The third is record-keeping.

**Priority 1: correct statements the cited paper does not support**

| # | File and line | Change | Source |
|---|---|---|---|
| 1 | `therapeutics/surveillance_protocol.md:93` | Recast the brain-imaging row as a question for the care team and record the authors' own position: the value of imaging is questioned, no recommendation exists, and the excess is tied to p.Asn363Lys | VP p. 1, 5, 6 |
| 2 | `therapeutics/immunotherapy_strategy.md:42`; `references/bibliography.bib:897` | State what the 2024 paper reports (phase 2b, n = 157, hazard ratio 0.561, 95% CI 0.309-1.017, two-sided p 0.053, follow-up 23 and 24 months); cite the later follow-up separately as abstract-only; mark the applicability and stronger-response sentences as unsupported; update the phase 3 status | W p. 632-638, 641 |
| 3 | `therapeutics/pharmacokinetic_considerations.md:188` and the head of that file | Give the route as intramuscular for mRNA-4157 and intravenous for pembrolizumab; say the product was never given alone; add the audit note the file lacks; extend the guard at `tests/test_repo_claims.py:27-28` to burden-dependent wording it misses | W p. 634 |
| 4 | `models/mechanistic_models.md:97`; `CHANGELOG.md:290`; `analysis/variant_verification/verify_c138del.py:105-115`; lane labels of `figures/c138del_translation_map.svg` | Present the three-level rule as the repository's own (as ledger V09 already does), drop the attribution to Kozak, and add a limits block: reporter system, two-fold threshold, positions never varied | K p. 285, 287-289 |
| 5 | `data/tissue_replication_rates.tsv:7`; `data/claims_ledger.tsv:33`; `references/bibliography.bib:714`; `models/mechanistic_models.md:284`, `:287`, `:291` | Give thyroid turnover as a range with its basis: 14.4 years (13 of 148,400 follicular cells) to 8.5 years (24 of 162,700 with ambiguous cells), an assumed 10-hour S phase, nine adults aged 22-56; delete the 5-8 year note; change `exact_spearman_check.py:5`, `generate_temporal_analysis.py:100, 391`, the notebook and `tests/test_scientific_consistency.py:396` together | C p. 661-663 |
| 6 | `models/mechanistic_models.md:169`, `:338`; `docs/clinical_case_summary.md:130`; `docs/systematic_health_history.md:174` | Remove the description of the thyroid as a rapidly dividing or high-mitotic-rate gland | C p. 663 |
| 7 | `docs/clinical_case_summary.md:259`, `:252`; `docs/polyposis_differential.md:72-73` | Say negative on the panel in place of excluded; record that the physical signs were never examined (ledger P05) and that a negative test does not settle a clinical diagnosis | P p. 2, 6, 7; Rev p. 4-5 |
| 8 | `docs/pole_carrier_registry_crossref.md:151`, `:155`, `:157`; `docs/AI-Research-Assistance-Framework.md:21`; `data/clinvar_submission/README.md:51` | Remove the comparator and PPAP-patient framing; answer the non-neoplastic question (*not stated*); strike the priority claim for c.138del | Y p. 1, 2; M p. 1-2 |
| 9 | `docs/clinical_case_summary.md:371-373`; `FAQ.md:68-74`; `models/mechanistic_models.md:70`; `therapeutics/surveillance_protocol.md:7` | Mark as contradicted in direction or unsupported, citing the review's rule on loss-of-function variants | Rev p. 5, 7 |
| 10 | `docs/pole_variant_comparison.md:10` | Split the tumour cell: burden, signature and second hit were not measured for p.Asn363Lys in this family | VP p. 4, 6 |
| 11 | `docs/polyposis_differential.md:71-72` | Reword the 93% figure as polyps of any type (*outside the paper*; see the Pilarski section) | P p. 3 |
| 12 | `docs/polyposis_differential.md:56-58` | Replace the ranking of mosaic APC as commonest with the published figures and their denominators | Rev p. 4, 8, 9 |
| 13 | `docs/clinical_case_summary.md:228` | Qualify the co-occurrence sentence: no somatic POLE alteration and, per the reply, no POLE signature in that tumour | Y p. 5; M p. 1 |

**Priority 2: add data that change reasoning or planning**

| # | File and line | Addition | Source |
|---|---|---|---|
| 14 | `data/claims_ledger.tsv:54` (E08) and `:13` (V12); Models 1 and 6 in `models/mechanistic_models.md`; `docs/pole_variant_comparison.md:12` | Yamaguchi's data: the cDNA name c.4191_4192del; leukocyte DNA 1,001 of 1,987 reads (50.4%) against transcripts 827 of 1,976 (41.9%); the stable cancer with 16,687 mutations and the unstable cancer with 488,915, MLH1 promoter methylation and BRAF p.Val600Glu; no single-nucleotide or copy-number second hit at POLE; only the proband tested | Y p. 2, 5-9, 11 |
| 15 | The evidence table at `docs/VERIFICATION_AUDIT_2026-11-20.md:84-92`; a new ledger row | The reply's table (122 of 102,460 against 3 of 1,864; p 0.8571; POLE and POLD1 pooled; interval of about 0.43-4.26 as *inference*) and its tests for a PPAP variant | M p. 1-2 |
| 16 | A new ledger row; `README.md:46`; `data/lovd_update_2026-11-20.md:8`; `data/clinvar_submission/README.md` | The review's rule on loss-of-function POLE and POLD1 variants and its functional definition of an actionable variant, with the caution that haploinsufficient on Rev p. 7 refers to exonuclease-domain missense alleles | Rev p. 5, 7 |
| 17 | The tissue-prediction table at `docs/polyposis_differential.md:80-86` | Rows for MUTYH (SBS18 with SBS36), NTHL1 (SBS30), MBD4 (SBS1, or SBS96 in the Degasperi 2022 naming, which is not COSMIC's SBS96; one germline variant with a somatic second hit is possible), MSH3 (tetranucleotide instability), MLH3 (no instability, no signature), biallelic mismatch repair (ID2, ID7), colibactin by name (SBS88, ID18, APC c.835-8A>G), germline APC beyond panel reach, therapy-induced polyposis and PTEN hamartoma tumour syndrome; refine the mosaic row (two lesions, 5% or less, digital PCR); add a guard that a shared c.835-8A>G is checked in normal tissue before it is called mosaic (*inference*) | Rev p. 2, 4-8; P p. 7 |
| 18 | `data/cosmic_signatures_cited.tsv`; `analysis/mutational_signatures/README.md:19-28` | SBS18, SBS36, SBS30, SBS96 (with its name collision flagged), SBS88, ID2, ID7, ID18; restore SBS2 and SBS13; note that Yamaguchi and the reply use older signature numbering (6, 10, 14, 15, 20) | Rev p. 2, 7-8; Y p. 7; M p. 1 |
| 19 | `data/templates/lesion_table_template.tsv:1-2`; `.github/ISSUE_TEMPLATE/pole-case-report.yml` | Histology classes for ganglioneuroma, lipomatous, leiomyomatous and lymphoid polyps; result columns for microsatellite status with the panel used, each of four mismatch-repair proteins, MLH1 methylation, BRAF, raw mutation count with its denominator, spectrum and signature fit, somatic POLE and POLD1 variants, copy number and loss of heterozygosity at POLE, the germline allele fraction in tumour DNA and RNA, and drivers; an endoscopy-level field for oesophageal glycogenic acanthosis | P p. 3, 7; Y p. 3-9 |
| 20 | A new data file holding the PHTS criteria checklist; `docs/systematic_health_history.md` | The criteria table with per-item status, basis (report, owner statement, not examined), date and examiner; history items for head circumference, oral papillomas, facial papules, palmoplantar pits, lipomas and background thyroid pathology | P p. 7 |
| 21 | `data/POLE_all_methionines.tsv`; `data/POLE_downstream_methionines.tsv`; a new reference table of Kozak's measured effects | Positions −6 to −1 for every ATG; the nearest measured construct (TCCATGT is B145 and B147; A at −3 with G at +4 is B31 at 5.0; A with T is B35 at 2.6; C with G is B32 at 0.9); yield and leakiness as separate ideas; natural frequencies (about 75% of mRNAs with A at −3, about 35% with A at −3 and G at +4, under 5% with the full consensus) | K p. 285-289 |
| 22 | `docs/research_plan_2026-11.md:54-74` | Reporter additions: a ladder of 5′ UTR contexts at −3 to −1; synonymous knock-outs of the out-of-frame ATGs (c.48T>C, c.66T>C, c.69T>C); a c.138del construct with the Met44 codon changed; an engineered earlier stop as the length control (c.76del does not serve); the later length literature cited as *outside the paper* | K p. 283, 287, 289 |
| 23 | `docs/research_plan_2026-11.md:76-84` | Yamaguchi's leukocyte measurement as the benchmark, with its gaps: method undescribed, no decay inhibitor, no protein | Y p. 5 |
| 24 | `docs/research_plan_2026-11.md:108-120`; `docs/polyposis_differential.md:117-125` | Digital PCR across tissues; APC transcript analysis on the blood RNA already planned; MLPA or long-read sequencing for structural APC variants; point-variant coverage of promoter 1B and the 5′UTR; tetranucleotide instability; retrieval of two archived polyp blocks (ledger P08) | Rev p. 3-5, 7 |
| 25 | `data/tissue_replication_rates.tsv` | Columns for low and high value, metric type, method, number of subjects, age range, key assumption and source page; the adolescent value (about 167 days), nodules (45-694 × 10⁻⁵) and stromal cells (4.67 years); the endothelium row marked unsourced | C p. 661-662 |
| 26 | New rows in `data/claims_ledger.tsv`; `therapeutics/immunotherapy_strategy.md` | KEYNOTE-942 design, primary result, burden subgroups and safety from the full text; the four conditions for relevance; the five-year and phase 3 reports as abstract-only rows | W p. 632-642 |
| 27 | `docs/pole_variant_comparison.md:8-21`; `docs/polyposis_differential.md:51-53` | Carrier-level numbers for a proven exonuclease-domain pedigree (16 of 23 with colorectal cancer at a mean age of 45; 4 of 23 with glioblastoma; 3 to more than 50 polyps, from age 19; no thyroid cancer among 33 people tabulated); the note that POLE was screened across exonuclease codons only; the evidence ladder shown in the next section | VP p. 2-6 |
| 28 | `data/claims_ledger.tsv:42` (P05); `docs/systematic_health_history.md` | Record as not examined: retinal pigment lesions, café-au-lait macules, pilomatricomas, dental anomalies, desmoids, adrenal masses | Rev p. 2-4 |

**Priority 3: record-keeping**

| # | File and line | Addition | Source |
|---|---|---|---|
| 29 | `references/bibliography.bib`; `tests/test_repo_claims.py:120`; `README.md:95` | Restore `pilarski2013`, `lam2017`, `heald2010` and `richards2015` from da4df83; add the three entries printed below; use one entry count everywhere | P p. 1; Rev p. 1; M p. 1 |
| 30 | `references/bibliography.bib:704-715`, `:746-757`, `:887-898`, `:933-943`, `:102-113` | Coclet: five authors and the 8.5-14.4 year range. Kozak: the mutational test of an existing consensus. Weber: remove the five-year figure. Vande Perre: issue 2 and the authors' own wording. Yamaguchi: record the dispute | C p. 655, 663; K p. 283; W p. 632; VP p. 1; M p. 1 |
| 31 | `data/claims_ledger.tsv`, column `how_checked`, for E08, N05, D12 and D17; first rows for Kozak, Pilarski, Weber and the review | Reading depth raised to full text; four papers that have no ledger row gain one | all eight |
| 32 | `references/search_log.tsv`, to be created (`docs/EVIDENCE_PROTOCOL.md:130`) | The searches behind the `NOT_FOUND` statements in these notes: Yamaguchi's exact allele in ClinVar and gnomAD (aggregator pages only, 2026-11-21); neoantigen-vaccine studies in POLE or polyposis settings (PubMed, 2026-11-21) | n/a |
| 33 | `analysis/mutational_signatures/README.md` | A fixed definition for reporting mutation rates: counts, variant types and callable territory | Y p. 5 |
| 34 | `models/mechanistic_models.md:375` | The answered check: the 52-residue peptide contains no NPF motif (computed in the re-review) | n/a |
| 35 | `models/mechanistic_models.md:284` | A bibliography entry for the Dumont 1992 citation, or its removal | n/a |

Verified BibTeX entries for the review, the reply and the authors' response, and for the 21 other works that this report and the question list cite and the bibliography lacks, are supplied with this report as `bibliography_additions_2026-11-21.bib` (24 entries). Every field was taken from the PubMed record on 2026-11-21, and each note states the depth at which the work was read. With them the bibliography holds 113 entries, counting the four that the last commit removed.

## What changes in the reasoning about c.138del

### Model 0 gains a citable basis, on evidence narrower than its wording

Three sources now say that one loss-of-function POLE allele does not predispose to cancer: the cohort in ledger E01 (5 of 2,309 patients against 119 of 59,095 controls; odds ratio 1.08, 95% interval 0.44-2.63), the reply's table ([M p. 2](https://doi.org/10.1038/s10038-019-0701-6)) and the review's rule ([Rev p. 5](https://doi.org/10.1007/s10689-025-00460-0)). They are not three independent replications. The reply and the review share a senior author, the repository attributes the cohort to the same laboratory (`docs/pole_carrier_registry_crossref.md:147`), the review's sentence comes with citations and no counts, and the two data sets are small, with three case alleles in the reply and five carriers in the cohort (*inference*, report writer). Neither data set concerns polyposis specifically and both pool POLE with POLD1. Cohorts assembled like the N363K family, with POLE sequenced across exonuclease codons only ([VP p. 2](https://doi.org/10.1007/s10689-018-0102-6)), could not have reported an exon 2 truncation at all (*inference*), which weakens the repository's argument from the absence of an excess (`docs/polyposis_differential.md:51-53`) until each cohort's methods are read. The fair summary is the one the repository's own Step 2 already gives (`docs/polyposis_differential.md:34-37`): no risk has been shown and a moderate one is not excluded. What the full texts add is that the group which wrote the classification recommendations treats the matter as closed for clinical purposes (Rev p. 5), so any claim to the contrary now has to rest on tissue or functional data from this allele.

### The paradox becomes a checklist that c.138del has not yet been put through

The repository still frames the case as a paradox (`README.md:44-46`). The reply and the review define PPAP by a mechanism and its tumour footprint (M p. 1; Rev p. 5, 7-8), and under that definition a truncating allele poses no paradox: it fails the variant-class test, and every tumour test is unmeasured. The comparison with p.Asn363Lys shows how an accepted variant got there. It reached its label through family genetics alone, with no burden, signature, second-hit or functional data (VP p. 4, 6). For a single carrier whose parents cannot be tested that route is closed, which leaves tissue sequencing and functional work as the only ways to move c.138del in either direction (*inference*). The repository's sentence that tumour sequencing is the test (`docs/pole_variant_comparison.md:21`) is right for a singleton and does not describe how N363K was accepted.

| Evidence type | p.Asn363Lys (VP) | Yamaguchi's c.4191_4192del, as the reply judges it | c.138del today |
|---|---|---|---|
| Variant class | Missense in the exonuclease domain (VP p. 1) | Frameshift outside the domain; fails (M p. 1-2) | Frameshift in exon 2; fails; no outcome of the allele lacks proofreading (audit section 3) |
| Unrelated families with the phenotype | 2 families, 23 carriers (VP p. 1) | One patient (Y p. 2) | One carrier with a described phenotype; three ClinVar submissions and two gnomAD alleles without phenotype; no publication (D01, D04, D05, D11) |
| Segregation | 11 carriers over three generations; no formal statistic (VP p. 2-4) | None; only the proband tested (Y p. 11; M p. 1) | None; parents cannot be tested and siblings are untested (P07) |
| Tumour microsatellite and mismatch-repair status | Stable, proteins retained, one isolated MSH6 loss (VP p. 2) | One stable cancer; one unstable through MLH1 methylation (Y p. 5-9) | Not done (P02) |
| Tumour mutation burden | Not performed (VP p. 4) | 2.8 and 81.5 per 10⁶ bases; fails the test of more than 100 per megabase (Y p. 5; M p. 1) | `NOT_MEASURED` (P01) |
| Spectrum and signatures | Not done; *not stated* in the paper | Signatures 6 and 15 above 80%, none of 10 or 14, per the reply's reading of the supplement (M p. 1); the main text is silent (Y p. 7) | `NOT_MEASURED` (P02) |
| Second hit at POLE | Not done (VP p. 6) | None by single-nucleotide variant or copy number in two cancers; copy-neutral loss not addressed (Y p. 5) | Not measured |
| RNA, protein, function | None in the paper; functional testing is named as future work (VP p. 6) | Leukocyte transcripts 41.9% against DNA 50.4% (Y p. 5); no protein | None; decay and restart are `INFERENCE` (V11, V12) |
| Class enriched in patients over controls | *Not stated* | No: 0.16% against 0.12%, p = 0.8571 (M p. 2) | No (E01) |
| Population frequency | *Not stated* | No population database mentioned (Y p. 5) | Present in gnomAD (D04, D05) |
| Resulting label | Pathogenic, without stated criteria (VP p. 3) | At most uncertain significance for PPAP (M p. 1) | Conflicting in ClinVar (D01) |

### Restart at Met66 is several questions, and the cited paper answers none of them

On the fate of the allele the papers sharpen the question more than they answer it. Kozak 1986 supports the ranking of POLE's start codons and the plausibility of bypass. It cannot carry the Met66 claim, because its restart experiment used a five-codon minicistron and the paper is silent on ORF length ([K p. 287, 289](https://doi.org/10.1016/0092-8674(86)90762-2)). Three points are new. The annotated start is sub-optimal but was measured above the floor (K p. 285, 287), so how much scanning leaks past it is an open quantity and not a given. Between it and Met44 stand three out-of-frame ATGs, one of them in the best context the paper measured, which act as barriers and whose ORFs overlap Met44 (*inference*). And on the mutant mRNA five upstream ORFs precede Met66, of **52, 34, 28, 27 and 9 codons** (ledger V10). The literature the Kozak notes cite, *outside the paper*, says restart falls as the upstream ORF lengthens, so on length alone the routes it favours are the shorter ones, above all the nine-codon ORF opened at Met44, and not the 52-codon ORF opened at the annotated start; how many ribosomes take each route is a separate unknown (*inference*, report writer). The planned reporter panel separates these routes only if a c.138del construct with the Met44 codon changed is added, and the ledger's wording that the geometry lies inside a published range (`data/claims_ledger.tsv:12`) rests on an abstract that has not been set against the upstream-ORF literature in full text.

On decay, Yamaguchi supplies the only published measurement for a germline POLE truncation, and it cuts against assumption: a mid-gene stop, where position predicts decay, left the mutant transcript at about 71% of the wild-type level in leukocytes ([Y p. 5](https://doi.org/10.1038/s10038-019-0611-7); *inference*). One person and an undescribed method make this weak evidence, yet it is enough to show that the null-allele rows of the audit's table of outcomes (`docs/VERIFICATION_AUDIT_2026-11-20.md:69-73`) cannot be assumed for c.138del, whose decay is borderline by rule (ledger V12). The measurement in the research plan (`docs/research_plan_2026-11.md:76-84`) is the same design with the inhibitor control that Yamaguchi lacks.

### A hypermutated lesion would have to clear two alternatives before POLE is credited

Published tumours from carriers of POLE loss-of-function alleles number more than the repository's comparison table records: the breast tumours of ledger E02 (1.09-1.70 mutations per megabase, no POLE signature), Yamaguchi's two colon cancers, and the endometrial cancer of ledger E19 with its somatic exonuclease-domain mutation. Yamaguchi's pair shows what could go wrong in reading this carrier's own tissue. One tumour was hypermutated, and the cause was MLH1 methylation, not POLE (Y p. 5-9; M p. 1). A high count in any lesion of this carrier would therefore have to clear mismatch-repair loss first and a somatic or mosaic exonuclease-domain variant second, since the review expects mosaicism in polyposis genes beyond APC (Rev p. 4), before c.138del could be credited. An isolated loss of one mismatch-repair protein, as in one N363K polyp (VP p. 2), would also need careful reading. The repository's first criterion for a finding (`docs/polyposis_differential.md:103`) needs those guards written into it.

### Histology is the gate for the polyps, and the thyroid tumour points away from POLE

For the cause of the polyps nothing can be applied until the lesions are typed. The review covers adenomatous polyposis only and says that adenomas of every genetic cause look alike (Rev p. 2, 6); the PTEN criteria count hamartomas and exclude hyperplastic polyps ([P p. 7](https://doi.org/10.1093/jnci/djt277)). Until the roughly 20 lesions are classified, the repository's label of adenomatous polyposis and its listing of Cowden syndrome as excluded both run ahead of the evidence. If the polyps are adenomas, the review turns the differential into checkable predictions: a shared APC variant in two lesions for mosaicism, c.835-8A>G with SBS88 and ID18 for colibactin, a named signature for each repair defect, germline sequencing for MLH3, which leaves no tissue mark, and second-hit analysis if a single MBD4 variant turns up (Rev p. 4-8). Ledger P08 records archived polyp blocks at several institutions, so the review's two-lesion test for mosaic APC need not wait for an endoscopy more than a year away (*inference*).

The thyroid carcinoma now points away from POLE on three grounds. It arose in a tissue whose adult cells divide about five times ([C p. 655, 663](https://doi.org/10.1111/j.1365-2265.1989.tb01290.x)), the opposite of the rapidly dividing gland the models describe. No thyroid cancer appears among the 33 tabulated members of the N363K families (VP p. 3-4), and the review does not list thyroid among PPAP cancers (Rev p. 3). And the two frames in which a thyroid tumour does belong are the alternatives: the cribriform-morular type under APC (Rev p. 2), and papillary carcinoma as a minor PTEN criterion, with the paper's caveat that some such diagnoses are incidental (P p. 6, 7). The stain and BRAF test that the repository already poses as a question for the care team (`docs/polyposis_differential.md:131`) are the smallest step that discriminates.

### The two citations that carried clinical weight do not carry it

The authors of the N363K report doubt the value of the brain imaging for which they are cited (VP p. 1, 6). KEYNOTE-942 enrolled only resected melanoma, tested its product only with pembrolizumab and found no larger benefit at higher burden ([W p. 634, 638, 641](https://doi.org/10.1016/S0140-6736(23)02268-7)). The review holds that a loss-of-function POLE variant found without congenital disease should not enter clinical decisions (Rev p. 5). These are statements of evidence. What follows from them for this carrier is a set of questions for the care team, gathered in the last group of the next section. The phenotype itself, about 20 polyps with high-grade dysplasia reported, remains clinically important whatever the POLE result means (`docs/VERIFICATION_AUDIT_2026-11-20.md:100-103`; `docs/polyposis_differential.md:129`).

Taken together, the eight papers move the repository's centre of gravity. The open questions are no longer about explaining a paradox. They are measurement questions with pass-or-fail criteria supplied by the literature, and the cheapest ones (documents, stains, one blood draw, one database page) come first. What stays open and scientifically interesting is narrower and better defined than before: whether start-proximal POLE truncations are nulls or hypomorphs, which matters for the recessive disorders where the review places loss-of-function alleles (Rev p. 5), and what one carrier's tissue shows when it is finally measured. The one implication the repository calls firm, carrier status for a recessive POLE-deficiency allele (`docs/polyposis_differential.md:133`), is also the place where the null-or-hypomorph answer would matter in practice, because an allele rescued by restart would be milder than a true null (`docs/pole_variant_comparison.md:65-69`).

## Research questions to lift into docs/research_questions.md

The text between the two markers below is self-contained and can be copied into the repository as `docs/research_questions.md`, with its headings moved up one level. It repeats the source key so that it can stand alone, and it paraphrases every source.

<!-- BEGIN docs/research_questions.md -->

### Research questions for POLE c.138del and the early POLE truncations

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

#### The most decisive questions, in order

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

#### 1. Fate of the allele and translation restart

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

#### 2. Tumour and tissue evidence

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

#### 3. Cause of the polyps

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

#### 4. This carrier's phenotype

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

#### 5. The class of early truncations, population and family

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

#### 6. Classification and reporting

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

#### 7. Therapy and surveillance claims: evidence and questions for the care team

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

<!-- END docs/research_questions.md -->

## What was not read and what could not be verified

**The papers.** All eight main texts were read in full for the notes, but several supporting pieces were out of reach. For Kozak 1986, three figures print no values, so the entries for the barrier and reinitiation mutants without a stated fold-change are band-intensity impressions; the later Kozak papers, Luukkonen 1995, the quantitative context study and the ribosome-profiling and proteomics papers were read as abstracts only, Kozak 2001 and 2002 were read in part through PubMed Central (the 2001 figures through a web fetch of that page, not from the publisher's PDF), and no experimental data on POLE translation were located, so every statement about POLE start-codon use remains inference from sequence. For Coclet 1989, three printed values look like misprints and are reported as printed, the origin of two of the ten subjects is *not stated*, and the Dumont review and the Ki-67 autopsy study were not read beyond an abstract. For Pilarski 2013, the final typeset version was not seen, the current NCCN wording was not opened, Heald 2010 was read as an abstract and the 2025 consensus guideline was keyword-searched only. For Vande Perre 2019, the supplementary material was unavailable and the later cell-line study was read as an abstract. For the review, its references 19-25, 73-78, 130 and 131 were not read, nor were the 2026 mosaicism papers behind ledger rows E13 and E15. For Yamaguchi 2019, the whole supplement was unavailable (the download was refused), so the evidence that the unstable tumour lacks a polymerase signature rests on the reply's description of one supplementary figure; the authors' response was read only as a publisher's preview through a fetch tool; ClinVar and gnomAD were not queried directly for that allele; and Smith 2013, Rosa 2020 and the full text of Mur 2020 were not read beyond the points noted. For Weber 2024, the supplementary appendix (full eligibility, tissue requirements, subgroups by BRAF and stage, interaction tests) and the linked Comment were not supplied; the full texts of the five-year report and of the phase 3 trial were not read; the product's regulatory status is undetermined; the trial registry was not queried; and the figures taken from news pages came through a tool that returns a summary and should be re-checked against the journal articles before the repository relies on them.

**The repository.** The 14 live tests were not run, so the SpliceAI, gnomAD, ClinVar, LOVD and PubMed statements were *not verified* on 2026-11-21. It is not known whether GitHub Actions ran on 59a82b3, whether the patch for the companion viewer was applied, or whether the public LOVD entry has been corrected. Image files were not viewed, the two removed Office files and the removed `CLAUDE.md` were not read, and the re-review could not tell which additions were written by the owner and which by a second pass of the auditor. The re-review compared the repository with itself for the drifting numbers it lists and verified no external figure such as a trial result or a prevalence.

**The carrier.** No clinical document has been seen by the auditor, by the note-takers or by the report writer: not the laboratory report, the alignment files, or any pathology, endoscopy, imaging or operative report. Every feature of the carrier in this report is an owner statement, and the comparison with the PTEN criteria inherits that limit and is for the care team to check.

**This report.** It was assembled from the six sets of notes. The report writer's own checks were limited to re-reading cited repository lines at HEAD, confirming the static causes of the failing tests, recomputing the reading frames from the repository's fixture, and locating the eight short quotations and a handful of headline numbers in the extracted paper texts. The test suite and the repository's scripts were not re-run, the papers were not re-read in full, and no web or database look-up was made, so every item marked *outside the paper* is carried over as the notes recorded it on 2026-11-21. Two readings marked as the report writer's inference are new here and have not been reviewed by anyone else: that the three published statements against a risk from loss-of-function alleles are not independent of one another, and that the restart question divides across five upstream ORFs of different lengths. A third point, that c.76del cannot serve as a length control, rests on the repository's own line and on the same recomputation.

## Checks made after the report was written

These checks were run on 2026-11-21 against the finished report, on exports of the repository outside the working copy, on the extracted paper texts and page images, and on PubMed. They add no new claims about the carrier.

**The test results reproduce, and the repair is narrower than ten failures suggests.** `python3 -m pytest -q` on an export of HEAD (59a82b3) gave 10 failed, 42 passed, 14 skipped; on an export of da4df83 it gave 52 passed, 14 skipped. A third run, with every file taken from da4df83 and only `README.md` taken from HEAD, gave **2 failed, 50 passed, 14 skipped**. The two remaining failures are `test_readme_figures_exist` and `test_identifiers_quoted_in_documents_match_the_derivation`, which fail because the shortened README no longer embeds the figures or prints the genomic identifiers. Restoring the 35 non-README files that c3ccb31 changed to their da4df83 versions therefore clears eight of the ten failures; the last two need either a short figure index and one identifier line in the README, or a change to those two tests. Restoring those files also makes two README statements true again that are false at HEAD: the SpliceAI result at `README.md:61` (ledger V13 returns to `VERIFIED`) and the count of 89 bibliography entries at `README.md:95`.

**Fourteen of the 36 files changed by c3ccb31 are byte-identical to the audit overlay of 2026-11-20.** They are `data/phenotype_hpo.tsv`, `docs/EVIDENCE_PROTOCOL.md`, `.github/workflows/verify.yml`, `analysis/figures/make_figures.py`, and the PNG and SVG of five figures (`c138del_codons`, `c138del_translation_map`, `pole_exon1-2_truncations`, `lof_evidence`, `clinical_timeline`). Those five SVGs carry a build time of 2026-11-20T21:36 at HEAD against 2026-11-21T13:02 at da4df83; `claims_ledger_status.svg` and the three SVGs in `analysis/temporal_phenotype/` carry 2026-11-21T11:14-11:20. The pattern fits an older working copy, or the overlay archive itself, being laid over the newer tree (*inference*).

**Figures in the report were checked against the sources.** Located in the extracted texts: the KEYNOTE-942 hazard ratios and intervals (0.561, 0.347, 0.652, 0.586), the 79 and 30 patients with high burden that sum to 109 of 154, the one-sided alpha, the registration number and the wording on burden (W); the reply's table (122 of 102,460; 3 of 1,864; p 0.8571) and its conclusion (M); the allele name, the read counts 1,001 of 1,987 and 827 of 1,976, the mutation counts 488,915 and 16,687, and the sentence on a second hit at POLE (Y); the review's passage on loss-of-function variants, the one-third unexplained, the colibactin hotspot with its figure of about 30%, the signature names and its references 1 and 12 (Rev); 16 of 23 and 4 of 23, the sentence on brain imaging, and the two codon ranges as printed (VP); the operational rules for a diagnosis, the 58 cm threshold, the polyp-type percentages and 44 of 48 (P); 13 of 148,400, 24 of 162,700, 14.4 years and 8.5 years as the minimal estimate, and the 21% of stromal cells (C). For Kozak 1986 the page images of journal pages 285 and 287 were viewed: Table 1 and Figure 5 show mutants B145 and B147 with T at −3, C at −2 and −1 and T at +4, the same seven bases as the POLE start context TCCATGT, and the text gives the at-least-four-fold comparison of B145 with B140. Nothing checked disagreed with the report.

**Recomputed from the repository's fixtures.** The contexts at c.47, c.65, c.68, c.130 and c.196; the synonymous changes c.48T>C, c.66T>C and c.69T>C (each GAT to GAC, Asp to Asp); 91.7% GC over c.11-c.46; the 52-codon reading frame of c.76del, identical to that of c.138del; for Yamaguchi's allele, a stop at codon 1398 for both c.4191_4192del and c.4193_4194del, 1,397 of 2,286 residues (61.1%) retained, and 2,553 nt from the stop to the last exon junction at c.6747. The ClinVar snapshot row for c.141del (`data/reference/POLE_clinvar_PLP_2026-11-21.tsv:489`) reads as the report describes it.

**Re-checked on PubMed.** According to PubMed, the five-year report of KEYNOTE-942 is Khattak et al., *J Clin Oncol* 2026;44(26):2482-2489, PMID 42223134, with hazard ratios of 0.510 (95% CI 0.294-0.887) for recurrence-free survival, 0.411 (0.200-0.843) for distant metastasis-free survival and 0.471 (0.165-1.345) for overall survival, all analyses descriptive ([doi:10.1200/JCO-26-00835](https://doi.org/10.1200/JCO-26-00835)). According to PubMed, the phase 3 trial is Long et al., *N Engl J Med*, published 11 November 2026, PMID 43013837: 1,137 patients, recurrence-free survival at 24 months 82.2% against 70.0% (two-sided P<0.001), with a piecewise hazard ratio of 0.99 (95% CI 0.66-1.49) before 6 months and 0.42 (0.30-0.58) after ([doi:10.1056/NEJMoa2609762](https://doi.org/10.1056/NEJMoa2609762)); the abstract reports no subgroup by mutational burden. According to PubMed, the three proposed bibliography entries match their records in authors, title, journal, volume, issue, pages and identifiers: the reply ([doi:10.1038/s10038-019-0701-6](https://doi.org/10.1038/s10038-019-0701-6)), the authors' response ([doi:10.1038/s10038-020-0752-8](https://doi.org/10.1038/s10038-020-0752-8)) and the review ([doi:10.1007/s10689-025-00460-0](https://doi.org/10.1007/s10689-025-00460-0)).

**A signature name that means two things.** The review ties MBD4 deficiency to SBS1 or to a closely similar signature that it calls SBS96, and cites its references 35 and 114 for this (Rev p. 7); reference 114 is the 2022 signature survey by Degasperi and colleagues. COSMIC's page for the signature it calls SBS96 gives the cause as unknown and says the signature entered COSMIC from that survey under a different number, 141 in that survey's own series ([COSMIC SBS96](https://cancer.sanger.ac.uk/signatures/sbs/sbs96/), Mutational Signatures v3.6, read on 2026-11-21 through a tool that returns a summary). According to PubMed, a 2024 study of MBD4-deficient tumours describes them by SBS1 and a rare SBS96 fitted from the Degasperi reference set ([doi:10.1038/s41467-024-54223-z](https://doi.org/10.1038/s41467-024-54223-z); abstract and figure legends read), and the survey itself is [doi:10.1126/science.abl9283](https://doi.org/10.1126/science.abl9283) (abstract read). The two uses of the name therefore appear to point at different signatures (*inference*; the COSMIC page should be read directly before the repository relies on this). The consequence is practical and belongs with RQ3.3: a fit meant to detect MBD4 deficiency has to use the Degasperi reference set, or SBS1 with the review's criterion of more than 60% of substitutions at methylated CpG sites, because a COSMIC-only fit would look for a different profile. The other four signatures were read on COSMIC the same day and match the review's use of them: SBS18 (possibly oxidative damage), SBS36 (failure of base excision repair with MUTYH mutations), SBS30 (the same with NTHL1 mutations) and SBS88 (E. coli that produce colibactin, associated with ID18).

**Nineteen more PubMed records were checked while the bibliography entries were built.** Each of the works that this report cites and the bibliography lacks was looked up by DOI or PMID, and its entry was written from the record. According to PubMed, the abstracts confirm the points this report takes from five of them: a hairpin of −50 kcal/mol cut proinsulin yield by 85-95% ([doi:10.1073/pnas.83.9.2850](https://doi.org/10.1073/pnas.83.9.2850)); inhibition of a downstream ORF grew with the length of the upstream one, and an upstream ORF of 84 nucleotides was predicted to stop half of the ribosomes from reinitiating ([doi:10.1128/JVI.69.7.4086-4094.1995](https://doi.org/10.1128/JVI.69.7.4086-4094.1995)); initiation moved progressively to the second AUG as the cap-to-AUG distance fell from 32 to 3 nucleotides, an effect that secondary structure downstream of the first AUG offset (PMID 1820208); Ki-67 was scored in 117 autopsy thyroids ([doi:10.1210/jc.2006-0417](https://doi.org/10.1210/jc.2006-0417)); and 65,536 start-site contexts from −6 to +5 were measured ([doi:10.15252/msb.20145136](https://doi.org/10.15252/msb.20145136)). Two of these details bear on the restart questions and are new here. Eighty-four nucleotides is 28 codons, the length of the frame that opens at c.65 on the c.138del mRNA, so by that one viral system the 27- and 28-codon frames would lose about half of their ribosomes and the 9-codon frame opened at Met44 far fewer (*inference*; a different mRNA and a different restart distance). And both features of the 1991 experiment are present in POLE: an annotated leader of 27 nucleotides, which sits near the long end of the range that experiment tested and may not be the true distance from the cap, and a GC-rich stretch just downstream of the first AUG. The two act in opposite directions, so neither can be used alone to predict how leaky the annotated start is (*inference*).

**The two documents and the repository's own guard tests.** This report and the question list cite 24 works and name five signatures that the repository does not catalogue, so adding the two documents alone would trip its tests for uncatalogued identifiers and signatures. The companion files supply what those tests need: the bibliography of da4df83 with 24 entries appended (113 in all, which also restores the four that the last commit removed), `data/cosmic_signatures_cited.tsv` with five rows added (the SBS96 row carries the name collision), `data/checksums.sha256` with the one changed hash, and the entry count pinned at `tests/test_repo_claims.py:120`. On an export of da4df83 with those files and the two documents in `docs/`, the suite gave **52 passed, 14 skipped**; with HEAD's shortened README put in place of the long one it gave 2 failed, 50 passed, 14 skipped, the same two README-dependent tests as above. Laid over HEAD as it stands, with nothing restored, the same files gave 7 failed, 45 passed, 14 skipped: three failures fewer than HEAD alone and none added. The 14 live tests need a network and were not run; the new entries follow the field layout those tests parse.

**Not re-checked.** The other items marked *outside the paper*, the per-line repository findings beyond the sixteen lines sampled, the unnumbered readings of Kozak's Figures 5 to 7, and everything that depends on a document about the carrier.
