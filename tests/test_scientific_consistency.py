"""Cross-file checks on the scientific data: every table against the sequence it describes, every document
against the table it quotes. Offline; runs on every push with the rest of tests/."""
import csv
import io
import json
import math
import os
import re
from contextlib import redirect_stdout

import fetch_clinvar_pole as clinvar
import verify_c138del as v

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REP = v.build_report()
TRANSCRIPT_GRCH38 = (132623762, 132687342)       # ENST00000320574.10, from the exon table
HOTSPOTS = {286, 297, 363, 411, 424, 456, 458, 459}   # exonuclease-domain residues named in data/POLE_clinvar_variants.tsv
AA3 = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E", "Gly": "G", "His": "H",
       "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F", "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W",
       "Tyr": "Y", "Val": "V"}
SKIP_DIRS = {".git", "tests", "__pycache__", ".pytest_cache", ".venv", "venv", "node_modules", "private"}
LOCAL_NOTES = {"todo.md", "CLAUDE.md"}        # gitignored working notes; not part of the published repository
DOI = r"10\.\d{4,9}/(?:[^\s\]>,;\"'|()]|\([^\s()]*\))+"   # allows balanced parentheses, as in 10.1016/S0140-6736(23)02268-7
PMID = r"PMID:?\s*(\d{6,9})"


def path(*parts):
    return os.path.join(ROOT, *parts)


def tsv(*parts):
    with open(path(*parts), encoding="utf-8") as fh:
        return list(csv.DictReader([l for l in fh if not l.startswith("#")], delimiter="\t"))


def markdown_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if f.endswith(".md") and not (dp == ROOT and f in LOCAL_NOTES):
                rel = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/")
                with open(os.path.join(dp, f), encoding="utf-8") as fh:
                    yield rel, fh.read()


def full_protein():
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_full.fa"))
    return cds, v.translate(cds)


def bib_entries():
    with open(path("references", "bibliography.bib"), encoding="utf-8") as fh:
        text = fh.read()
    out = {}
    for key, body in re.findall(r"@\w+\{([^,\s]+),(.*?)\n\}", text, re.S):
        doi = re.search(r"doi\s*=\s*\{([^}]+)\}", body)
        pmid = re.search(r"pmid\s*=\s*\{([^}]+)\}", body)
        out[key] = (doi.group(1).strip().lower() if doi else None, pmid.group(1).strip() if pmid else None)
    return out


# --- sequence and structure -------------------------------------------------------------------------------

def test_exon_table_is_a_complete_minus_strand_transcript():
    exons = v.read_exons(os.path.join(v.REF, "POLE_MANE_exons_GRCh38.tsv"))
    assert [n for n, _, _ in exons] == list(range(1, 50))
    assert all(s <= e for _, s, e in exons)
    assert all(exons[i][1] > exons[i + 1][2] for i in range(len(exons) - 1)), "exons must descend without overlap"
    assert (exons[-1][1], exons[0][2]) == TRANSCRIPT_GRCH38
    segs = v.cds_segments(exons)
    cds, _ = full_protein()
    assert sum(c1 - c0 + 1 for _, c0, c1, _ in segs) >= len(cds), "CDS segments must cover the whole coding sequence"
    assert segs[0][1:] == (1, 62, v.CDS_START_GRCH38) and segs[1][1:3] == (63, 204)


def test_both_domain_maps_agree_with_the_variant_and_the_hotspots():
    lit = {r["domain"]: (int(r["start"]), int(r["end"])) for r in tsv("data", "POLE_domain_boundaries.tsv")}
    db = {r["accession"]: (int(r["start"]), int(r["end"])) for r in tsv("data", "POLE_domains_interpro.tsv")}
    for name, (s, e) in list(lit.items()) + list(db.items()):
        assert 1 <= s <= e <= 2286, name
    ordered = sorted(lit.values())
    assert ordered[0][0] == 1 and ordered[-1][1] == 2286
    assert all(ordered[i][1] + 1 == ordered[i + 1][0] for i in range(len(ordered) - 1)), "literature map must tile 1-2286"
    assert lit["Exonuclease"] == db["cd05779"], "data/README.md says the CDD domain equals the narrow exonuclease range"
    for h in HOTSPOTS:
        assert lit["Exonuclease"][0] <= h <= lit["Exonuclease"][1] and db["cd05779"][0] <= h <= db["cd05779"][1], h
    stop, restart = REP["c138del"]["stop_codon_number"], REP["first_atg_after_ptc"]["codon_number"]
    catalytic = [lit["Exonuclease"], lit["Polymerase"], db["cd05779"], db["cd05535"]]
    assert all(stop < s and restart < s for s, _ in catalytic), "the stop and the Met66 restart both lie 5' of every catalytic domain"


