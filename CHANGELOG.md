# Changelog

All notable updates to the POLE c.138del Research Framework will be documented in this file.

---

## [0.5.5] ; 2026-04-25

### Changed (Evidence Status Revision ; Confirmed Findings & Pending Tumour Data)

**Claims now confirmed (strengthened with documentation):**

- **Orthogonal confirmation status updated** from "Pending" to "Confirmed" across `README.md`, `CLAUDE.md`, `data/clinvar_submission/README.md`: Variant confirmed by accredited clinical germline testing with orthogonal confirmation on an independent assay
- **Germline status made explicit** across `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `FAQ.md`, `data/clinvar_submission/README.md`: New "Germline status" row/field confirming heterozygous call from blood/saliva-derived DNA on germline-specific assay. Previously implicit throughout; now explicitly stated as constitutional variant, not tumor-derived
- **gnomAD date-stamped** to v4.1.0 (accessed April 2026) across `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `FAQ.md`, `data/clinvar_submission/README.md`

**Claims softened pending tumour data:**

- **TMB documentation caveat strengthened** across `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `FAQ.md`: Clarified that the germline report does not address TMB; tumour sequencing methodology details (assay platform, exact mut/Mb, numerator/denominator, synonymous/indel inclusion, tumour-only vs tumour-normal status) are pending documentation from a separate tumour NGS report
- **Differential Diagnosis subsection added** to `docs/clinical_case_summary.md`: New section covering MMR IHC (MLH1/MSH2/MSH6/PMS2), MSI status, MLH1 promoter methylation, and germline panel results for Lynch syndrome/MUTYH/NTHL1. Status table shows all MMR/MSI tests as pending. Cross-referenced from `README.md` MSI status row and FAQ
- **Mutational signature section reframed** in `README.md` and `analysis/mutational_signatures/README.md`: Added prominent status callout noting signature decomposition has NOT been performed; flagged as the single most diagnostic readout available and the highest-priority immediate analysis, not a hypothetical exercise
- **Research Prioritization Timeline reordered** in `README.md`: MMR IHC/MSI/MLH1 methylation elevated to item #1 (prerequisite differential diagnosis); mutational signatures emphasized as item #3

**Mechanism-agnostic clinical call framing:**

- **Pathogenicity classification framing added** across `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `data/clinvar_submission/README.md`: Explicitly states the Pathogenic classification rests on standard ACMG criteria for null variants (PM2 + PP4), not on observed phenotype-genotype correlation. Notes the lab explicitly reports the variant has not been previously reported in POLE-related conditions. Frames that the clinical pathogenicity call and the mechanistic novelty answer different questions, and both can be true simultaneously

**Technical corrections:**

