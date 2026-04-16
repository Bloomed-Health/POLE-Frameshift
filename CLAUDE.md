# CLAUDE.md — POLE c.138del Research Framework

## Project Overview

This is a scientific research framework investigating **POLE c.138del (p.Leu46Phefs*8)** — an ultra-rare pathogenic frameshift variant in the POLE gene that causes Polymerase Proofreading-Associated Polyposis (PPAP) with ultra-hypermutated tumor phenotype (TMB >100 mut/Mb).

The central research question is a **mechanistic paradox**: this variant truncates the protein at residue 54, eliminating 100% of functional domains (exonuclease at 268–471, polymerase at 580–1260), yet produces a clinical phenotype indistinguishable from classical PPAP caused by missense variants within the exonuclease active site.

## Key Context

- **Variant:** POLE c.138del (p.Leu46Phefs*8) — frameshift deletion, premature stop at ~residue 54 of 2,286 amino acids
- **Gene:** POLE (DNA Polymerase Epsilon, catalytic subunit), chromosome 12q24.33, transcript ENST00000320574
- **Constraint:** gnomAD pLI = 0.98, LOEUF = 0.22 — extreme loss-of-function intolerance; variant absent from all population databases
- **Classification:** Pathogenic (PVS1, PM2, PP4); not yet in ClinVar
- **47-gene panel (2022):** Negative for APC, MUTYH, MLH1/MSH2/MSH6/PMS2, POLD1, BRCA1/2, TP53, PTEN, and all other genes tested — POLE c.138del is the sole identified genetic driver

## Patient Phenotype (Five Categories + Comorbidity Context)

1. **Neoplastic:** Progressive adenomatous polyposis (~6 adenomas at age 19, accumulating to ~15+ by age 31; stomach, cecum, sigmoid), Stage I papillary thyroid microcarcinoma (~28; encapsulated, non-invasive, 0.6 cm; outside established PPAP spectrum)
2. **Proliferative/stromal:** Bilateral breast changes with IHC-confirmed PASH (CD34+, CK AE1/AE3−), liver hypervascular lesion (hemangioma vs FNH, segment VII, 16×14 mm) with splenoportal arteriovenous shunt
3. **Endometrial:** Stage IV+ deep infiltrating endometriosis (~27; thoracic diaphragm, intestinal adhesions), diffuse adenomyosis (~28; severe menorrhagia, iron infusions, syncope → ovarian-sparing total hysterectomy)
4. **Congenital developmental:** Duplicated inferior vena cava — cannot be explained by somatic LOH, argues for constitutive POLE haploinsufficiency
5. **Autoimmune/immune:** ANA 1:160 with reticular cytoplasmic AC-21 pattern (associated with anti-mitochondrial antibodies) — may reflect immune recognition of mitochondrial antigens exposed through POLE-driven dysfunction of nuclear-encoded mitochondrial proteins
6. **Comorbidity triad:** hEDS/POTS/gastroparesis — creates therapeutic constraints (unreliable oral drug absorption, amplified autonomic side effects) and potential phenotype modifiers (MCAS as pro-tumorigenic microenvironment; altered ECM affecting crypt architecture; dysautonomia modulating neuroimmune axis)
7. **Family history:** Maternal grandmother had uterine cancer (core PPAP malignancy) + ductal breast cancer. Raises possibility of maternal inheritance; parental testing recommended. Father and paternal grandmother unremarkable.

## Five Candidate Mechanistic Models

1. **Somatic LOH** — wild-type allele lost in tumor (Knudson two-hit)
2. **Translational reinitiation** — ribosomes reinitiate at downstream AUG, producing polymerase-only protein
3. **NMD escape + holoenzyme poisoning** — truncated peptide competes for POLE2 binding
4. **Replication stress-dependent haploinsufficiency** — 50% POLE is rate-limiting in high-turnover tissues
5. **Isoform-specific effects** — variant differentially affects tissue-specific transcripts

The congenital duplicated IVC and multi-system non-neoplastic findings most strongly support Model 4, potentially combined with Model 1 for tumor-specific ultra-hypermutation.

## Repository Structure