def test_variant_table_rows_are_internally_consistent():
    _, protein = full_protein()
    lit = {r["domain"]: (int(r["start"]), int(r["end"])) for r in tsv("data", "POLE_domain_boundaries.tsv")}
    seen = set()
    for r in tsv("data", "POLE_clinvar_variants.tsv"):
        c = re.match(r"c\.(\d+)", r["variant_cdna"])
        p = re.match(r"p\.([A-Z][a-z]{2})(\d+)", r["variant_protein"])
        assert c and p, r
        codon = math.ceil(int(c.group(1)) / 3)
        assert codon == int(p.group(2)), f"{r['variant_cdna']} is codon {codon}, not {p.group(2)}"
        assert protein[codon - 1] == AA3[p.group(1)], f"{r['variant_protein']}: reference residue is {protein[codon - 1]}"
        s, e = lit["Exonuclease"] if r["domain"] == "Exonuclease" else lit["N-terminal_region"]
        assert s <= codon <= e, f"{r['variant_protein']} is outside the {r['domain']} range {s}-{e}"
        if r["clinvar_variation_id"] != "None":
            assert re.fullmatch(r"ClinVar:\d+", r["clinvar_variation_id"]), r["clinvar_variation_id"]
        assert r["variant_cdna"] not in seen
        seen.add(r["variant_cdna"])
    assert "c.138del" in seen


def test_all_methionines_table_matches_the_sequence():
    cds, protein = full_protein()
    _, utr = v.read_fasta(os.path.join(v.REF, "POLE_MANE_5utr_last6.fa"))
    seq = utr + cds
    rows = tsv("data", "POLE_all_methionines.tsv")
    assert [int(r["position_aa"][1:]) for r in rows] == [i + 1 for i, a in enumerate(protein) if a == "M"]
    for r in rows:
        n = int(r["position_aa"][1:])
        assert r["position_cdna"] == f"c.{3 * n - 2}A"
        if n == 1:
            continue                     # the table records the annotated start as n/a
        ctx, strength = v.kozak(seq, len(utr) + 3 * n - 3)
        assert (r["kozak_context"], r["kozak_strength"]) == (ctx, strength), r


# --- ClinVar population snapshot ---------------------------------------------------------------------------

def test_clinvar_snapshot_summary_is_reproducible_and_on_locus():
    name = "POLE_clinvar_PLP_2026-11-21"
    rows = tsv("data", "reference", f"{name}.tsv")
    with open(path("data", "reference", f"{name}.summary.txt"), encoding="utf-8") as fh:
        assert fh.read().rstrip("\n") == clinvar.summarise(rows), "summary.txt must be what summarise() produces from the TSV"
    assert all(clinvar.is_pole_record(r) for r in rows)
    lo, hi = TRANSCRIPT_GRCH38
    off = [r["vcv"] for r in rows
           if r["grch38_chr12_start"].isdigit() and not r["variant_type"].startswith("copy number")
           and not lo <= int(r["grch38_chr12_start"]) <= hi]
    assert not off, f"point variants outside the POLE transcript: {off}"
    vcvs = {r["vcv"] for r in rows}
    assert "VCV000548779" not in vcvs, "c.138del is classified conflicting; if it appears here ClinVar has changed"
    for r in tsv("data", "POLE_clinvar_variants.tsv"):
        if r["clinvar_variation_id"] == "None":
            continue
        vcv = "VCV" + r["clinvar_variation_id"].split(":")[1].zfill(9)
        if r["clinvar_classification"] == "Pathogenic":
            assert vcv in vcvs, f"{r['variant_protein']} is labelled Pathogenic but absent from the P/LP export"
        elif r["clinvar_classification"] == "Conflicting":
            assert vcv not in vcvs, f"{r['variant_protein']} is labelled Conflicting but present in the P/LP export"


# --- phenotype files ---------------------------------------------------------------------------------------

