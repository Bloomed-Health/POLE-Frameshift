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

- DepMap dependency profiles of POLE-mutant cell lines (computational analysis)
- Drug sensitivity data from patient-derived organoids (when established)
- MSI status of patient's tumor (determines WRN relevance)