```
POLE-Frameshift/
├── README.md                        # Comprehensive overview and research framework
├── CLAUDE.md                        # This file
├── CITATION.cff                     # Citation metadata
├── CONTRIBUTING.md                  # Collaboration opportunities
├── CHANGELOG.md                     # Project timeline
├── FAQ.md                           # Plain-language overview
├── docs/
│   ├── clinical_case_summary.md     # Full clinical phenotype and genomic profile
│   ├── systematic_health_history.md # Whole-body phenotyping questionnaire (20 systems)
│   ├── pole_carrier_registry_crossref.md # Cross-reference: PolED, Valle cohort, published carriers
│   ├── comorbidity_interaction_analysis.md # hEDS/POTS/gastroparesis interaction with POLE pathology
│   ├── endometriosis_hypothesis/    # POLE-endometriosis hypothesis with testable predictions
│   │   └── POLE_Endometriosis_Hypothesis.docx
│   ├── POLE_Comprehensive_Framework.docx # Comprehensive research framework document
│   ├── POLE_PPAP_Research.pptx      # Slide deck (12 slides)
│   └── AI-Research-Assistance-Framework.md
├── analysis/
│   ├── variant_landscape/           # POLE protein variant lollipop plot (SVG/PNG)
│   ├── temporal_phenotype/          # Tissue vulnerability, phenotype timeline, turnover-vs-age correlation
│   │   ├── generate_temporal_analysis.py  # Generates 3 figures
│   │   ├── temporal_correlation_analysis.ipynb  # Statistical analysis (Spearman/Pearson/bootstrap)
│   │   └── *.svg, *.png             # Output visualizations
│   ├── mutational_signatures/       # SigProfiler pipeline specs
│   ├── loh_analysis/                # ASCAT/FACETS LOH framework
│   ├── duplex_sequencing/           # NanoSeq pipeline specs
│   └── neoantigen_prediction/       # NetMHCpan/pVACseq pipeline
├── models/
│   ├── mechanistic_models.md        # Formal hypotheses with falsification criteria
│   ├── computational/               # Stochastic crypt dynamics model
│   └── experimental_protocols/      # Organoid, CRISPR, mouse model protocols
├── therapeutics/
│   ├── immunotherapy_strategy.md    # ICI rationale and monitoring
│   ├── synthetic_lethality.md       # ATR/PARP/WRN targets
│   ├── surveillance_protocol.md     # Multi-organ surveillance
│   └── pharmacokinetic_considerations.md # Drug-comorbidity interaction map
├── data/                            # Structured reference data (TSV/FASTA/JSON)
│   ├── POLE_coding_sequence.fa
│   ├── POLE_domain_boundaries.tsv
│   ├── POLE_downstream_methionines.tsv
│   ├── POLE_gnomad_constraints.tsv
│   ├── POLE_clinvar_variants.tsv
│   ├── phenotype_hpo.tsv           # HPO phenotype mapping (16 findings)
│   ├── phenotype_timeline.tsv      # Age-at-onset data with specific ages for temporal analysis
│   ├── tissue_replication_rates.tsv # Tissue turnover rates with POLE vulnerability
│   ├── checksums.sha256            # SHA-256 checksums for reproducibility
│   ├── phenopacket/                # GA4GH Phenopacket v2
│   │   └── pole_c138del_phenopacket.json
│   └── clinvar_submission/         # ClinVar submission preparation
│       ├── README.md               # Submission guide, ACMG evidence, checklist
│       └── clinvar_submission_template.json  # API v2 submission template
└── references/
    └── bibliography.bib             # BibTeX references
```

## Key References

- **Classification framework:** Mur et al. (2023) *Genome Medicine* — gene-specific ACMG/AMP for POLE/POLD1 ED variants; c.138del falls outside its scope (truncating, upstream of ED)
- **Normal tissue mutation rates:** Robinson et al. (2021) *Nature Genetics* — NanoSeq proves germline POLE mutations elevate SBS10a/b in normal cells
- **ICI response:** Garmezy et al. (2022) *JCO Precision Oncology* — pathogenic POLE: 82.4% CBR; Pietrantonio et al. (2024) *Annals of Oncology* — POLE signature ≥78.5% predicts response
- **Preventive ICB:** Sawant et al. (2025) *Cancer Research* — ICB delays cancer in polymerase mutator mice
- **PolED database (2025)** — curated POLE/POLD1 variant functional studies

## Skills

When working on variant interpretation, mechanistic reasoning, or therapeutic mapping for this case, use the **Cancer Predisposition Variant Analyst** skill:

```bash
npx skills@latest add Bloomed-Health/cancer-predisposition-variant-analyst
```

- **Repository:** https://github.com/Bloomed-Health/cancer-predisposition-variant-analyst
- **What it does:** Resolves genotype-phenotype paradoxes in cancer predisposition genes. Assembles ACMG/ClinGen evidence, generates ranked mechanistic hypotheses, maps mechanism to therapy. 72 references (2024–2026). The worked example throughout is the POLE c.138del case from this repo.
- **Trigger:** Fires when the conversation involves a genotype-phenotype paradox, POLE/POLD1 truncation variants, or mechanistic contradictions in multi-domain disease genes.
- **Workflow:** Characterize variant → generate hypotheses → classify (ACMG) → search literature → map to therapeutics.

## Conventions

- This is a research framework, not a software project — there are no build steps or tests
- All clinical data is de-identified
- Content is licensed CC BY 4.0
- References use PubMed links where available; bibliography in BibTeX at `references/bibliography.bib`
- Mutational signatures follow COSMIC v3.4 nomenclature (SBS10a, SBS10b, SBS28, etc.)
- Protein positions refer to the canonical POLE transcript ENST00000320574 (NM_006231), 2,286 amino acids
- This framework is intended for research purposes and does not constitute medical advice
