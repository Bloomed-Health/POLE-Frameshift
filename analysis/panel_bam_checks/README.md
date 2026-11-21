# Checks on the panel BAM/CRAM

Read-level checks you can run on the 47-gene panel alignment file. Everything stays on your machine.
Never copy the BAM into this repository (`.gitignore` blocks it).

Requirements: Python 3.9 or later and samtools 1.10 or later. A CRAM needs the reference FASTA it was aligned to.

```bash
cd analysis/panel_bam_checks
samtools index sample.bam                                   # if there is no .bai yet
python3 panel_bam_checks.py profile --bam sample.bam        # build, read count, depth at the three POLE sites
python3 panel_bam_checks.py variant --bam sample.bam        # c.138del: supporting reads, fraction, strand split
python3 panel_bam_checks.py sites   --bam sample.bam        # the two recessive POLE alleles
python3 panel_bam_checks.py power   --depth 600             # what a given depth can detect
python3 panel_bam_checks.py mosaic  --bam sample.bam --ref reference.fa --gene APC > apc_candidates.tsv
```

## What each step tells you

| Step | Question | Reading the result |
|---|---|---|
| `profile` | What is this file? | A few million mapped reads means a panel. The build is detected from the length of chromosome 12 |
| `variant` | Is c.138del in the reads, and at what fraction? | About 0.4-0.5 fits an inherited heterozygous variant. A much lower fraction would raise mosaicism |
| `sites` | Does the patient also carry c.1686+32C>G or c.4444+3A>G? | Either one in trans with c.138del causes recessive POLE deficiency, which this adult's history does not suggest. "NOT COVERED" means the panel did not capture that intronic base |
| `mosaic` | Is there a low-fraction variant in APC in blood? | Each line is a lead to inspect, not a call. An empty list does not exclude mosaicism: most mosaic APC variants are low or absent in blood |
| `power` | How low could the scan see? | At 600x and five supporting reads, a 1% variant is found about 7 times in 10 and a 2% variant almost always |

## The APC region

`--gene APC` scans Ensembl's span of the gene for the build detected in your file: GRCh38 chr5:112707452-112846239,
GRCh37 chr5:112043195-112181936 (ENSG00000134982, looked up 2026-11-20). Only positions the panel captured at
100x or more are examined. Use `--region` for anything else.

## Status and limits

- The pileup parser, the statistics and the POLE coordinates are tested (`tests/test_panel_bam_checks.py`).
- The samtools calls were written without access to samtools or to real data. Treat the first run as a test of the script as well as of the sample, and report anything odd.
- `mpileup` is run with its default read filters, which drop reads flagged as duplicate, secondary, QC-fail or improperly paired. Capture panels can have many improperly paired fragments, so depth and variant fractions may be understated; compare with the depth shown in a genome browser before concluding anything from a low count. `mosaic` refuses to run without `--ref`, because without the reference FASTA the reference base at each position is unknown.
- A panel BAM cannot answer questions about genes it did not capture, about structural variants, or about tissue that was not sequenced.
- A finding here is a research lead. Clinical confirmation belongs to an accredited laboratory.
