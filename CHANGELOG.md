# Changelog

All notable updates to the POLE c.138del Research Framework will be documented in this file.

---

## [0.5.0] — 2026-04-17

### Changed (Scientific Database Verification & Literature Update)

- **CRITICAL: gnomAD constraint metrics corrected.** Previous values (pLI = 0.98, LOEUF = 0.22) were incorrect. Verified against gnomAD v4 API (GRCh38, ENST00000320574): pLI ≈ 0 (1.1×10⁻⁴⁰), LOEUF = 0.76, oe_lof = 0.67 (188 observed / 279 expected LoF variants). POLE tolerates heterozygous LoF — 188 carriers in gnomAD lack apparent PPAP. Corrected across all files
- **PVS1 argument strengthened by gnomAD data:** Gene-level LoF tolerance (pLI ≈ 0) provides additional evidence against PVS1 applicability
- **Mechanistic model implications updated:** gnomAD LoF tolerance supports LOH/second-hit model for tumor-specific ultra-hypermutation; Bayesian priors revised (M1 raised to 30%, M4+M1 combination ~40%)
- **Literature consensus acknowledgment added:** Prominent note in README that current scientific consensus does NOT support truncating POLE variants as pathogenic for PPAP; this framework investigates a novel hypothesis

### Added

- **Ambrosini et al. (2024) *Annals of Oncology*:** POLE/D1pd mCRC 89% ORR on ICI vs 54% dMMR/MSI-H (P=0.01)
- **Andrianova et al. (2024) *Eur J Hum Genet*:** Heterozygous POLD1 ExoD → ~15% mutation rate increase; cancer requires LOH (recessive model)
- **Nous-209 vaccine:** Leoni et al. (2026) *Nature Medicine* — 100% immune response in Lynch carriers (37/37)
- **mRNA-4157/V940:** Weber et al. (2024) *Lancet* + 5-year data (49% recurrence reduction, press release Jan 2026)
- **Wang et al. (2025) *PNAS*:** First cryo-EM proofreading intermediates of human Pol epsilon-PCNA
- **Keskitalo et al. (2025) *Nature Communications*:** POLE2 is NPF motif receptor
- **N363K glioblastoma:** Vande Perre et al. (2019) + Labrousse et al. (2023) *NAR Cancer* — extends PPAP spectrum
- **Tissue-specific NMD:** Kolakada et al. (2025) *Cell Genomics* — peptide release rate modulates NMD
- **SMaHT benchmarking:** Zhang et al. (2025) bioRxiv — 6 duplex methods compared; ppmSeq 44% recovery
- **Research gaps section** added to surveillance protocol (synthetic lethality in POLE-null, thyroid, endometriosis, AMA, preventive ICI)
- **13 new bibliography entries** in references/bibliography.bib

---

## [0.4.0] — 2026-04-17

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

## [0.3.0] — 2026-04-17

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

## [0.1.0] — 2026-04-15

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
