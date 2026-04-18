# Synthetic Lethality Targets

## Rationale

POLE-deficient cells operate near a viability threshold for replication stress and DNA damage tolerance. Targeting compensatory DNA repair and replication stress response pathways may be selectively lethal to tumor cells.

## Target Summary

| Target | Drug Candidates | Rationale | Stage |
|--------|----------------|-----------|-------|
| **ATR-CHK1** | Ceralasertib, Berzosertib, Elimusertib | ATR inhibition causes replication catastrophe in POLE-deficient cells | Phase I/II |
| **WRN helicase** | WRN inhibitors | Essential for fork stability at expanded microsatellites if secondary MMR loss creates MSI | Preclinical |
| **PARP trapping** | Olaparib, Talazoparib | Replication stress increases dependence on PARP1-mediated fork stabilization | Phase II |
| **dNTP metabolism** | Brequinar (DHODH), low-dose HU | Nucleotide imbalance compounds proofreading deficit | Experimental |
| **WEE1 kinase** | Adavosertib (AZD1775) | WEE1 inhibition forces premature mitotic entry with unrepaired DNA damage; synergizes with replication stress from POLE deficiency | Phase I/II |
| **CDK4/6** | Palbociclib, Ribociclib, Abemaciclib | G1/S checkpoint inhibition in combination with replication stress; may force POLE-deficient cells into S-phase with inadequate proofreading capacity | Phase I (combination; no POLE-specific data) |
| **ATR + PARP** | AZD6738 + Olaparib | ATR inhibition causes HRR deficiency, synergizing with PARP trapping | Phase I/II |

## Evidence

### ATR-CHK1 Axis

- Deppas JJ et al. (2025) — ATR inhibitors exploit replication stress in DNA repair-deficient cancers
- Marciniak B et al. (2024) — Synthetic lethality between ATR and POLA1 in CRC
- DepMap data suggests POLE-mutant cell lines may show ATR/CHK1 dependency (analysis needed)

### WRN Helicase

- Relevant only if secondary MMR loss creates microsatellite instability
- WRN dependency is well-established in MSI-H cancers (Behan et al., 2019)

### WEE1

- WEE1 is a G2/M checkpoint kinase; its inhibition forces cells with DNA damage into mitosis
- Smith HL et al. (2024) demonstrated WEE1 inhibitors cause HRR deficiency, creating synthetic lethality with PARP inhibitors
- POLE-deficient cells with elevated replication errors may be selectively vulnerable to premature mitotic entry
- Adavosertib has shown clinical activity in combination with other DDR inhibitors in Phase I/II trials

### PARP

- Smith HL et al. (2024) — ATR/CHK1/WEE1 inhibitors create HRR deficiency, synergizing with PARP inhibitors
- Replication stress from POLE deficiency may independently increase PARP dependence

## Critical Distinction: POLE-Mutant vs. POLE-Null

> **All published synthetic lethality data in POLE-deficient cancers derives from POLE-*mutant* (exonuclease domain missense) cells, NOT POLE-*null* (complete loss-of-function) cells.** This distinction is critical for translating synthetic lethality findings to this patient's tumors.

### Comparison

| Feature | POLE-Mutant (ExoD Missense) | POLE-Null (Complete Loss) |
|---------|----------------------------|--------------------------|
| **Polymerase present?** | Yes — full-length, catalytically active | No — absent or truncated/nonfunctional |
| **Leading strand replication** | Pol epsilon-dependent (normal processivity) | Must be rescued by Pol delta or other polymerases |
| **Source of replication stress** | Proofreading deficiency → uncorrected mismatches → ultra-hypermutation | Loss of leading strand polymerase → fork stalling, collapse, incomplete replication |
| **ATR/CHK1 dependency** | Moderate — replication stress from mismatch accumulation | Likely high — replication fork collapse activates ATR strongly |
| **Fork speed** | Normal or slightly elevated | Reduced (Pol delta is slower on leading strand) |
| **Mutation signature** | SBS10a/b, SBS28 (characteristic POLE ExoD signatures) | Unknown — no published data |

