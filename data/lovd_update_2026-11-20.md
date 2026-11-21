# Replacement text for the LOVD entry (variant #0001074000, DB-ID POLE_000381)

The entry at <https://databases.lovd.nl/shared/variants/0001074000> was created by this project on 2026-04-15.
Three of its fields are no longer accurate. Suggested values, field by field:

| LOVD field | Current value | Suggested value | Why |
|------------|---------------|-----------------|-----|
| Clinical classification | pathogenic (dominant) | VUS, or "pathogenic (recessive)" if the curator prefers to follow the laboratory | The laboratory's Pathogenic call rests on loss of function, which causes recessive POLE deficiency (FILS, IMAGe). No evidence shows that one loss-of-function allele causes dominant disease; ClinVar holds conflicting classifications |
| Affects function (as reported) | Affects function | Effect unknown | No RNA, protein or tumour data exist for this allele |
| Variant remarks | "variant presents a mechanistic paradox ... phenotype is indistinguishable from classical dominant-negative PPAP ..." | "Heterozygous frameshift in exon 2 (stop at codon 53). Carrier has about 20 gastric and colonic polyps removed since age 19 (histology reports being collected) and a papillary thyroid carcinoma. No tumour has been sequenced; tumour mutational burden and mutational signatures are unknown. A 47-gene hereditary cancer panel was otherwise negative. Whether the variant contributes to the phenotype is unknown. Transcript fate (nonsense-mediated decay versus re-initiation at Met66) is untested." | The earlier text asserted a PPAP phenotype and a paradox that rest on an unmeasured mutational burden |
| ClinVar ID | - | 548779 (VCV000548779) | The variant has been in ClinVar since 2018 |
| dbSNP ID | - | rs1555230420 | |
| Frequency | absent gnomAD | gnomAD v4.1 exomes: 1/1,461,874 alleles; gnomAD v2.1.1 genomes: 1/31,386 alleles | gnomAD API, queried 2026-11-20 (ledger rows D04, D05) |
| Reference | github.com/Bloomed-Health/POLE-Frameshift | unchanged, plus `docs/VERIFICATION_AUDIT_2026-11-20.md` | |
| Genes screened (screening record) | POLD1, POLE, PTEN | the 47 genes listed in `data/claims_ledger.tsv`, row L02 | The screening was a 47-gene panel |

Fields that are already correct and should stay: hg19 g.133257790del, hg38 g.132681204del, c.138del, p.(Leu46PhefsTer8), origin germline, technique SEQ-NG, tissue blood.

The transcript shown by LOVD is NM_006231.2. The variant name is the same on NM_006231.4 (MANE Select).
