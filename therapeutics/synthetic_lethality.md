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
| **ATR + PARP** | AZD6738 + Olaparib | ATR inhibition causes HRR deficiency, synergizing with PARP trapping | Phase I/II |

## Evidence

### ATR-CHK1 Axis

- Deppas JJ et al. (2025) — ATR inhibitors exploit replication stress in DNA repair-deficient cancers
- Marciniak B et al. (2024) — Synthetic lethality between ATR and POLA1 in CRC
- DepMap data suggests POLE-mutant cell lines may show ATR/CHK1 dependency (analysis needed)

### WRN Helicase

- Relevant only if secondary MMR loss creates microsatellite instability
- WRN dependency is well-established in MSI-H cancers (Behan et al., 2019)

### PARP

- Smith HL et al. (2024) — ATR/CHK1/WEE1 inhibitors create HRR deficiency, synergizing with PARP inhibitors
- Replication stress from POLE deficiency may independently increase PARP dependence

## Prioritization

1. **ATR inhibitors** — strongest mechanistic rationale and most advanced clinical development
2. **PARP inhibitors** — well-characterized safety profile; potential combination with ATR
3. **WRN inhibitors** — conditional on MSI status
4. **dNTP metabolism** — experimental; requires preclinical validation

## Data Needed

- DepMap dependency profiles of POLE-mutant cell lines (computational analysis)
- Drug sensitivity data from patient-derived organoids (when established)
- MSI status of patient's tumor (determines WRN relevance)
