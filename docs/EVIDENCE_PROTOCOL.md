# Evidence protocol

How claims enter this repository. Written after the 2026-11-20 audit, for human contributors and for AI
assistants working in the repository. The failure it is designed to stop is fluent text that reads as
knowledge and is not: a sequence that was never fetched, a citation that names the wrong paper, a patient
finding that was assumed from the literature.

## 1. Status tags

Every row of `data/claims_ledger.tsv` carries exactly one.

| Tag | Meaning | Minimum to earn it |
|-----|---------|--------------------|
| `VERIFIED` | Checked against a primary source on the date given | Identifier of the source and what was opened (abstract, full text, record page, script output) |
| `CONTRADICTED` | A statement the repository made that a primary source refutes | The refuting source |
| `INFERENCE` | Reasoning from verified facts; no direct evidence | The facts it rests on, and the experiment that would test it |
| `OWNER_STATEMENT` | Reported by the repository owner; the document was not seen | Who said it and when |
| `NOT_MEASURED` | A patient-level quantity that no test has produced | Nothing; this is the default for anything about tumours until a report exists |
| `UNVERIFIED` | Not checked, or checked from a title or a secondary site only | Say what was and was not opened |
| `NOT_FOUND` | Looked for and not located | The query, where it was run, and the date |

## 2. Rules

1. **Compute sequence facts.** Codons, coordinates, frames, start codons and peptide sequences come from
   `analysis/variant_verification/` run on `data/reference/`. If the fixture does not cover a position, extend
   the fixture with `scripts/fetch_reference.py`; do not write the residue from memory.
2. **Two independent routes for anything load-bearing.** The variant name was confirmed from Ensembl sequence,
   UniProt sequence and Ensembl VEP. A coordinate with one source is `UNVERIFIED`.
3. **Quote identifiers, not recollections.** A citation is a PMID or DOI that was fetched. Author, title,
   journal and year are copied from the record.
4. **Report the depth of reading.** "Abstract read", "full text read", "title only". A number that is not in
   the text you read is written as "not in abstract".
5. **Keep patient observations apart from literature.** A finding about this patient needs a report or data
   file. Until then it is `OWNER_STATEMENT` or `NOT_MEASURED`, and no model may treat it as data.
6. **Record failures.** A blocked page, an empty search or a refusal is written down as such.
7. **One change, one ledger row, one test where possible.** If a claim can be checked by code, add the check to `tests/`.

## 3. Extraction format, with worked examples

When a paper is read for this repository, extract into this shape. Leave a field as `not stated` instead of filling it.

```
source:        PMID / DOI
read:          abstract | full text | title only
population:    who was studied, n
finding:       the number or statement, copied closely
applies_to:    which claim in this repository it bears on
does_not_show: the tempting over-reading
```

**Example 1 (good).**

```
source:        PMID 32792570; doi:10.1038/s41436-020-0922-2
read:          full text
population:    2,813 hereditary cancer probands; gnomAD non-cancer controls
finding:       loss-of-function POLE/POLD1 variants in 5/2,309 (0.22%) patients vs 119/59,095 (0.20%) controls, p = 0.81
applies_to:    whether a heterozygous POLE null allele raises cancer risk
does_not_show: that the risk is exactly zero; the interval computed from these counts is 0.44-2.63
```

**Example 2 (good, negative result).**

```
source:        PubMed query: POLE AND (haploinsufficiency OR heterozygous null OR hemizygous) AND (cancer OR tumor OR replication stress)
read:          14 records returned; titles of 10 examined
finding:       none concerned POLE dosage
applies_to:    whether anyone has studied cancer risk from reduced POLE dose
does_not_show: that no such study exists
status:        NOT_FOUND
```

**Example 3 (good, sequence fact).**

```
source:        analysis/variant_verification/verify_c138del.py, section 6
read:          script output
finding:       on the c.138del mRNA the AUGs at c.1, c.47, c.65, c.68 and c.130 open ORFs ending by c.160; the next AUG is c.196 (Met66), in frame
applies_to:    Model 2 (re-initiation)
does_not_show: that ribosomes restart at Met66; that is an experiment
status:        VERIFIED for the sequence; INFERENCE for the biology
```

**Example 4 (bad; taken from this repository's history).**

```
claim:   "Verification against the POLE coding sequence in this repository confirms: codon 46 (c.136-138) = GAA = Glu"
problem: the file was never compared with a second source. A check against UniProt would have failed at residue 2.
fix:     rule 2. tests/test_variant_facts.py::test_two_independent_sources_agree now runs on every push.
```

**Example 5 (bad).**

```
claim:   "Tumor mutational burden: reported as ultra-hypermutated (above 100 per megabase)"
problem: no assay, specimen or report existed. A literature expectation for a different class of variant was written as a patient result.
fix:     rule 5. The quantity is NOT_MEASURED until a sequencing report is on file.
```

**Example 6 (bad).**

```
claim:   a 2019 reference attributed to one first author for a statement about polymerase mutations without loss of heterozygosity
problem: the DOI resolved to a review by different authors; the PMID in the entry belonged to an unrelated paper
fix:     rule 3. references/bibliography.bib is now rebuilt from PubMed records.
```

## 4. Reasoning template for an analysis

Write the steps out. The value is that each step can be attacked separately.

1. **Question** in one sentence, with the decision it feeds.
2. **Facts in hand**, each with its ledger id.
3. **What each hypothesis predicts** for an observation that could be made. If two hypotheses predict the same thing, the observation does not separate them.
4. **Inference**, marked as inference.
5. **What would change the conclusion.**
6. **Confidence** in words, and what it rests on.

Worked on the central question:

1. Does c.138del explain this patient's polyps?
2. E01-E05 (loss-of-function carriers are not enriched and their tumours are not hypermutated), V10 (the allele cannot produce a proofreading-deficient enzyme), P01 (no tumour data), P03 (histology undocumented), E13-E14 (mosaic APC variants are common in unexplained polyposis and usually invisible in blood).
3. If POLE were the cause through faulty proofreading, polyps would carry SBS10-type signatures and a raised mutation count, as in the POLD1 family of Buchanan et al. 2025. If the cause were mosaic APC, two or more polyps would share one APC variant that is low or absent in blood. If neither, burden and signatures would be ordinary and no shared variant would appear.
4. Inference: an independent cause is more likely than POLE.
5. Any polyp with a polymerase signature; a second affected carrier of an early POLE truncation; RNA or protein evidence of an abnormal product.
6. Moderate. It rests on cohort data with a wide interval and on mechanism, not on this patient's tissue.

## 5. Search log

Append to `references/search_log.tsv` (create it on first use): date, database, exact query, records returned,
records opened, what was found.

## 6. Before committing

- [ ] `python3 analysis/variant_verification/verify_c138del.py` exits 0
- [ ] `python3 -m pytest -q tests` passes
- [ ] every new factual sentence has a ledger row
- [ ] no patient finding is written as observed without a document behind it
- [ ] new references were fetched, and their fields copied from the record