- **Coordinate system note added** across `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `data/clinvar_submission/README.md`: GRCh37 coordinate (chr12:133249847, from clinical report) provided alongside existing GRCh38 coordinates (chr12:132681203–132681204). All repository coordinates default to GRCh38 unless otherwise noted. Users directed to UCSC LiftOver or Ensembl CrossMap for conversion

---

## [0.5.4] ; 2026-04-19

### Changed (Comprehensive Audit ; Scientific Accuracy Corrections)

- **CRITICAL: CDK4/6 inhibitor mechanism corrected** across `README.md` and `therapeutics/synthetic_lethality.md`: CDK4/6 inhibitors enforce G1 arrest (not "force S-phase entry"). Rationale rewritten: POLE-deficient clones that have lost G1 checkpoint control (via p53/Rb inactivation) may be selectively sensitive to restored G1 arrest
- **CRITICAL: Albertson et al. (2009) mouse data corrected** in `README.md` and `references/bibliography.bib`: Heterozygous proofreading-dead mice showed ~15x elevated mutation rate (not "indistinguishable from WT"). Homozygous mutation rate corrected from ">70x" to "~65x". Interpretation updated: heterozygous data supports Model 4 (measurable haploinsufficiency) while still requiring LOH for full cancer phenotype
- **"188 LoF carriers" → "188 LoF variants"** across all files: gnomAD reports 188 observed LoF *variants*, not 188 individual *carriers* (different quantities). Corrected in `README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `models/mechanistic_models.md`, `data/phenopacket/pole_c138del_phenopacket.json`, `data/clinvar_submission/README.md`, `docs/AI-Research-Assistance-Framework.md`
- **Anglesio et al. (2017) statistic corrected** in `README.md` and `therapeutics/surveillance_protocol.md`: 79% of *patients* with deep infiltrating endometriosis harbored somatic mutations in at least one lesion, not 79% of *lesions*; 26% of individual lesions had driver mutations
- **"Indistinguishable from classical PPAP" → "clinically consistent with PPAP"** in `README.md` header tagline and line 17, and `CLAUDE.md`: Overstated when TMB assay platform is unconfirmed and SBS10a/b signatures are pending; "(molecular confirmation pending)" added
- **Bass citation corrected** from "Bass & Redwine, 2010" to "Bass et al., 2000" across `docs/clinical_case_summary.md`, `README.md`, and `models/mechanistic_models.md`
- **Andrianova et al. (2024) precision improved** in `README.md`: Explicitly noted study demonstrated recessive model for *POLD1* (not POLE); added "(demonstrated for POLD1; the principle may extend to POLE)"
- **Adavosertib (AZD1775) discontinued** in `README.md` and `therapeutics/synthetic_lethality.md`: Updated to next-generation WEE1 inhibitors (azenosertib/ZN-c3, Debio 0123) with note on improved therapeutic windows
- **Tebentafusp specificity noted** in `therapeutics/immunotherapy_strategy.md`: Clarified that tebentafusp is specific to gp100/HLA-A*02:01 melanoma; listed as platform concept for future neoantigen-directed bispecifics
- **Domain boundary TSV corrected** (`data/POLE_domain_boundaries.tsv`): C-terminal region start changed from 1189 to 1190 (eliminates overlap with Polymerase domain end); source attribution corrected from "Liu & Linn 2000" to "Korona et al. 2011 JBC; Liu & Linn 2000 NAR (domain architecture)"
- **"Three critical observations" → "four"** in `docs/clinical_case_summary.md`: Count corrected to match the four numbered observations listed
- **Broken cross-reference fixed** in `docs/clinical_case_summary.md`: `../models/comorbidity_interaction_analysis.md` → `comorbidity_interaction_analysis.md` (file is in same directory)
- **SHA-256 checksums regenerated** (`data/checksums.sha256`): Updated for all data files modified in v0.5.3 and v0.5.4

---

## [0.5.3] ; 2026-04-19

### Added

- **"Endometriosis × POLE Intersection" section** in `README.md`: Dedicated section covering the testable prediction that germline POLE proofreading deficiency should elevate somatic mutation burden (and SBS10a/b signatures) in endometriotic epithelium above baseline ARID1A/KRAS/PIK3CA rates; why this case is informative (Stage IV+ with trans-diaphragmatic extension); tissue collection opportunity at upcoming surgery
- **"POLE Domain Architecture & Biochemistry" reference section** in `README.md`: Liu & Linn 2000, Korona et al. 2011, Henninger & Pursell 2014, Kane & Shcherbakova 2014, Barbari & Shcherbakova 2019
- **6 new bibliography entries** in `references/bibliography.bib`: Liu 2000 (domain architecture), Korona 2011 (140 kDa fragment), Henninger 2014 (review), Kane 2014 (50-fold mutator), Barbari 2019 (no LOH in ExoD tumors), Folletet 2025 (POLD1 duodenal adenocarcinomas)
- **50-fold mutator effect** in Classical PPAP Mechanism section: pol2-P301R vs pol2-4 comparison (Kane & Shcherbakova 2014; Parkash et al. 2019); explicitly surfaces that canonical ExoD drivers operate without LOH (Barbari & Shcherbakova 2019)
- **Mouse knockout citation** added: homozygous *Pole* knockout lethal at E7 (MGI:1196391); hemizygous P286R/null essentially embryonic lethal (Barbari & Shcherbakova 2019)
- **Banked tissue status** clarified in Research Prioritization Timeline: FFPE thyroidectomy and hysterectomy specimens archived; fresh-frozen tissue not currently banked; upcoming surgery as prospective collection opportunity

