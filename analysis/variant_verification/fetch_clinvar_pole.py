#!/usr/bin/env python3
"""Export every ClinVar POLE record with a germline classification of Pathogenic or Likely pathogenic.

Needs network access (NCBI E-utilities). Standard library only. Writes a dated TSV and a summary next to it:

    python3 analysis/variant_verification/fetch_clinvar_pole.py            # writes data/reference/POLE_clinvar_PLP_<date>.tsv
    python3 analysis/variant_verification/fetch_clinvar_pole.py --out x.tsv

Why: the hand-curated table data/POLE_clinvar_variants.tsv holds a few literature variants. Statements such as
"truncating POLE variants are classified Pathogenic for the recessive syndromes, not for PPAP" need the whole
population of records, with the date they were pulled. This script provides that population; it does not interpret it.

Summary categories (from ClinVar's own fields, no re-annotation):
  consequence: ClinVar molecular_consequence_list collapsed to truncating (nonsense / frameshift / splice) versus
               missense versus other
  condition:   trait names as submitted, grouped by the OMIM number when present
               615083 = CRCS12 (PPAP, dominant); 618336 = IMAGe-I; 615139 = FILS (both recessive)
  exonuclease: missense records whose protein position (parsed from the title) lies in 268-471
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY = ('POLE[gene] AND ("clinsig pathogenic"[Properties] OR "clinsig likely pathogenic"[Properties] '
         'OR "clinsig pathogenic low penetrance"[Properties])')
EXO = (268, 471)
OMIM_NAMES = {"615083": "CRCS12 (PPAP)", "618336": "IMAGe-I", "615139": "FILS"}
TRUNCATING = {"nonsense", "frameshift variant", "splice donor variant", "splice acceptor variant"}


def get(url: str, data: bytes | None = None) -> str:
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "POLE-Frameshift-verification/1.0"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return fh.read().decode()


def search_ids() -> list[str]:
    url = EUTILS + "esearch.fcgi?db=clinvar&retmax=10000&retmode=json&term=" + urllib.parse.quote(QUERY)
    r = json.loads(get(url))["esearchresult"]
    ids = r["idlist"]
    if int(r["count"]) != len(ids):
        raise SystemExit(f"esearch count {r['count']} but {len(ids)} ids returned; raise retmax or page")
    return ids


def summaries(ids: list[str]) -> list[dict]:
    out = []
    for i in range(0, len(ids), 200):
        batch = ids[i:i + 200]
        body = urllib.parse.urlencode({"db": "clinvar", "retmode": "json", "id": ",".join(batch)}).encode()
        res = json.loads(get(EUTILS + "esummary.fcgi", body))["result"]
        out.extend(res[k] for k in batch if k in res)
        time.sleep(0.4)
    return out


def protein_position(title: str) -> int | None:
    m = re.search(r"\(p\.[A-Za-z]{3}(\d+)", title)
    return int(m.group(1)) if m else None


def row(d: dict) -> dict:
    g = d.get("germline_classification") or {}
    vs = (d.get("variation_set") or [{}])[0]
    loc = next((l for l in vs.get("variation_loc", []) if l.get("assembly_name") == "GRCh38"), {})
    traits = g.get("trait_set") or []
    names = []
    omims = []
    for t in traits:
        names.append(t.get("trait_name", ""))
        omims.extend(x["db_id"] for x in t.get("trait_xrefs", []) if x.get("db_source") == "OMIM")
    cons = d.get("molecular_consequence_list") or []
    return {
        "vcv": f"VCV{int(d['uid']):09d}",
        "title": d.get("title", ""),
        "cdna_change": vs.get("cdna_change", ""),
        "protein_change": d.get("protein_change", ""),
        "variant_type": vs.get("variant_type", ""),
        "molecular_consequence": "; ".join(cons),
        "germline_classification": g.get("description", ""),
        "review_status": g.get("review_status", ""),
        "last_evaluated": g.get("last_evaluated", ""),
        "conditions": " | ".join(names),
        "condition_omim": " | ".join(sorted(set(omims))),
        "grch38_chr12_start": loc.get("start", ""),
        "canonical_spdi": vs.get("canonical_spdi", ""),
    }


def classify(r: dict) -> str:
    cons = set(c.strip() for c in r["molecular_consequence"].split(";") if c.strip())
    if cons & TRUNCATING:
        return "truncating"
    if "missense variant" in cons:
        return "missense"
    return "other/unspecified"


def is_pole_record(r: dict) -> bool:
    """ClinVar's POLE[gene] query also returns records annotated to a neighbouring gene (for example a P2RX2
    missense whose title is NM_170682.4(P2RX2):...). Keep a record unless its title names another gene's transcript."""
    m = re.match(r"N[MR]_\d+\.\d+\((\w+)\):", r["title"])
    return m is None or m.group(1) == "POLE"


def summarise(rows: list[dict]) -> str:
    lines = [f"{len(rows)} ClinVar POLE records with germline classification Pathogenic or Likely pathogenic",
             f"query: {QUERY}", ""]
    by = {}
    for r in rows:
        by.setdefault(classify(r), []).append(r)
    for k in ("truncating", "missense", "other/unspecified"):
        lines.append(f"{k}: {len(by.get(k, []))}")
    lines.append("")
    lines.append("condition (OMIM) by consequence class:")
    for k in ("truncating", "missense", "other/unspecified"):
        counts = {}
        for r in by.get(k, []):
            key = ", ".join(OMIM_NAMES.get(o, o) for o in r["condition_omim"].split(" | ") if o) or "no OMIM id (" + (r["conditions"] or "not provided") + ")"
            counts[key] = counts.get(key, 0) + 1
        for key, n in sorted(counts.items(), key=lambda x: -x[1]):
            lines.append(f"  {k:18s} {n:4d}  {key}")
    exo = [r for r in by.get("missense", []) if (p := protein_position(r["title"])) and EXO[0] <= p <= EXO[1]]
    lines.append("")
    lines.append(f"missense inside the exonuclease domain (residues {EXO[0]}-{EXO[1]}): {len(exo)} of {len(by.get('missense', []))}")
    lines.append("  " + ", ".join(sorted({r['protein_change'] or r['title'].split('(')[-1].rstrip(')') for r in exo})))
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    today = dt.date.today().isoformat()
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "reference", f"POLE_clinvar_PLP_{today}.tsv"))
    a = ap.parse_args()
    ids = search_ids()
    rows = sorted((r for r in (row(d) for d in summaries(ids)) if is_pole_record(r)),
                  key=lambda r: (int(r["grch38_chr12_start"] or 0), r["vcv"]))
    fields = list(rows[0].keys())
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(f"# ClinVar POLE records, germline Pathogenic/Likely pathogenic, retrieved {today} via NCBI E-utilities\n")
        fh.write(f"# query: {QUERY}\n")
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    text = summarise(rows)
    with open(a.out.rsplit(".", 1)[0] + ".summary.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)
    print(f"\nwrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
