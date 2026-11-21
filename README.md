# POLE c.138del (p.Leu46Phefs*8) — Research Framework

> **No tumour or polyp from this patient has been sequenced.** Tumour mutational burden, mutational signatures and MMR status are unknown. Statements about hypermutation in this repository are assumptions from the PPAP literature, not observations. Read this alongside the [verification audit](docs/VERIFICATION_AUDIT_2026-11-20.md).

An ultra-rare germline frameshift in DNA Polymerase Epsilon (two carriers in gnomAD; conflicting ClinVar classifications) in a patient with progressive adenomatous polyposis and papillary thyroid carcinoma. **Whether the variant contributes to the phenotype is the open question.**

## Quick Links

| Start here | Additional resources |
|------------|---------------------|
| [Verification Audit](docs/VERIFICATION_AUDIT_2026-11-20.md) | [Clinical Case Summary](docs/clinical_case_summary.md) |
| [Research Plan](docs/research_plan_2026-11.md) | [Systematic Health History](docs/systematic_health_history.md) |
| [Polyposis Differential](docs/polyposis_differential.md) | [POLE Carrier Registry Cross-Ref](docs/pole_carrier_registry_crossref.md) |
| [c.138del Among Other POLE Variants](docs/pole_variant_comparison.md) | [Comorbidity Interaction Analysis](docs/comorbidity_interaction_analysis.md) |
| [Evidence Protocol](docs/EVIDENCE_PROTOCOL.md) | [Formal Hypotheses & Falsification](models/mechanistic_models.md) |
| [Claims Ledger](data/claims_ledger.tsv) | [FAQ](FAQ.md) · [Changelog](CHANGELOG.md) · [llms.txt](llms.txt) |

---

## The Variant