### Changed

- **Domain coordinates corrected and sourced** across all files (`README.md`, `CLAUDE.md`, `docs/clinical_case_summary.md`, `models/mechanistic_models.md`, `data/POLE_domain_boundaries.tsv`, `analysis/variant_landscape/generate_pole_lollipop.py`): Polymerase domain 580–1260 (unsourced) → polymerase core ~530–1189 (Korona et al. 2011, 140 kDa catalytic fragment). Exonuclease active site 268–471 retained with citation (Church et al. 2013). Broader ExoD region 223–517 noted (Atlas of Genetics). Domain convention notes and source citations added to ASCII diagram
- **"p261" clarified** in domain diagrams: "POLE Catalytic Subunit (p261)" → "(p261; 2,286 aa, 261 kDa)" to avoid confusion between molecular weight and residue count
- **Frontiers in Oncology 2025 POLD1 citation completed**: Added first author (Folletet A), volume (15), article number (1727289), and DOI in `README.md` and `therapeutics/surveillance_protocol.md`

---

## [0.5.2] ; 2026-04-19

### Added

- **"Variant Verification & Methodology" section** in `README.md`: New section surfacing sequencing method, orthogonal confirmation status, TMB methodology status, MSI status, gnomAD query details, patient demographics, family history summary, and consent/IRB status ; enabling external PIs to assess variant authenticity and data strength without reading the full clinical case summary
- **Explicit n-of-1 framing** in `README.md` Overview: Callout box acknowledging this is a single-patient hypothesis-generating framework seeking collaborators for validation in additional carriers
- **gnomAD v4 query links** added to `README.md` (Overview + "What We Know" table) and `docs/clinical_case_summary.md` with genomic coordinates (GRCh38 chr12:132681203–132681204)
- **Therapeutic strategy clinical context caveat** in `README.md`: Clarifies that the patient has no active advanced malignancy; therapeutic section is prospective contingency planning, not current treatment recommendations; synthetic lethality targets require preclinical validation in POLE-null models

### Changed

- **TOC updated** in `README.md` to include new Variant Verification section

---

## [0.5.1] ; 2026-04-18

### Added

- **POLE-null vs. POLE-mutant distinction** in `therapeutics/synthetic_lethality.md`: New section explaining that all published synthetic lethality data derives from POLE-ExoD-*mutant* cells, not POLE-*null* (LOH-driven) cells ; a critical gap for translating findings to this patient's tumors. Includes comparison table, evidence gap analysis, and required CRISPR knockout experiments
- **POLE-null synthetic lethality validation** added to Data Needed section in `synthetic_lethality.md`
- **Two bibliography entries** in `references/bibliography.bib`: Tan et al. (2025) *Nucleic Acids Research* (cell-type-dependent NMD, PMID 40366162) and Palou-Márquez & Supek (2025) *Genome Biology* (variable NMD across tissues/individuals, PMID 41023738) ; both previously cited in `mechanistic_models.md` but missing from bibliography
- **AAAAI/EAACI caveat** added to food-specific IgG section in `docs/clinical_case_summary.md`: Blockquote noting that AAAAI recommends against food-specific IgG testing for diagnosis; data retained for pattern documentation only; cross-reference to validated permeability assays

### Changed

