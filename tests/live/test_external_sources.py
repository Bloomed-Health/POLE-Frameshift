"""Checks against the live databases the repository quotes. Opt-in: set POLE_LIVE=1.

    POLE_LIVE=1 python3 -m pytest -q tests/live

Each test compares a fixture or a ledger value with what the source returns today. A failure means the world
has changed (a reclassification, a new carrier, a new publication, a fixture drift) and names the ledger row
to update. Standard library only; NCBI calls stay under the 3-per-second limit for unauthenticated use."""
import csv
import json
import os
import re
import time
import urllib.parse
import urllib.request

import pytest
import verify_c138del as v

pytestmark = pytest.mark.skipif(os.environ.get("POLE_LIVE") != "1", reason="live network checks; set POLE_LIVE=1")

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
UA = {"User-Agent": "POLE-Frameshift live checks (github.com/Bloomed-Health/POLE-Frameshift)"}
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def get(url, data=None, headers=None, retries=3):
    req = urllib.request.Request(url, data=data, headers={**UA, "Accept": "application/json", **(headers or {})})
    for attempt in range(retries):
        try:
            return urllib.request.urlopen(req, timeout=60).read().decode()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def get_json(url, **kw):
    return json.loads(get(url, **kw))


def tsv(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return list(csv.DictReader([l for l in fh if not l.startswith("#")], delimiter="\t"))


def ledger():
    return {r["claim_id"]: r for r in tsv("data", "claims_ledger.tsv")}


# --- the variant in the databases ----------------------------------------------------------------------

def test_clinvar_c138del_classification_unchanged():
    """Ledger D01: conflicting, three submitters. A change here is the first thing a reader would want to know."""
    d = get_json(EUTILS + "esummary.fcgi?db=clinvar&id=548779&retmode=json")["result"]["548779"]
    assert d["title"] == "NM_006231.4(POLE):c.138del (p.Leu46fs)"
    assert d["germline_classification"]["description"] == "Conflicting classifications of pathogenicity", \
        f"ClinVar now says: {d['germline_classification']['description']}; update ledger D01 and every file that quotes it"
    scvs = set(d["supporting_submissions"]["scv"])
    assert scvs == {"SCV000785494", "SCV000834648", "SCV006397458"}, f"submissions changed: {sorted(scvs)}; update ledger D01"


def test_gnomad_allele_counts_unchanged():
    """Ledger D04/D05: one v4.1 exome carrier and one v2.1.1 genome carrier. A new allele means a new carrier."""
    def counts(variant_id, dataset):
        q = '{variant(variantId:"%s", dataset:%s){exome{ac an} genome{ac an}}}' % (variant_id, dataset)
        d = get_json("https://gnomad.broadinstitute.org/api", data=json.dumps({"query": q}).encode(),
                     headers={"Content-Type": "application/json"})["data"]["variant"]
        return {k: (x["ac"], x["an"]) for k, x in d.items() if x}
    assert counts("12-132681203-GC-G", "gnomad_r4") == {"exome": (1, 1461874)}, "gnomAD v4.1 changed; update ledger D04"
    assert counts("12-133257789-GC-G", "gnomad_r2_1") == {"genome": (1, 31386)}, "gnomAD v2.1.1 changed; update ledger D05"


def test_spliceai_scores_unchanged():
    """Ledger V13: all four delta scores 0 on the MANE transcript (Ensembl VEP SpliceAI plugin)."""
    d = get_json("https://rest.ensembl.org/vep/human/region/12:132681204-132681204:1/-?SpliceAI=1&transcript_id=ENST00000320574",
                 headers={"Content-Type": "application/json"})
    tc = next(t for t in d[0]["transcript_consequences"] if t["transcript_id"] == "ENST00000320574")
    assert "frameshift_variant" in tc["consequence_terms"]
    scores = {k: tc["spliceai"][k] for k in ("DS_AG", "DS_AL", "DS_DG", "DS_DL")}
    assert all(s == 0 for s in scores.values()), f"SpliceAI now reports {scores}; update ledger V13"


def test_no_publication_names_the_variant_yet():
    """Ledger D11 is NOT_FOUND. A hit here is good news and must be read and recorded."""
    term = 'POLE AND ("c.138del" OR "Leu46Phefs" OR "L46Ffs" OR "Leu46fs")'
    d = get_json(EUTILS + "esearch.fcgi?db=pubmed&retmode=json&term=" + urllib.parse.quote(term))["esearchresult"]
    assert d["count"] == "0", f"PubMed now returns {d['count']} record(s) for {term}: {d['idlist']}; read them and update ledger D11"


# --- reference fixtures against their sources -----------------------------------------------------------

def test_mane_transcript_and_cds_fixture_unchanged():
    """Ledger V02 and the fixtures in data/reference/: the transcript version and the coding sequence."""
    info = get_json("https://rest.ensembl.org/lookup/id/ENST00000320574?content-type=application/json")
    assert info["version"] == 10 and info["assembly_name"] == "GRCh38", f"transcript is now version {info['version']}"
    live = get("https://rest.ensembl.org/sequence/id/ENST00000320574?type=cds;content-type=text/plain").strip()
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_full.fa"))
    assert live == cds, "the live Ensembl CDS differs from data/reference/POLE_MANE_cds_full.fa; run scripts/fetch_reference.py"


def test_uniprot_sequence_matches_translation():
    text = get("https://rest.uniprot.org/uniprotkb/Q07864.fasta", headers={"Accept": "text/plain"})
    live = "".join(l.strip() for l in text.splitlines() if not l.startswith(">"))
    _, cds = v.read_fasta(os.path.join(v.REF, "POLE_MANE_cds_full.fa"))
    assert v.translate(cds).rstrip("*") == live, "UniProt Q07864 no longer equals the translated MANE CDS"


def test_exon_table_matches_live_ensembl():
    """Ledger D15."""
    d = get_json("https://rest.ensembl.org/lookup/id/ENST00000320574?expand=1;content-type=application/json")
    live = sorted(((e["start"], e["end"]) for e in d["Exon"]), reverse=True)
    fixture = [(s, e) for _, s, e in v.read_exons(os.path.join(v.REF, "POLE_MANE_exons_GRCh38.tsv"))]
    assert live == fixture, "exon coordinates changed; regenerate data/reference/POLE_MANE_exons_GRCh38.tsv"


def test_hpo_terms_resolve_and_labels_match():
    """Ledger N03: every HPO identifier in the phenotype table and the phenopacket."""
    with open(os.path.join(ROOT, "data", "phenopacket", "pole_c138del_phenopacket.json"), encoding="utf-8") as fh:
        pp = json.load(fh)
    wanted = {r["hpo_id"]: r["hpo_term"] for r in tsv("data", "phenotype_hpo.tsv")}
    wanted.update({f["type"]["id"]: f["type"]["label"] for f in pp["phenotypicFeatures"]})
    wrong = []
    for hid, label in sorted(wanted.items()):
        d = get_json(f"https://ontology.jax.org/api/hp/terms/{hid}")
        if d.get("isObsolete") or d["name"] != label:
            wrong.append(f"{hid}: repository says '{label}', HPO says '{d['name']}' (obsolete={d.get('isObsolete')})")
    assert not wrong, "\n".join(wrong)


# --- bibliography against PubMed ---------------------------------------------------------------------------

def bib_entries():
    with open(os.path.join(ROOT, "references", "bibliography.bib"), encoding="utf-8") as fh:
        text = fh.read()
    out = {}
    for key, body in re.findall(r"@\w+\{([^,\s]+),(.*?)\n\}", text, re.S):
        f = dict(re.findall(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*\n", body, re.S))
        out[key] = f
    return out


def test_pubmed_records_match_bibliography():
    """The check that found 34 wrong entries in the audit: PMID -> first author surname, year and (loosely) title."""
    entries = {k: f for k, f in bib_entries().items() if f.get("pmid")}
    ids = [f["pmid"] for f in entries.values()]
    results = {}
    for i in range(0, len(ids), 100):
        d = get_json(EUTILS + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids[i:i + 100]))["result"]
        results.update({k: x for k, x in d.items() if k != "uids"})
        time.sleep(0.4)
    problems = []
    for key, f in entries.items():
        rec = results.get(f["pmid"])
        if not rec or "error" in rec:
            problems.append(f"{key}: PMID {f['pmid']} did not resolve")
            continue
        def surname(s):
            s = re.sub(r"^\{?\s*(the\s+)?", "", s.lower())       # "{The Cancer Genome Atlas ...}" -> "cancer ..."
            m = re.search(r"[a-zà-ÿ]+", s)
            return m.group(0) if m else ""
        first = surname(rec["authors"][0]["name"]) if rec.get("authors") else ""
        bib_first = surname(f.get("author", ""))
        year = rec.get("pubdate", "")[:4]
        title_words = set(re.findall(r"[a-z]{5,}", f.get("title", "").lower()))
        rec_words = set(re.findall(r"[a-z]{5,}", rec.get("title", "").lower()))
        overlap = len(title_words & rec_words) / max(1, len(title_words))
        if first and bib_first and not (first.startswith(bib_first[:4]) or bib_first.startswith(first[:4])):
            problems.append(f"{key}: first author '{f.get('author', '')[:30]}' vs PubMed '{rec['authors'][0]['name']}'")
        if year and f.get("year") and abs(int(year) - int(f["year"])) > 1:
            problems.append(f"{key}: year {f['year']} vs PubMed {year}")
        if overlap < 0.5:
            problems.append(f"{key}: title overlap {overlap:.0%} with PubMed '{rec.get('title', '')[:60]}'")
    assert not problems, "\n".join(problems)


# --- population snapshot drift -----------------------------------------------------------------------------

def test_clinvar_pole_plp_population_has_not_drifted_far():
    """Ledger D16: 497 P/LP POLE records on 2026-11-21. More than 10% change means the snapshot and the numbers
    quoted from it in docs/pole_variant_comparison.md should be refreshed with fetch_clinvar_pole.py."""
    import fetch_clinvar_pole as c
    ids = c.search_ids()
    snapshot = len(tsv("data", "reference", "POLE_clinvar_PLP_2026-11-21.tsv"))
    assert abs(len(ids) - snapshot) <= 0.1 * snapshot, f"ClinVar now returns {len(ids)} records (snapshot {snapshot})"


# --- the exon 1-2 neighbours -------------------------------------------------------------------------------

TRUNCATING_CONSEQUENCES = {"start_lost", "stop_gained", "frameshift_variant", "splice_donor_variant"}
EXON_REGIONS = ("12:132687254-132687342", "12:132681138-132681279")     # exon 1 CDS part, exon 2; see the fixture header


def test_no_new_truncating_alleles_in_exons_1_2():
    """data/reference/POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv: a new record is a potential carrier and must
    be added to the fixture (nterm_truncations.py then models it)."""
    live = {}
    for region in EXON_REGIONS:
        for x in get_json(f"https://rest.ensembl.org/overlap/region/human/{region}?feature=variation",
                          headers={"Content-Type": "application/json"}):
            if x.get("consequence_type") in TRUNCATING_CONSEQUENCES:
                live[x["id"]] = (x["consequence_type"], x["start"], x["end"], "/".join(x.get("alleles", [])))
    fixture = {r["rsid"] for r in tsv("data", "reference", "POLE_exon1-2_truncating_dbsnp_2026-11-20.tsv")}
    new = {k: v for k, v in live.items() if k not in fixture}
    gone = fixture - set(live) - {"ClinVar:c.137dup"}
    assert not new, f"new truncating records in exons 1-2: {new}; add them to the fixture"
    assert not gone, f"records in the fixture that Ensembl no longer returns: {gone}"


def test_nterm_truncation_predictions_match_ensembl_vep():
    """Every allele modelled by nterm_truncations.py gets the same protein consequence from Ensembl VEP."""
    import nterm_truncations as nt
    rows = [r for r in nt.rows() if "hgvs_c" in r]
    assert len(rows) >= 30
    body = json.dumps({"hgvs_notations": [f"ENST00000320574:{r['hgvs_c']}" for r in rows]}).encode()
    out = get_json("https://rest.ensembl.org/vep/human/hgvs?hgvs=1", data=body, headers={"Content-Type": "application/json"})
    by_input = {x["input"].split(":", 1)[1]: x for x in out}
    problems = []
    for r in rows:
        x = by_input.get(r["hgvs_c"])
        tc = next((t for t in x.get("transcript_consequences", []) if t["transcript_id"] == "ENST00000320574"), None) if x else None
        if tc is None:
            problems.append(f"{r['hgvs_c']}: no VEP result")
            continue
        vep_p = (tc.get("hgvsp") or "").split(":")[-1].replace("Ter", "*")
        ours = r["hgvs_p"].replace("Ter", "*")
        if vep_p != ours:
            problems.append(f"{r['hgvs_c']}: nterm_truncations says {ours}, VEP says {vep_p or tc.get('consequence_terms')}")
        expected_term = {"nonsense": "stop_gained", "frameshift": "frameshift_variant", "start_lost": "start_lost"}[r["kind"]]
        if expected_term not in tc["consequence_terms"]:
            problems.append(f"{r['hgvs_c']}: kind {r['kind']} but VEP terms {tc['consequence_terms']}")
    assert not problems, "\n".join(problems)


# --- LOVD ----------------------------------------------------------------------------------------------------

def test_lovd_entry_reflects_the_correction():
    """data/lovd_update_2026-11-20.md asks the curator to change three fields of variant #0001074000. Until
    the change is live this test skips; it fails only if the entry disappears or its genomic description changes."""
    import urllib.error
    url = "https://databases.lovd.nl/shared/api/rest/variants/POLE?format=application/json&search_position=g.132681204"
    try:
        text = get(url)
    except urllib.error.HTTPError as e:
        if e.code == 403:
            pytest.skip("LOVD refuses scripted access (403); check https://databases.lovd.nl/shared/variants/0001074000 by hand")
        raise
    assert "POLE_000381" in text and "132681204" in text, "the LOVD entry for c.138del was not found at its genomic position"
    if "Effect unknown" not in text:
        pytest.skip("LOVD still shows the pre-audit functional-effect field; the correction in data/lovd_update_2026-11-20.md is pending")


# --- DOIs against Crossref --------------------------------------------------------------------------------

def test_bibliography_dois_resolve_to_the_cited_titles():
    """Every DOI in bibliography.bib resolves at Crossref (or at doi.org) and its registered title overlaps the bib title."""
    import urllib.error
    entries = {k: f for k, f in bib_entries().items() if f.get("doi")}
    problems = []
    for key, f in entries.items():
        doi = f["doi"].strip()
        try:
            msg = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"),
                           headers={"User-Agent": UA["User-Agent"] + " (mailto:research@bloomed.health)"})["message"]
            title = " ".join(msg.get("title") or [])
        except urllib.error.HTTPError as e:
            if e.code != 404:
                problems.append(f"{key}: Crossref HTTP {e.code} for {doi}")
                continue
            try:                                        # not a Crossref DOI (DataCite, etc.): it still has to resolve
                urllib.request.urlopen(urllib.request.Request("https://doi.org/" + doi, method="HEAD", headers=UA), timeout=60)
            except urllib.error.HTTPError as e2:
                problems.append(f"{key}: DOI {doi} does not resolve (HTTP {e2.code})")
            continue
        bib_words = set(re.findall(r"[a-z]{5,}", f.get("title", "").lower()))
        reg_words = set(re.findall(r"[a-z]{5,}", title.lower()))
        overlap = len(bib_words & reg_words) / max(1, len(bib_words))
        if overlap < 0.5:
            problems.append(f"{key}: DOI {doi} is registered as '{title[:70]}' (title overlap {overlap:.0%})")
        time.sleep(0.2)
    assert not problems, "\n".join(problems)