- **POLE c.138del (p.Leu46Phefs*8)** — heterozygous germline frameshift, confirmed on two independent clinical platforms
- Premature stop at codon 53 of 2,286 — upstream of all catalytic domains
- Classified **Pathogenic** by clinical lab (standard ACMG null-variant criteria); independently assessed as **VUS** pending functional data ([ClinVar VCV000548779](https://www.ncbi.nlm.nih.gov/clinvar/variation/548779/), conflicting)
- gnomAD: present in 2 of ~1.5M alleles; gene-level pLI ≈ 0, LOEUF 0.76 (tolerates heterozygous LoF)
- 47-gene hereditary cancer panel: POLE c.138del is the only finding; panel does not cover MBD4, RNF43, FAN1, connective tissue genes, or structural variation
- HGVS verified on MANE Select (NM_006231.4 / ENST00000320574.10): [`verify_c138del.py`](analysis/variant_verification/verify_c138del.py)

## The Patient

Female, early 30s, European ancestry. Five phenotype categories plus comorbidity context:

| Category | Key findings |
|----------|-------------|
| **Neoplastic** | ~15 adenomatous polyps (ages 19–31, progressive); Stage I papillary thyroid carcinoma (~age 28) |
| **Proliferative/stromal** | Bilateral PASH (CD34+); liver hypervascular lesion; splenoportal AV shunt |
| **Endometrial** | Stage IV+ deep infiltrating endometriosis; adenomyosis → hysterectomy at ~28 |
| **Congenital** | Duplicated inferior vena cava (cannot be somatic; base rate 0.6–2.6%) |
| **Autoimmune** | ANA 1:160, AC-21 pattern (anti-mitochondrial antibody associated) |
| **Comorbidity** | hEDS / POTS / gastroparesis — confounds some findings and constrains therapeutics |

Full clinical detail: [`docs/clinical_case_summary.md`](docs/clinical_case_summary.md)

## Why It's a Paradox

Classical PPAP is caused by **exonuclease-domain missense** variants that produce a dominant-negative, error-prone polymerase. This variant truncates the protein before any functional domain. Under orthodox models, haploinsufficiency should be insufficient (gnomAD has 188 LoF variants without apparent PPAP), and complete POLE loss is embryonic lethal. Yet the patient's phenotype overlaps with PPAP on polyp count, distribution, and multi-system involvement — though no molecular feature of PPAP has been confirmed.

## Candidate Models

Eight models are maintained. **Model 0 (variant is incidental) currently leads** on present evidence.

| # | Model | Status |
|---|-------|--------|
| **0** | **Null hypothesis** — variant is a passenger; phenotype driven by an unidentified cause | **Leading.** Supported by Mur et al. 2020 (LoF not enriched in cancer; OR 1.08), 188 gnomAD LoF carriers, and no patient-level molecular data |
| 1 | Somatic LOH — wild-type allele lost in tumour (Knudson two-hit) | Hypothesis; but a null allele + LOH = no Pol ε |
| 2 | Translational reinitiation at Met66 | Untested; a Met66 product keeps both catalytic domains |
| 3 | NMD escape + holoenzyme poisoning | Low prior (binding interface is C-terminal) |
| 4 | Replication stress-dependent haploinsufficiency | Pre-audit primary; supporting evidence weakened |
| 5 | Isoform-specific effects | Untested |
| 6 | Second-site somatic POLE mutation on wild-type allele | Testable by phased tumour WGS |
| 7 | Variant-call / annotation artifact | **Closed.** HGVS verified; SpliceAI delta scores all 0 |

Formal hypotheses with falsification criteria: [`models/mechanistic_models.md`](models/mechanistic_models.md)

## What Needs to Happen

Ranked by information per unit cost (full detail in [`docs/research_plan_2026-11.md`](docs/research_plan_2026-11.md)):

1. **Reporter assay for Met66 re-initiation** + allele-specific RNA from blood — what does the allele make?
2. **Exome of the stored thyroid tumour** with matched blood — first measured burden, signature, LOH
3. **Duplex sequencing (NanoSeq)** of blood and normal colon — is the normal mutation rate elevated?
4. **Polyp sequencing** at next endoscopy — shared APC variant → mosaic APC; polymerase signature → unexpected
5. **Clinical WGS/WES** — test the null hypothesis by looking for alternative drivers

## Reproducibility

All sequence-level claims are re-derived from checked-in fixtures by code. 52 offline tests run on every push; 14 live tests run weekly. Every factual claim has a row in [`data/claims_ledger.tsv`](data/claims_ledger.tsv) with status, source, and date. See [`docs/EVIDENCE_PROTOCOL.md`](docs/EVIDENCE_PROTOCOL.md) for the rules.

```bash
# Verify the variant derivation and run the test suite
python3 analysis/variant_verification/verify_c138del.py && python3 -m pytest -q tests
```

## Repository Structure

```
POLE-Frameshift/
├── README.md                        # This file
├── docs/                            # Audit, research plan, differential, clinical detail, evidence protocol
├── analysis/                        # Variant verification, figures, pipeline specs (mostly not yet run)
├── models/                          # Mechanistic models, experimental protocols, computational specs
├── therapeutics/                    # ICI, synthetic lethality, surveillance, PK (pre-audit; contingency)
├── data/                            # Reference fixtures, claims ledger, phenotype data, ClinVar/LOVD
├── figures/                         # Generated figures (SVG + PNG)
├── references/bibliography.bib      # 89 entries, rebuilt from PubMed
├── tests/                           # 52 offline + 14 live tests
└── .github/workflows/              # CI: verify on push, live checks weekly
```

## Contributing

This is an n-of-1 hypothesis-generating framework seeking collaborators — structural biologists, clinical geneticists, bioinformaticians, immunologists. See [CONTRIBUTING.md](CONTRIBUTING.md).

- **Have a patient with a POLE truncating variant?** [Submit a case report](https://github.com/Bloomed-Health/POLE-Frameshift/issues/new?template=pole-case-report.yml)
- **Questions or ideas?** [Discussions](https://github.com/Bloomed-Health/POLE-Frameshift/discussions)
- **New to POLE/PPAP?** [FAQ](FAQ.md)

## License

MIT. See [`LICENSE`](LICENSE) · [`CITATION.cff`](CITATION.cff)