- **Food-specific IgG note strengthened** in `docs/clinical_case_summary.md`: End-of-section caveat updated to reference AAAAI/EAACI position statement; antigen count corrected from "19+" to "17" (actual count from table)
- **Leading theory date fixed** in `README.md`: "Updated 2026-04-16" → "Updated 2026-04-17" (consistent with v0.5.0 release date)
- **Phenotype heading clarified** in `CLAUDE.md`: "Five Categories + Comorbidity Context" → "Five Phenotype Categories + Supplementary Context"

---

## [0.5.0] ; 2026-04-17

### Changed (Scientific Database Verification & Literature Update)

- **CRITICAL: gnomAD constraint metrics corrected.** Previous values (pLI = 0.98, LOEUF = 0.22) were incorrect. Verified against gnomAD v4 API (GRCh38, ENST00000320574): pLI ≈ 0 (1.1×10⁻⁴⁰), LOEUF = 0.76, oe_lof = 0.67 (188 observed / 279 expected LoF variants). POLE tolerates heterozygous LoF ; 188 carriers in gnomAD lack apparent PPAP. Corrected across all files
- **PVS1 argument strengthened by gnomAD data:** Gene-level LoF tolerance (pLI ≈ 0) provides additional evidence against PVS1 applicability
- **Mechanistic model implications updated:** gnomAD LoF tolerance supports LOH/second-hit model for tumor-specific ultra-hypermutation; Bayesian priors revised (M1 raised to 30%, M4+M1 combination ~40%)
- **Literature consensus acknowledgment added:** Prominent note in README that current scientific consensus does NOT support truncating POLE variants as pathogenic for PPAP; this framework investigates a novel hypothesis

### Added

- **Ambrosini et al. (2024) *Annals of Oncology*:** POLE/D1pd mCRC 89% ORR on ICI vs 54% dMMR/MSI-H (P=0.01)
- **Andrianova et al. (2024) *Eur J Hum Genet*:** Heterozygous POLD1 ExoD → ~15% mutation rate increase; cancer requires LOH (recessive model)
- **Nous-209 vaccine:** Leoni et al. (2026) *Nature Medicine* ; 100% immune response in Lynch carriers (37/37)
- **mRNA-4157/V940:** Weber et al. (2024) *Lancet* + 5-year data (49% recurrence reduction, press release Jan 2026)
- **Wang et al. (2025) *PNAS*:** First cryo-EM proofreading intermediates of human Pol epsilon-PCNA
- **Keskitalo et al. (2025) *Nature Communications*:** POLE2 is NPF motif receptor
- **N363K glioblastoma:** Vande Perre et al. (2019) + Labrousse et al. (2023) *NAR Cancer* ; extends PPAP spectrum
- **Tissue-specific NMD:** Kolakada et al. (2025) *Cell Genomics* ; peptide release rate modulates NMD
- **SMaHT benchmarking:** Zhang et al. (2025) bioRxiv ; 6 duplex methods compared; ppmSeq 44% recovery
- **Research gaps section** added to surveillance protocol (synthetic lethality in POLE-null, thyroid, endometriosis, AMA, preventive ICI)
- **13 new bibliography entries** in references/bibliography.bib

---

## [0.4.0] ; 2026-04-17

### Changed (Peer Review Feedback)

- **ACMG classification clarified:** Variant is Pathogenic per clinical laboratory. PVS1 applicability discussed as research nuance (mechanism does not match canonical dominant-negative model); independent ACMG evidence: PM2 + PP4; Mur et al. (2023) POLE-specific framework does not cover this variant type
- **"Unambiguous PPAP" → "clinically consistent with PPAP"** throughout (molecular confirmation via SBS10a/b/28 pending)
- **TMB sourcing qualified:** All TMB >100 mut/Mb references now marked as "reported" with assay platform and source specimen pending clarification
- **Thyroid carcinoma corrected:** 0.6 cm microcarcinoma → 1.2 cm carcinoma, isthmus; T1a → T1b; "microcarcinoma" removed throughout
- **Model 6 prior raised:** 15% → 20% (mechanistically straightforward); M5 reduced 10% → 5% to rebalance
- **Family history modulated:** Added population base rates (uterine ~3%, breast ~12% lifetime) to contextualize maternal grandmother's cancer history
- **47-gene panel limitations noted:** Panel does not cover GREM1 regulatory variants, connective tissue genes, or all structural variation
- **Food-specific IgG reframed:** Added AAAAI warning (recommends against food-specific IgG testing); data retained but flagged as clinically invalid; priority downgraded from High to Low
- **MCAS priority downgraded:** High → Medium (diagnosis unconfirmed)
- **Comorbidity analysis separated:** Added prominent note that hEDS/POTS hypotheses are secondary to core POLE research with zero direct evidence
- **"Eliminates 100%"** replaced with specific domain language in clinical case summary
- **FAQ updated** with TMB source caveat and thyroid size correction

