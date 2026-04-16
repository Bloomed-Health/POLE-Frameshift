# Immunotherapy Strategy

## Rationale

The POLE c.138del tumor has TMB >100 mutations/Mb, far exceeding the FDA tissue-agnostic threshold (≥10 mut/Mb) for pembrolizumab. Published data on pathogenic POLE variants shows strong immunotherapy efficacy.

## Evidence Base

| Study | Key Finding |
|-------|-------------|
| Garmezy et al. (2022) *JCO Precision Oncology* | Pathogenic POLE: 82.4% CBR, 15.1 mo PFS, 29.5 mo OS (n=458) |
| Pietrantonio et al. (2024) *Annals of Oncology* | POLE signature ≥78.5% predicts ICI response |
| Sawant et al. (2025) *Cancer Research* | Preventive ICB delays cancer in polymerase mutator mice |

## Treatment Options

### First-Line: Anti-PD-1 Monotherapy

- **Agent:** Pembrolizumab 200mg IV q3w or 400mg IV q6w
- **Rationale:** TMB >100 mut/Mb; tissue-agnostic FDA approval
- **Monitoring:** CT imaging q12w, ctDNA q6–8w

### Escalation: Anti-PD-1 + Anti-CTLA-4

- **Agents:** Nivolumab + ipilimumab
- **Rationale:** If immune profiling shows multiple co-inhibitory receptors (PD-1, TIM-3, LAG-3, TIGIT) on tumor-infiltrating T cells
- **Precedent:** CheckMate-142 in MSI-H CRC

### Neoantigen Vaccination

- **Platform:** mRNA-4157/V940 or equivalent
- **Setting:** Adjuvant, post-resection, in combination with anti-PD-1
- **Rationale:** Extreme neoantigen load provides abundant high-quality vaccine targets

### Preventive Immunotherapy (Hypothesis-Generating Only)

- **Setting:** Pre-cancer, in PPAP carriers
- **Evidence:** Sawant et al. (2025) — In polymerase mutator mice, prophylactic anti-PD-1 raised the responder rate from 2.7% to 32.5% and delayed tumor onset, selecting against aneuploid tumors. However, ICB did **not** improve survival in mice with established tumors. This is a provocative hypothesis-generating preclinical finding in germline exonuclease-domain missense mutant mice (not frameshift carriers), not a therapeutic recommendation.
- **Status:** Preclinical only; no human trials; the authors frame this as raising a possibility for high-risk individuals, not as evidence that preventive ICB works

## Pre-Treatment Autoimmune Considerations

The patient has **ANA 1:160 with reticular cytoplasmic AC-21 pattern**, characteristically associated with anti-mitochondrial antibodies (AMA). This has direct implications for ICI safety:

### irAE Risk Assessment

- **Pre-existing ANA positivity** is associated with increased risk of immune-related adverse events (irAEs) during checkpoint inhibitor therapy
- **AC-21/AMA association** raises specific concern for autoimmune hepatitis, cholangitis, and biliary irAEs — particularly relevant given the patient's liver FNH/hemangioma
- ICI can unmask subclinical autoimmune conditions; the AC-21 finding warrants pre-treatment characterization

### Required Pre-ICI Workup

| Test | Purpose |
|------|---------|
| **AMA-specific ELISA** (anti-PDC-E2) | Confirm whether AC-21 reflects true AMA; establish baseline |
| **Liver function panel** (GGT, ALP, bilirubin) | Baseline biliary function; PBC screening given AMA + hepatic lesions |
| **Extended autoimmune panel** (anti-dsDNA, ENA, C3/C4, anti-smooth muscle) | Characterize scope of autoimmune activation before ICI |
| **Thyroid function** (TSH, free T4, anti-TPO) | Baseline for thyroid irAE monitoring. Patient is post-total thyroidectomy on levothyroxine — ICI-induced thyroiditis is not expected (no thyroid tissue), but TSH/free T4 monitoring remains necessary to detect ICI-mediated changes in levothyroxine metabolism or absorption, and thyroglobulin trending for recurrence detection |

### ICI Monitoring Modifications for ANA-Positive Patients

- **Liver enzymes q2w** during induction (vs. standard q3–6w) — lower threshold for hepatic irAE investigation
- **AMA titer trending** at baseline, week 6, week 12, and at any suspected irAE — rising titers may indicate evolving biliary autoimmunity
- **Hepatology consultation** if any Grade ≥1 hepatic irAE given potential overlap with subclinical PBC
- **Hold ICI and escalate** if ALP rises >2x ULN with GGT elevation — biliary pattern concerning for cholangitis irAE vs. PBC exacerbation

## Dysautonomia and Comorbidity Considerations

The patient's hEDS/POTS/gastroparesis triad creates specific constraints and risks for immunotherapy that are not captured in standard ICI response prediction frameworks.

### Drug Delivery Challenges

| Challenge | Impact | Mitigation |
|-----------|--------|------------|
| **Gastroparesis** | Delayed and erratic gastric emptying → unreliable oral drug absorption | Prefer IV formulations; if oral agents required, consider liquid/sublingual forms; monitor drug levels |
| **POTS** | Orthostatic intolerance during infusions; autonomic instability | Extended infusion protocols; IV hydration pre/post; supine or reclined infusion positioning |
| **GI dysmotility** | Baseline nausea, bloating, SIBO overlap complicates irAE detection | Establish detailed GI symptom baseline before ICI initiation; use validated PRO instruments |

### ICI-Specific Risks in Dysautonomia

- **Autoimmune colitis (irAE):** Especially difficult to detect against the backdrop of pre-existing GI dysmotility, gastroparesis, recurrent SIBO, and endometriosis-related bowel adhesions. Low threshold for endoscopic evaluation of new GI symptoms.
- **Autonomic neuropathy (irAE):** ICI agents can cause immune-mediated autonomic neuropathy — potentially catastrophic in a patient with pre-existing POTS. Baseline autonomic function testing required; monitor for POTS exacerbation during treatment.
- **Hepatic irAE overlap:** Pre-existing ANA AC-21/AMA + liver FNH/hemangioma + potential subclinical PBC requires careful hepatic monitoring (see Pre-Treatment Autoimmune Considerations above).

### Impact on Response Prediction

The ICI response prediction framework (POLE signature ≥78.5% predicting response; Pietrantonio et al., 2024) was established in patients without this comorbidity burden. There is genuine uncertainty about whether published response rates translate directly to this patient, because:

1. **Dysautonomia modulates immune function** — the vagus nerve is a major neuroimmune regulatory pathway; POTS patients may have altered baseline immune profiles
2. **MCAS (if present)** may suppress local immune surveillance, potentially counteracting neoantigen-driven T cell responses
3. **Chronic inflammation** from mast cell activation or connective tissue dysfunction may create an immunosuppressive microenvironment

These factors do not contraindicate ICI — the TMB >100 mut/Mb remains a strong predictor — but they argue for enhanced monitoring, immune profiling before and during treatment, and realistic expectations about whether published response data fully apply.

## Resistance Monitoring

- **Primary resistance markers:** B2M loss, JAK1/JAK2 mutations, HLA loss
- **Monitoring:** ctDNA for emerging resistance mutations; repeat biopsy at progression
- **Strategy:** Proactive surveillance for resistance rather than reactive detection
