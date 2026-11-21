"""Guards against the claims retired by the 2026-11-20 audit coming back, and checks the machine-readable files."""
import csv
import hashlib
import json
import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TEXT_EXT = (".md", ".tsv", ".json", ".py", ".cff", ".yml")
# Files that describe the retired claims and therefore have to quote them.
EXEMPT = {"CHANGELOG.md", "docs/VERIFICATION_AUDIT_2026-11-20.md", "docs/EVIDENCE_PROTOCOL.md", "data/claims_ledger.tsv",
          "references/bibliography_corrections.tsv", "references/bibliography.bib",
          "data/POLE_all_methionines.tsv"}  # generated from the full CDS; M444 happens to be a real methionine
# pattern -> (why it is retired, regex that makes a line acceptable because it explains the retirement)
RETIRED = {
    r"133249847": ("GRCh37 position of c.1376, not of c.138del", r"c\.1376|legacy"),
    r"ENST00000320574\.6\b": ("MANE Select is version .10", None),
    r"1,614,586": ("the variant is not absent from gnomAD", None),
    r"612591": ("OMIM 612591 is CRCS10 (POLD1); CRCS12 is 615083", r"CRCS10|POLD1"),
    r"Glu46|= GAA = Glu|Glu \(not Leu\)": ("codon 46 is TTG (Leu)", r"non-POLE|not POLE|was not POLE"),
    r"\bM(89|128|185|292|331|444|497|530|634)\b": ("methionines computed from a non-POLE sequence", r"not POLE|non-POLE"),
    r"residue 54\b|54-residue|53[–-]54": ("the stop is codon 53; the product is 52 residues", None),
    r"[Aa]bsent from ClinVar|Not_reported": ("the variant is ClinVar VCV000548779", r"superseded|Not in ClinVar"),
    r"Barbari|Pietrantonio et al|Shinbrot et al|Valle et al\.? \(?2020": ("misattributed citation", r"not Shinbrot|Tomlinson and Valle"),
    r"\"SOLVED\"|\"CAUSATIVE\"": ("the case is not solved", None),
}
TMB = re.compile(r"(>|≥|above )\s?100\s?(mut(ations)?\s?/\s?Mb|mutations per megabase)"
                 r"|ultra-?hypermutat\w*\s+(in the\s+)?POLE c\.138del tumou?r|reported ultra-?hypermutat", re.I)
BANNER = "Audit note, 2026-11-20"


def text_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "tests", "__pycache__", ".pytest_cache", ".venv", "venv", "node_modules", "private")]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/")
            if f.endswith(TEXT_EXT) and rel not in EXEMPT:
                with open(os.path.join(dp, f), encoding="utf-8") as fh:
                    yield rel, fh.read()


def document_texts():
    """Text of every .docx/.pptx (XML inside the zip) and .ipynb (cell sources) in the repository."""
    import html
    import json
    import zipfile
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "tests", "__pycache__", ".pytest_cache", ".venv", "venv", "node_modules", "private")]
        for f in fn:
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            if f.endswith((".docx", ".pptx")):
                with zipfile.ZipFile(path) as z:
                    parts = [n for n in z.namelist() if n.endswith(".xml") and ("word/document" in n or "ppt/slides/slide" in n)]
                    xml = " ".join(z.read(n).decode("utf-8", "ignore") for n in parts)
                yield rel, html.unescape(re.sub(r"<[^>]+>", " ", xml))
            elif f.endswith(".ipynb"):
                with open(path, encoding="utf-8") as fh:
                    nb = json.load(fh)
                yield rel, "\n".join("".join(c.get("source", [])) for c in nb.get("cells", []))