---

## [0.3.0] ; 2026-04-17

### Added

- Population base rates for novel associations: duplicated IVC (0.6–2.6%), ANA 1:160 (~5–15% in healthy women), diaphragmatic endometriosis (0.6–1.5%)
- Bayesian model comparison framework with prior odds and updating rules (`models/mechanistic_models.md`)
- Tissue-specificity discriminator row in discriminatory power matrix
- Confidence tiers for novel research questions (Supported/Plausible/Speculative)
- hEDS confounding analysis: table disentangling POLE-attributable vs. hEDS-attributable phenotypes
- Missing hypotheses: POLE in telomere maintenance, immune cell development
- Emerging immunotherapy agents: anti-LAG3, anti-TIGIT, bispecifics, TIL therapy, neoantigen ADCs
- WEE1 kinase and CDK4/6 inhibitors as synthetic lethality targets
- MCAS pre-medication protocol for ICI infusions
- Levothyroxine-ICI interaction monitoring protocol
- Clinical trial matching section in surveillance protocol
- Fertility-specific genetic counseling considerations
- Tissue kinetics citations: Barker 2014, Clevers 2013, Coclet 1989, Gargett 2016, Karam 2010
- Kozak consensus references: Kozak 1986, 1987
- Duplicated IVC prevalence reference: Coco 2019
- ANA prevalence reference: Satoh 2012
- Diaphragmatic endometriosis prevalence reference: Nezhat 2019
- `requirements.txt` for Python dependencies
- Statistical limitations section in temporal correlation analysis notebook

### Changed

- Strengthened Model 1a falsification criterion with VAF threshold (≥0.15 for clonal LOH)
- Strengthened Model 4a with quantitative threshold (≥1.5-fold mutation rate elevation)
- Fixed mutational signatures row in discriminatory matrix for Models 3 and 4
- Aspirin chemoprevention: noted 81 mg as safer alternative to 600 mg given gastroparesis/gastritis
- Tissue turnover table now includes citation sources and conflation caveat
- Temporal correlation analysis includes explicit statistical limitations (n=7, surveillance bias, data dependency)
- ClinVar PP4 evidence includes limitation note (no functional data)
- Kozak scoring method explicitly defined (Kozak 1986, 1987 consensus rules)

---

## [0.1.0] ; 2026-04-15

### Added

- Initial repository setup with comprehensive README
- Research framework document (`docs/POLE_Comprehensive_Framework.docx`)
- Research slide deck (`docs/POLE_PPAP_Research.pptx`)
- AI research assistance framework (`docs/AI-Research-Assistance-Framework.md`)
- Clinical case summary (`docs/clinical_case_summary.md`)
- Six candidate mechanistic models with falsification criteria (`models/mechanistic_models.md`)
- Directory structure for analysis pipelines, models, therapeutics, and references
- CITATION.cff for repository citation
- CONTRIBUTING.md with specific collaboration opportunities
- FAQ for accessible overview of the research
- GitHub issue template for POLE truncating variant case reporting
- BibTeX bibliography (`references/bibliography.bib`)
- POLE reference data: coding sequence, domain boundaries, downstream methionines, gnomAD constraints, ClinVar variants
