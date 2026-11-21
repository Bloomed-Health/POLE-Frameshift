# Variant verification

Deterministic, offline re-derivation of POLE c.138del and of its neighbours. Standard library only.

```bash
python3 analysis/variant_verification/verify_c138del.py          # report; exit code 0 only if p.Leu46Phefs*8 is reproduced
python3 analysis/variant_verification/verify_c138del.py --json   # the same, machine-readable
python3 analysis/variant_verification/nterm_truncations.py       # every start-loss and truncating allele in exons 1-2
python3 analysis/variant_verification/nterm_truncations.py --tsv
```

`verify_c138del.py` does seven things:

1. checks that the Ensembl CDS fixture translates to the UniProt fixture (two independent sources);
2. prints the wild-type codons around the variant;
3. deletes c.138, applies the HGVS 3′ rule and derives the protein name;
4. maps the variant to GRCh38 and GRCh37, and shows where the retired GRCh37 coordinate really points;
5. lists the start codons in the first 480 nt with their Kozak context;
6. builds the translation map of the wild-type and mutant mRNA: every AUG, the ORF it opens, and where that ORF ends;
7. with `--check-legacy FILE`, measures how far a FASTA is from POLE.

`nterm_truncations.py` re-derives the dbSNP/ClinVar records listed in
`data/reference/POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv` and reports, for each, the stop position and the
next in-frame start codon. It fails if any reference allele in that table disagrees with the CDS fixture.

## Feeding the 3D viewer

The companion project [3D-POLE-Modeler](https://bloomed-health.github.io/3D-POLE-Modeler/) has a mutation page
that reads `data/pole_mutations.json`. Generate that file here, so both repositories show the same codons:

```bash
python3 analysis/variant_verification/export_viewer_json.py > ../3D-POLE-Modeler/data/pole_mutations.json
```

What these scripts establish is sequence. Whether a ribosome restarts at Met66, and whether the transcript is
degraded, are experiments (`docs/research_plan_2026-11.md`).
