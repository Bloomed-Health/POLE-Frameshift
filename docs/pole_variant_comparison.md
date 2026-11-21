# c.138del among other POLE variants

Written 2026-11-20. Reproduce the tables with `python3 analysis/variant_verification/nterm_truncations.py`.
Ledger rows C01-C03 and E01-E12.

## 1. Four classes of germline POLE variant

| Class | Examples | What the allele does | Inheritance and phenotype | Tumours |
|---|---|---|---|---|
| Exonuclease-domain missense | p.Leu424Val, p.Pro286Arg, p.Val411Leu, p.Ser459Phe, p.Tyr458Phe, p.Asn363Lys | Full-length enzyme that copies DNA and does not proofread | Dominant: polymerase proofreading-associated polyposis | Ultramutated, SBS10a/b; the wild-type allele is kept (Park & Pursell 2019, [doi](https://doi.org/10.1016/j.dnarep.2019.02.007)) |
| Hypomorphic splice alleles | c.1686+32C>G; c.4444+3A>G | Mostly mis-spliced, some normal transcript | Recessive: IMAGe syndrome with a null allele in trans; FILS syndrome when homozygous | Lymphoma in 2 of 15 IMAGe patients (Logan et al. 2018, [doi](https://doi.org/10.1016/j.ajhg.2018.10.024)) |
| Loss of function | c.2091dupC, p.Trp1980\*, p.Tyr683\*, c.1A>T, c.62+1G>A and others in IMAGe families; p.Glu396Thrfs\*15, p.Gln1494\*, p.Tyr766\* in Mur 2020 | No functional enzyme from that allele | Recessive disease only with a hypomorph in trans; carrier parents unaffected | Not hypermutated where measured (Mur et al. 2020, [doi](https://doi.org/10.1038/s41436-020-0922-2)) |
| **Start-proximal truncations** (a subset of the above) | **c.138del**, c.137del, c.137dup, c.141del, c.1A>T and 29 more in exons 1-2 | Unknown. Sequence permits a restart at Met44 or Met66 with both catalytic domains intact | Unknown; treated by laboratories like any other loss of function | No data |

c.138del belongs to the third class by default and to the fourth by position. Nothing places it in the first.

How a POLE or POLD1 variant earns the first class is instructive: p.Tyr458Phe was upgraded after two carriers'
tumours proved ultramutated and a mutagenesis assay agreed (Rocque et al. 2023,
[doi](https://doi.org/10.1007/s00438-023-02000-w)); POLD1 p.Leu474Ile was supported by hypermutation and
SBS10c/SBS10d in cancers and in most polyps from three relatives (Buchanan et al. 2025,
[doi](https://doi.org/10.1007/s10689-025-00506-3)). Tumour sequencing is the test.

## 2. The neighbours of c.138del

dbSNP and ClinVar hold 26 truncating and 8 start-loss alleles in the coding part of exons 1 and 2
(retrieved through Ensembl; one added from ClinVar Miner). All were re-derived on MANE Select.

Alleles that hit codons 46-48:

| Allele | Protein | New tail | Stop | Next in-frame AUG | ClinVar terms for the rsID |
|---|---|---|---|---|---|
| c.137del (rs2136034222) | p.Leu46Cysfs\*8 | CGLVLSG | codon 53 (c.158_160) | Met66, 35 nt on | pathogenic |
| c.137dup (no rsID) | p.Leu46Phefs\*6 | FAVWF | codon 51 (c.150_152) | Met66, 43 nt on | uncertain significance |
| **c.138del (rs1555230420)** | **p.Leu46Phefs\*8** | **FGLVLSG** | **codon 53 (c.158_160)** | **Met66, 35 nt on** | **pathogenic; uncertain significance** |
| c.141del (rs761329565) | p.Phe48Leufs\*6 | LVLSG | codon 53 (c.158_160) | Met66, 35 nt on | likely pathogenic; pathogenic |

Two more frameshifts further upstream (c.76del, c.74_75insGCGCG) run into the same stop codon.

Grouped by where translation could restart:

| Position of the premature stop | Alleles | Next in-frame AUG | Product if used |
|---|---|---|---|
| Upstream of Met44 (before c.130) | 15 (for example p.Glu18\*, c.51dup, p.Ser28\*, p.Trp40\*) | Met44 | lacks residues 1-43 |
| Codons 51-62 | 10 (the four above, plus c.76del, c.74_75insGCGCG, p.Lys54\*, p.Lys59\* and two alleles giving p.Trp62\*) | Met66 | lacks residues 1-65 |
| After codon 66 | 1 (c.176del, stop at codon 72) | Met221 | lacks residues 1-220 |
| Start codon lost | 8 at c.1, c.2, c.3 (c.1A>T is an IMAGe allele) | first AUG met is c.47, out of frame; then Met44 by leaky scanning or Met66 after a 37-codon ORF | lacks residues 1-43 or 1-65 |

The ClinVar terms are aggregated per rsID by Ensembl and are not allele-specific at multi-allelic sites. The
pattern is the one seen for c.138del: Pathogenic from a laboratory that applies a loss-of-function rule
(the same submitter text appears on other POLE frameshifts), Uncertain significance from others.

## 3. What the comparison says

1. **c.138del is not unusual as a database entry.** Early POLE truncations are seen regularly in clinical
   testing and carry the same split classification. The whole population of records confirms it: on 2026-11-21
   ClinVar held **497** POLE records classified Pathogenic or Likely pathogenic for germline disease, of which
   **413 are truncating** (nonsense, frameshift, splice) and only **12 are missense** (10 inside the exonuclease
   domain: E277G, P286L, S297F, N363K, L424V, P436R, P436S, Y458F, Y458H, S459F). 388 of the 413 truncating
   records name no condition; 4 name IMAGe, 3 FILS, and 10 name CRCS12/PPAP, which is a curation inconsistency,
   since no truncating variant has been shown to cause PPAP (`analysis/variant_verification/fetch_clinvar_pole.py`;
   `data/reference/POLE_clinvar_PLP_2026-11-21.tsv`). Pathogenic labels on truncating POLE variants therefore describe
   a loss-of-function rule applied at scale, not a cancer phenotype.
2. **It is unusual as a research object because it is one of four near-identical alleles.** A result on
   c.138del should hold for c.137del, c.137dup and c.141del, and largely for the other six whose next start codon is Met66. That turns a single case into a class.
3. **The class has a specific, untested property.** UniProt annotates residues 1-30 as disordered and records
   no domain before the exonuclease region. A protein that starts at Met44 or Met66 would keep every annotated
   domain. If such a protein is made and works, these alleles are milder than true nulls. That would matter
   for the recessive disorders: a start-proximal truncation paired with c.1686+32C>G might cause milder disease
   than a distal one. Three IMAGe patients carried c.1A>T; the published table is too small to tell.
4. **Nothing in the comparison supports a dominant cancer phenotype.** The property that defines the
   cancer-predisposing class, DNA synthesis without proofreading, is the one thing no outcome of these alleles can produce.

## 4. Open questions for the class

1. How much mutant transcript survives in carrier cells, with and without NMD inhibition?
2. Does translation restart at Met66 (or Met44 for the more 5′ alleles), and how efficiently compared with the wild type?
3. Is a POLE that lacks residues 1-65 stable, and does it support replication?
4. Is the weak context of the annotated start codon used at all levels of expression, or is Met44 a natural second start in normal cells?
5. Do carriers of start-proximal truncations differ from carriers of distal truncations in any measurable way: POLE protein level, S-phase progression, somatic mutation rate?
6. In IMAGe families, is the phenotype milder when the null allele is start-proximal?
7. How many carriers of these alleles exist in population cohorts, and what are their colonoscopy findings?