def test_phenopacket_and_hpo_table_describe_the_same_findings():
    with open(path("data", "phenopacket", "pole_c138del_phenopacket.json"), encoding="utf-8") as fh:
        p = json.load(fh)
    table = {r["hpo_id"]: r["hpo_term"] for r in tsv("data", "phenotype_hpo.tsv")}
    present = {f["type"]["id"]: f["type"]["label"] for f in p["phenotypicFeatures"] if not f.get("excluded")}
    excluded = {f["type"]["id"] for f in p["phenotypicFeatures"] if f.get("excluded")}
    assert set(present) == set(table), {"phenopacket_only": set(present) - set(table), "table_only": set(table) - set(present)}
    assert all(present[h] == table[h] for h in present), "labels differ between the phenopacket and the table"
    assert excluded == {"HP:0001249", "HP:0012759"}, "only the FILS/neurodevelopmental features are recorded as absent"
    assert not excluded & set(table)


def test_hpo_table_is_well_formed():
    rows = tsv("data", "phenotype_hpo.tsv")
    categories = {"Neoplastic", "Proliferative/Stromal", "Endometrial/Hormonal", "Congenital Developmental",
                  "Autoimmune/Immune", "Comorbidity"}
    for r in rows:
        assert re.fullmatch(r"HP:\d{7}", r["hpo_id"]), r
        assert r["phenotype_category"] in categories, r["phenotype_category"]
    findings = [r["finding"] for r in rows]
    assert len(findings) == len(set(findings))


def test_timeline_ages_agree_with_the_hpo_table():
    by_finding = {r["finding"]: r for r in tsv("data", "phenotype_timeline.tsv")}
    polyposis = next(r for f, r in by_finding.items() if f.startswith("Gastrointestinal polyposis"))
    thyroid = next(r for f, r in by_finding.items() if f.startswith("Stage I papillary thyroid"))
    assert polyposis["age_at_onset"] == "19" and thyroid["age_at_diagnosis"] == "~28"
    hpo = {r["hpo_id"]: r["onset"] for r in tsv("data", "phenotype_hpo.tsv")}
    assert hpo["HP:0005227"].startswith("Age 19") and hpo["HP:0002895"] == "Age ~28"
    ivc = by_finding["Duplicated inferior vena cava"]
    assert ivc["onset_type"] == "Congenital" and ivc["age_at_onset"] == "0"


def test_tissue_turnover_rows_are_sourced_and_parseable():
    allowed = ("CITED", "PHYSIOLOGY", "PARTLY SOURCED", "UNSOURCED")
    for r in tsv("data", "tissue_replication_rates.tsv"):
        assert r["source_status"].startswith(allowed), r["tissue"]
        if r["source_status"].startswith("CITED"):
            assert re.search(r"PMID\s*\d{6,9}", r["source"]), f"{r['tissue']}: CITED without a PMID"
        if r["tissue"] == "Hematopoietic stem cells":
            assert "280" in r["turnover_days"] and "40 weeks" in r["turnover_days"], "corrected 2026-11-21 from 40 days"


def test_turnover_correlation_quoted_in_text_matches_the_exact_test():
    """The audit's p = 0.067 is re-derived here; every document quoting an exact p must quote this one."""
    ns = {}
    with open(path("analysis", "temporal_phenotype", "exact_spearman_check.py"), encoding="utf-8") as fh:
        src = fh.read()
    with redirect_stdout(io.StringIO()):
        exec(compile(src, "exact_spearman_check.py", "exec"), ns)
    rho, p_two, n = ns["rho"], ns["p_two"], len(ns["x"])
    assert n == 6 and round(rho, 2) == 0.82 and round(p_two, 3) == 0.067
    quoted = {(rel, m) for rel, text in markdown_files() for m in re.findall(r"exact two-sided p = (0\.\d+)", text)}
    assert quoted and all(m == f"{p_two:.3f}" for _, m in quoted), quoted
    claims = [rel for rel, text in markdown_files() if rel != "CHANGELOG.md" and re.search(r"Spearman[^.\n]{0,80}p < 0\.05", text)]
    assert not claims, f"a significant Spearman result is still claimed in {claims}"


# --- population genetics -----------------------------------------------------------------------------------

def test_gnomad_constraint_table_is_arithmetically_consistent():
    m = {r["metric"]: r["value"] for r in tsv("data", "POLE_gnomad_constraints.tsv")}
    obs, exp = int(m["obs_lof"]), float(m["exp_lof"])
    assert round(obs / exp, 2) == float(m["oe_lof"])
    assert float(m["oe_lof"]) < float(m["LOEUF"]), "LOEUF is the upper bound of the oe_lof interval"
    assert 0 <= float(m["pLI"]) <= 1
    for rel, text in markdown_files():
        if rel == "CHANGELOG.md":
            continue
        for val in re.findall(r"LOEUF\s*(?:=|of|:)?\s*(0\.\d+)", text):
            assert val == m["LOEUF"], f"{rel} quotes LOEUF {val}"
        for val in re.findall(r"oe_lof\s*(?:=|of|:)?\s*(0\.\d+)", text):
            assert float(m["oe_lof"]) == round(float(val), 2), f"{rel} quotes oe_lof {val}"