def test_documents_and_notebooks_carry_no_retired_claims():
    """Office files and notebooks are not line-scanned above; they get the same patterns, with no waivers, and the TMB guard."""
    problems = []
    for rel, text in document_texts():
        for pat, (why, _waiver) in RETIRED.items():
            if re.search(pat, text):
                problems.append(f"{rel}: /{pat}/ ({why})")
        if TMB.search(text):
            problems.append(f"{rel}: states a tumour mutational burden that was never measured")
    assert not problems, "\n".join(problems)


def test_retired_claims_do_not_return():
    problems = []
    for rel, text in text_files():
        for i, line in enumerate(text.split("\n"), 1):
            for pat, (why, waiver) in RETIRED.items():
                if re.search(pat, line) and not (waiver and re.search(waiver, line)):
                    problems.append(f"{rel}:{i}: /{pat}/ ({why})")
    assert not problems, "\n".join(problems)


def test_unmeasured_tmb_is_always_flagged():
    # the issue template is a blank form for other carriers; its placeholder text is not a claim about this patient
    missing = [rel for rel, text in text_files()
               if TMB.search(text) and BANNER not in text and not rel.startswith(".github/ISSUE_TEMPLATE/")]
    assert not missing, f"files stating a tumour mutational burden without the audit note: {missing}"


def test_phenopacket_does_not_overstate():
    with open(os.path.join(ROOT, "data/phenopacket/pole_c138del_phenopacket.json"), encoding="utf-8") as fh:
        p = json.load(fh)
    it = p["interpretations"][0]
    gi = it["diagnosis"]["genomicInterpretations"][0]
    assert it["progressStatus"] == "IN_PROGRESS" and gi["interpretationStatus"] == "CANDIDATE"
    assert gi["variantInterpretation"]["therapeuticActionability"] == "UNKNOWN_ACTIONABILITY"
    assert it["diagnosis"]["disease"]["id"] == "OMIM:615083" and p["diseases"] == []
    assert not [f for f in p["phenotypicFeatures"] if "TMB" in f.get("description", "")]
    vd = gi["variantInterpretation"]["variationDescriptor"]
    assert {e["value"] for e in vd["expressions"]} >= {"NM_006231.4:c.138del", "NC_000012.12:g.132681204del"}
    assert (vd["vcfRecord"]["pos"], vd["vcfRecord"]["ref"], vd["vcfRecord"]["alt"]) == ("132681203", "GC", "G")


def test_claims_ledger_is_well_formed():
    with open(os.path.join(ROOT, "data/claims_ledger.tsv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    assert len(rows) >= 40
    ids = [r["claim_id"] for r in rows]
    assert len(ids) == len(set(ids))
    for r in rows:
        assert r["status"] in {"VERIFIED", "CONTRADICTED", "UNVERIFIED", "NOT_FOUND", "INFERENCE", "NOT_MEASURED", "OWNER_STATEMENT"}, r
        assert r["source"].strip() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["checked"]), r


def test_bibliography_keys():
    with open(os.path.join(ROOT, "references/bibliography.bib"), encoding="utf-8") as fh:
        keys = re.findall(r"^@\w+\{([^,\s]+),", fh.read(), re.M)
    assert len(keys) == len(set(keys)) == 89
    assert not {"valle2020", "shinbrot2019", "barbari2019", "pietrantonio2024", "baranovskiy2022", "deppas2025", "pich2025b"} & set(keys)
    assert {"mur2020", "yamaguchi2019", "park2019", "ambrosini2024", "lisova2022"} <= set(keys)


def test_checksums():
    with open(os.path.join(ROOT, "data/checksums.sha256"), encoding="utf-8") as fh:
        for line in fh:
            digest, rel = line.split()
            with open(os.path.join(ROOT, rel), "rb") as f:
                assert hashlib.sha256(f.read()).hexdigest() == digest, rel


def test_readme_figures_exist():
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        paths = re.findall(r"!\[[^\]]*\]\(([^)]+\.png)\)", fh.read())
    assert len(paths) >= 8
    missing = [p for p in paths if not os.path.exists(os.path.join(ROOT, p))]
    assert not missing, missing
