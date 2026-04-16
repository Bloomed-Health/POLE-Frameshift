# Changelog

All notable updates to the POLE c.138del Research Framework will be documented in this file.

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