def test_gnomad_allele_counts_quoted_in_text_match_the_ledger():
    ledger = {r["claim_id"]: r for r in tsv("data", "claims_ledger.tsv")}
    counts = re.findall(r"1 of ([\d,]+)", ledger["D04"]["value"] + " " + ledger["D05"]["value"])
    assert "1,461,874" in counts and "31,386" in counts
    for rel, text in markdown_files():
        for an in re.findall(r"1 of ([\d,]+) (?:gnomAD )?v4\.1 exome", text):
            assert an == "1,461,874", f"{rel} quotes {an}"
        for an in re.findall(r"1 of ([\d,]+) (?:gnomAD )?v2\.1\.1 genome", text):
            assert an == "31,386", f"{rel} quotes {an}"


# --- documents against the derivation ---------------------------------------------------------------------

def test_key_numbers_quoted_in_documents_match_the_derivation():
    c, restart = REP["c138del"], REP["first_atg_after_ptc"]
    checks = {
        r"(\d+)-residue (?:product|peptide)": str(c["truncated_length_aa"]),
        r"premature stop at codon (\d+)": str(c["stop_codon_number"]),
        r"exon 2 of (\d+)": "49",
        r"codon \d+ of ([\d,]+)": "2,286",
        r"next (?:in-frame )?AUG(?: after the stop)? is Met(\d+)": str(restart["codon_number"]),
    }
    problems = []
    for rel, text in markdown_files():
        if rel == "CHANGELOG.md":
            continue
        for pat, want in checks.items():
            for got in re.findall(pat, text):
                if got != want:
                    problems.append(f"{rel}: /{pat}/ gives {got}, derivation says {want}")
    assert not problems, "\n".join(problems)