### Why This Matters

The patient's POLE c.138del frameshift creates a **loss-of-function allele**. In tumors that undergo LOH (loss of the wild-type allele), the resulting state is **POLE-null** — complete absence of functional Pol epsilon exonuclease and polymerase activity. This is mechanistically distinct from the P286R/V411L missense mutations studied in synthetic lethality screens, where the polymerase is present but proofreading-deficient.

Key implications:
- **ATR/CHK1 inhibitors** may be *more* effective in POLE-null cells (greater replication stress from fork collapse) — but this is untested
- **PARP inhibitors** may have different efficacy profiles (different type of replication stress)
- **WEE1 inhibitors** rationale may be stronger (more unrepaired damage at G2/M)
- Drug sensitivity predictions from POLE-mutant DepMap data may not transfer directly

### Evidence Gap

Andrianova et al. (2024) established that heterozygous POLD1 ExoD mutations produce only ~15% mutation rate increase, with cancer requiring LOH — a **recessive model**. This supports the interpretation that the patient's tumors are POLE-null (via LOH), not POLE-haploinsufficient. However, no synthetic lethality screen has been performed in POLE-null (knockout) cells.

### Required Experiments

- **CRISPR POLE knockout** in appropriate cell lines (colorectal, endometrial) followed by drug sensitivity screening against ATR, PARP, WEE1, and CHK1 inhibitors
- **Comparison** of drug sensitivity profiles between POLE-knockout and POLE-ExoD-mutant isogenic cell lines
- **DepMap reanalysis** filtering for any POLE-null (homozygous deletion/truncating) cell lines vs. POLE-ExoD-mutant lines

## Prioritization

1. **ATR inhibitors** — strongest mechanistic rationale and most advanced clinical development
2. **PARP inhibitors** — well-characterized safety profile; potential combination with ATR
3. **WEE1 inhibitors** — strong mechanistic rationale (forces mitotic entry with unrepaired errors); adavosertib in Phase I/II
4. **WRN inhibitors** — conditional on MSI status
5. **CDK4/6 inhibitors** — potential combination with replication stress inducers; well-characterized safety profile
6. **dNTP metabolism** — experimental; requires preclinical validation

## Comorbidity-Specific Therapeutic Risks

The patient's hEDS/POTS/gastroparesis triad interacts with several candidate synthetic lethality agents:

| Agent Class | Relevant Side Effects | Interaction with Comorbidities |
|-------------|----------------------|-------------------------------|
| **ATR inhibitors** (ceralasertib, berzosertib) | Nausea, fatigue, autonomic side effects | Potentially catastrophic in pre-existing POTS; nausea compounds gastroparesis; requires dose modification and enhanced monitoring |
| **PARP inhibitors** (olaparib, talazoparib) | Nausea, fatigue, myelosuppression | Oral bioavailability unreliable with gastroparesis; consider IV alternatives or absorption monitoring |
| **dNTP metabolism** (brequinar, low-dose HU) | GI toxicity, myelosuppression | Oral agents; gastroparesis affects absorption predictability |

**Route of administration is a critical consideration.** Gastroparesis makes oral medication bioavailability inherently unreliable — any drug regimen must account for delayed and erratic absorption. IV formulations should be preferred where available. For oral agents, pharmacokinetic monitoring or alternative delivery routes (sublingual, transdermal, subcutaneous) should be evaluated.

## Data Needed

- **POLE-null synthetic lethality validation:** CRISPR knockout screens in colorectal/endometrial cell lines to determine whether drug sensitivities differ between POLE-null and POLE-ExoD-mutant states (see § Critical Distinction above)
- DepMap dependency profiles of POLE-mutant cell lines (computational analysis)
- Drug sensitivity data from patient-derived organoids (when established)
- MSI status of patient's tumor (determines WRN relevance)