def test_identifiers_quoted_in_documents_match_the_derivation():
    g = REP["genomic"]
    grch38, grch37 = g["GRCh38"]["hgvs_g"], g["GRCh37"]["hgvs_g"]
    assert (grch38, grch37) == ("NC_000012.12:g.132681204del", "NC_000012.11:g.133257790del")
    for rel, text in markdown_files():
        for m in re.findall(r"NC_000012\.12:g\.(\d+)del", text):
            assert m == str(g["GRCh38"]["pos_deleted_base"]), f"{rel} quotes GRCh38 g.{m}del"
        for m in re.findall(r"NC_000012\.11:g\.(\d+)del", text):
            assert m == str(g["GRCh37"]["pos_deleted_base"]), f"{rel} quotes GRCh37 g.{m}del"
    with open(path("README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    assert all(w in readme for w in (grch38, grch37, g["GRCh38"]["vcf"], "VCV000548779", "rs1555230420"))


# --- citations and ledger ----------------------------------------------------------------------------------

def test_bibliography_identifiers_are_well_formed_and_unique():
    entries = bib_entries()
    dois = [d for d, _ in entries.values() if d]
    pmids = [p for _, p in entries.values() if p]
    assert len(dois) == len(set(dois)) and len(pmids) == len(set(pmids))
    for key, (doi, pmid) in entries.items():
        assert doi or pmid, f"{key} has neither DOI nor PMID"
        assert doi is None or re.fullmatch(r"10\.\d{4,9}/\S+", doi), f"{key}: malformed DOI {doi}"
        assert pmid is None or re.fullmatch(r"\d{6,9}", pmid), f"{key}: malformed PMID {pmid}"
    for r in tsv("references", "bibliography_corrections.tsv"):
        assert r["new_key"] == "(removed)" or r["new_key"] in entries, f"corrections table names {r['new_key']}, which is not in the bibliography"


def test_every_doi_and_pmid_cited_in_text_is_catalogued():
    entries = bib_entries()
    with open(path("data", "claims_ledger.tsv"), encoding="utf-8") as fh:
        ledger = fh.read()
    known_doi = {d for d, _ in entries.values() if d} | {d.rstrip(".").lower() for d in re.findall(DOI, ledger)}
    known_pmid = {p for _, p in entries.values() if p} | set(re.findall(PMID, ledger))
    missing = []
    for rel, text in markdown_files():
        for d in set(d.rstrip(".").lower() for d in re.findall(DOI, text)):
            if d not in known_doi:
                missing.append(f"{rel}: doi {d}")
        for p in set(re.findall(PMID, text)):
            if p not in known_pmid:
                missing.append(f"{rel}: PMID {p}")
    assert not missing, "cited but in neither bibliography.bib nor claims_ledger.tsv:\n" + "\n".join(missing)


def test_every_cosmic_signature_named_in_text_is_catalogued():
    catalogued = {r["signature"] for r in tsv("data", "cosmic_signatures_cited.tsv")}
    named = set()
    for rel, text in markdown_files():
        named |= {a + b for a, b in re.findall(r"\b(SBS\d+)([a-z]?)\b", text)}
        named |= {"SBS" + n for pair in re.findall(r"\bSBS(\d+)/(\d+)\b", text) for n in pair}       # "SBS2/13"
        named |= {a + s for a, b, c in re.findall(r"\b(SBS\d+)([a-z])/([a-z])\b", text) for s in (b, c)}  # "SBS10a/b"
    named.discard("SBS10")    # "SBS10-type" is used as a family name
    assert named <= catalogued, f"named in text but not in data/cosmic_signatures_cited.tsv: {sorted(named - catalogued)}"


def test_ledger_rows_cited_in_documents_exist_and_are_sourced():
    rows = {r["claim_id"]: r for r in tsv("data", "claims_ledger.tsv")}
    cited = set()
    for rel, text in markdown_files():
        cited |= set(re.findall(r"(?:ledger(?: rows?)?|rows?)\s+([VDLPECBN]\d{2})", text))
        for a, b in re.findall(r"\b([VDLPECBN]\d{2})-(\d{2})\b", text):
            cited |= {f"{a[0]}{i:02d}" for i in range(int(a[1:]), int(b) + 1)}
    assert cited <= set(rows), f"cited but not in the ledger: {sorted(cited - set(rows))}"
    locatable = re.compile(r"10\.\d{4,9}/|PMID|\.py|\.tsv|REST|API|https?://|VCV\d|rs\d+|HP:\d|ClinVar|gnomAD|Ensembl|UniProt|HPO|"
                           r"InterPro|E-utilities|PubMed|LOVD|cancer\.sanger|tests/|COSMIC|OMIM|HGNC|dbSNP|ClinGen|Pfam|CDD", re.I)
    for cid, r in rows.items():
        if r["status"] == "VERIFIED":
            assert locatable.search(r["source"]), f"{cid} is VERIFIED but its source is not an identifier: {r['source']}"
        if r["status"] == "NOT_FOUND":
            assert r["how_checked"].strip(), f"{cid}: a NOT_FOUND row must record the query"


# --- repository hygiene ------------------------------------------------------------------------------------

def test_checksums_cover_every_data_file():
    with open(path("data", "checksums.sha256"), encoding="utf-8") as fh:
        listed = {line.split()[1] for line in fh if line.strip()}
    actual = set()
    for dp, dn, fn in os.walk(path("data")):
        for f in fn:
            if f.endswith((".tsv", ".fa", ".json", ".txt")):
                actual.add(os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/"))
    assert actual == listed, {"unlisted": sorted(actual - listed), "listed_but_absent": sorted(listed - actual)}


# --- timeline against the turnover table ------------------------------------------------------------------

def parse_turnover_days(s):
    """'3-5' -> 4, '~28 (monthly)' -> 28, '200-300' -> 250, 'Variable (~hormonal)' -> None."""
    m = re.match(r"~?(\d+)(?:-(\d+))?", s.strip())
    if not m:
        return None
    lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
    return (lo + hi) / 2


def parse_age(s):
    m = re.fullmatch(r"~?(\d+)", s.strip())
    return int(m.group(1)) if m else None


def test_timeline_tissue_keys_join_the_turnover_table():
    rates = {r["tissue"]: r for r in tsv("data", "tissue_replication_rates.tsv")}
    rows = tsv("data", "phenotype_timeline.tsv")
    keyed = [r for r in rows if r["tissue_key"]]
    assert len(keyed) >= 10, "most findings should key into a turnover row"
    for r in keyed:
        assert r["tissue_key"] in rates, f"{r['finding']}: tissue_key '{r['tissue_key']}' is not a row of tissue_replication_rates.tsv"
        if r["tissue_turnover_rate"].startswith("N/A"):
            continue
        label, ref = r["tissue_turnover_rate"].split(" (")[0], rates[r["tissue_key"]]["estimated_turnover"]
        assert ref.lower().startswith(label.lower().split("-")[0]), \
            f"{r['finding']}: timeline says '{r['tissue_turnover_rate']}', turnover table says '{ref}'"
    for r in rows:
        if not r["tissue_key"]:
            assert r["phenotype_category"] in ("Comorbidity",), f"{r['finding']} has no tissue_key but is not a comorbidity"


def test_notebook_dataset_versus_the_tables():
    """The n = 6 dataset behind rho = 0.82, p = 0.067 (analysis/temporal_phenotype) is reproduced from the two
    tables except for two entries the tables do not support: breast turnover (unsourced 'Variable') and
    adenomyosis as a tissue separate from endometrium. Anyone who sources those values must re-derive the statistic."""
    rates = {r["tissue"]: parse_turnover_days(r["turnover_days"]) for r in tsv("data", "tissue_replication_rates.tsv")}
    derived = {}
    for r in tsv("data", "phenotype_timeline.tsv"):
        age, key = parse_age(r["age_at_diagnosis"]), r["tissue_key"]
        if age is None or age == 0 or not key or rates.get(key) is None:
            continue
        t, a = derived.get(key, (rates[key], 10 ** 9))
        derived[key] = (rates[key], min(a, age))
    assert derived == {"Colonic crypt epithelium": (4, 19), "Gastric epithelium": (5, 19),
                       "Endometrium": (28, 22), "Thyroid epithelium": (2920, 28)}, derived
    ns = {}
    with open(path("analysis", "temporal_phenotype", "exact_spearman_check.py"), encoding="utf-8") as fh:
        src = fh.read()
    with redirect_stdout(io.StringIO()):
        exec(compile(src, "exact_spearman_check.py", "exec"), ns)
    notebook = dict(ns["tissues"])
    alias = {"Colonic epithelium": "Colonic crypt epithelium"}
    supported = {alias.get(k, k): v for k, v in notebook.items() if alias.get(k, k) in derived}
    assert supported == derived, "the notebook's values no longer match the tables; re-derive rho and p"
    unsupported = {k: v for k, v in notebook.items() if alias.get(k, k) not in derived}
    assert unsupported == {"Breast stroma": (60, 27), "Endometrium/myometrium": (28, 28)}, unsupported


def test_phenotype_categories_agree_between_timeline_and_hpo_table():
    timeline = {r["finding"]: r["phenotype_category"] for r in tsv("data", "phenotype_timeline.tsv")}
    hpo = {r["finding"]: r["phenotype_category"] for r in tsv("data", "phenotype_hpo.tsv")}
    shared = set(timeline) & set(hpo)
    assert len(shared) >= 8
    assert not [f for f in shared if timeline[f] != hpo[f]], \
        {f: (timeline[f], hpo[f]) for f in shared if timeline[f] != hpo[f]}


# --- figures against the data they are built from ---------------------------------------------------------

def svg_text(p):
    import html
    with open(p, encoding="utf-8") as fh:
        raw = fh.read()
    out = []
    for t in re.findall(r"<text[^>]*>(.*?)</text>", raw, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
        if t:
            out.append(t)
    return sorted(out)


def test_committed_figures_carry_the_same_labels_as_a_fresh_build(tmp_path):
    """Regenerates the README figures into a temporary directory and compares every text label (numbers, names,
    captions) with the committed SVGs. Rendering may differ between matplotlib versions; the labels may not."""
    pytest = __import__("pytest")
    pytest.importorskip("matplotlib")
    import subprocess
    import sys
    env = {**os.environ, "POLE_FIGURES_OUT": str(tmp_path)}
    subprocess.run([sys.executable, path("analysis", "figures", "make_figures.py")], check=True, env=env,
                   stdout=subprocess.DEVNULL, cwd=ROOT)
    names = ["c138del_codons", "c138del_translation_map", "pole_exon1-2_truncations", "lof_evidence",
             "claims_ledger_status", "clinical_timeline"]
    stale = []
    for n in names:
        fresh, committed = svg_text(tmp_path / f"{n}.svg"), svg_text(path("figures", f"{n}.svg"))
        if fresh != committed:
            only_fresh = sorted(set(fresh) - set(committed))[:5]
            only_committed = sorted(set(committed) - set(fresh))[:5]
            stale.append(f"figures/{n}.svg: fresh-only {only_fresh}, committed-only {only_committed}")
    assert not stale, "regenerate with python3 analysis/figures/make_figures.py:\n" + "\n".join(stale)
