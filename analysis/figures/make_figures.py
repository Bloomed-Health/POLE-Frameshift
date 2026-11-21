#!/usr/bin/env python3
"""Build the README figures from the verified fixtures, the claims ledger and the phenotype table.

    python3 analysis/figures/make_figures.py          # writes PNG and SVG files to figures/

Needs matplotlib. Every number drawn comes from analysis/variant_verification (sequence facts),
data/claims_ledger.tsv, data/phenotype_timeline.tsv, or the two case-control counts quoted from
Mur et al. 2020 (ledger row E01). Nothing is positioned by hand except labels.

Colours: three categorical hues that pass an all-pairs colour-vision check on this surface
(blue, orange, aqua), one reserved "stop" red that always carries a text label, and greys.
"""
from __future__ import annotations

import csv
import math
import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "analysis", "variant_verification"))
import nterm_truncations as nt  # noqa: E402
import verify_c138del as v  # noqa: E402

OUT = os.environ.get("POLE_FIGURES_OUT") or os.path.join(ROOT, "figures")   # tests regenerate into a temporary directory
SURFACE, INK, INK2, MUTED, GRID, NEUTRAL = "#fcfcfb", "#0b0b0b", "#52514e", "#8b8a84", "#e4e3df", "#f0efec"
BLUE, ORANGE, AQUA, STOP, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#d03b3b", "#b9b8b2"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": INK, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.edgecolor": GRID, "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE, "svg.fonttype": "none", "axes.titlesize": 12,
})


def finish(fig, name: str) -> None:
    os.makedirs(OUT, exist_ok=True)
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=200, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("wrote", f"figures/{name}.png and .svg")


def bare(ax) -> None:
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])


def titled(fig, title: str, subtitle: str) -> None:
    fig.text(0.01, 0.985, title, ha="left", va="top", fontsize=13, fontweight="bold", color=INK)
    fig.text(0.01, 0.925, subtitle, ha="left", va="top", fontsize=9.5, color=INK2)


# ------------------------------------------------------------------------------------------- 1. codons
def fig_codons(rep: dict) -> None:
    wt = rep["codons_44_54_wt"][:10]
    mut = rep["codons_44_53_mut"]
    first = rep["c138del"]["codon_number"]
    fig, ax = plt.subplots(figsize=(10, 3.9))
    bare(ax)
    ax.set_xlim(-1.75, 10.1)
    ax.set_ylim(-1.15, 3.2)
    for row, (label, cells) in enumerate((("Wild type", wt), ("c.138del", mut))):
        y = 1.55 - row * 1.35
        ax.text(-1.7, y + 0.42, label, ha="left", va="center", fontsize=11, fontweight="bold")
        for i, c in enumerate(cells):
            aa = v.CODON[c["nt"]]
            changed = row == 1 and c["codon"] >= first
            stop = aa == "*"
            face = "#fde3d8" if changed and not stop else ("#f9dcdc" if stop else NEUTRAL)
            edge = ORANGE if changed and not stop else (STOP if stop else GREY)
            ax.add_patch(FancyBboxPatch((i + 0.04, y), 0.92, 0.84, boxstyle="round,pad=0,rounding_size=0.08",
                                        facecolor=face, edgecolor=edge, linewidth=1.4))
            ax.text(i + 0.5, y + 0.57, c["nt"], ha="center", va="center", family="DejaVu Sans Mono", fontsize=12)
            ax.text(i + 0.5, y + 0.22, "stop" if stop else v.AA3[aa], ha="center", va="center", fontsize=10,
                    color=INK, fontweight="bold" if (changed or stop) else "normal")
            if row == 0:
                ax.text(i + 0.5, y + 1.02, str(c["codon"]), ha="center", va="bottom", fontsize=9, color=INK2)
    ax.text(-1.7, 2.73, "codon", ha="left", va="bottom", fontsize=9, color=INK2)
    # the deleted base: third letter of codon 46 in the wild-type row
    x46 = (first - 44) + 0.5
    ax.plot([x46 + 0.1, x46 + 0.25], [1.55 + 0.42, 1.55 + 0.42], color=STOP, lw=2, solid_capstyle="round")
    ax.plot([x46 + 0.175, x46 + 0.175], [1.5, 1.36], color=INK2, lw=1)
    ax.text(x46 + 0.26, 1.29, "c.138: this G is deleted", fontsize=9.5, color=INK, ha="left", va="center")
    c = rep["c138del"]
    ax.text(-1.7, -0.45, f"{c['hgvs_p']}   ·   stop at codon {c['stop_codon_number']} ({c['stop_codon']})   ·   "
            f"predicted product {c['truncated_length_aa']} residues: {c['native_residues']} native + {c['novel_residues']}",
            ha="left", va="center", fontsize=10.5)
    ax.add_patch(Rectangle((-1.7, -0.98), 0.26, 0.2, facecolor="#fde3d8", edgecolor=ORANGE, lw=1.2))
    ax.text(-1.36, -0.88, "residue changed by the frameshift", ha="left", va="center", fontsize=9, color=INK2)
    ax.add_patch(Rectangle((2.25, -0.98), 0.26, 0.2, facecolor="#f9dcdc", edgecolor=STOP, lw=1.2))
    ax.text(2.59, -0.88, "new stop codon", ha="left", va="center", fontsize=9, color=INK2)
    titled(fig, "POLE c.138del at codon resolution",
           "Re-derived from the MANE Select coding sequence (ENST00000320574.10 / NM_006231.4); matches Ensembl VEP")
    finish(fig, "c138del_codons")


# ------------------------------------------------------------------------------------------- 2. translation map
def fig_translation_map(rep: dict) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True, gridspec_kw={"hspace": 0.16})
    xmax = 240
    lanes = [1, 47, 65, 68, 130, 196]
    names = {1: "c.1  annotated start", 47: "c.47", 65: "c.65", 68: "c.68", 130: "c.130  Met44", 196: "c.196  Met66"}
    for ax, key, label in ((axes[0], "orf_map_wild_type", "Wild-type mRNA"), (axes[1], "orf_map_c138del", "c.138del mRNA")):
        orfs = {o["atg_c"]: o for o in rep[key]}
        mutant = key.endswith("c138del")
        ax.axvspan(1, 150, color=NEUTRAL, lw=0, zorder=0)
        ax.axvline(62.5, color=GREY, lw=1, ls=(0, (3, 3)), zorder=1)
        if mutant:
            ax.axvline(138, color=INK, lw=1.2, zorder=1)
        for row, c in enumerate(lanes):
            y = len(lanes) - 1 - row
            o = orfs[c]
            end = xmax + 6 if o["stop_c"] is None else o["stop_c"][0] - 0.5
            in_pole_frame = (c - 1) % 3 == 0
            segs = []
            if mutant and c < 138:
                segs.append((c, 138, BLUE if in_pole_frame else ORANGE))
                segs.append((138, end, ORANGE))                 # every frame is shifted after the deletion
            else:
                segs.append((c, end, BLUE if in_pole_frame else ORANGE))
            if mutant and c == 196:
                segs = [(c, end, AQUA)]
            for a, b, col in segs:
                ax.plot([a, b], [y, y], color=col, lw=7, solid_capstyle="butt", zorder=3)
            ax.plot([c], [y], marker="o", ms=8.5, color=INK, mec=SURFACE, mew=1.6, zorder=5)
            if o["stop_c"] is not None:
                ax.plot([o["stop_c"][0] + 1], [y], marker="s", ms=8, color=STOP, mec=SURFACE, mew=1.4, zorder=5)
                ax.text(o["stop_c"][1] + 4, y, f"stop c.{o['stop_c'][0]}–{o['stop_c'][1]}  ({o['codons']} codons)",
                        va="center", ha="left", fontsize=8.8, color=INK2, zorder=6)
            else:
                ax.annotate("", xy=(xmax + 9, y), xytext=(xmax + 3, y), arrowprops=dict(arrowstyle="-|>", color=segs[-1][2], lw=2))
            ax.text(-4, y, f"{names[c]}   {o['strength']}", va="center", ha="right", fontsize=9, color=INK)
        ax.set_ylim(-0.95, len(lanes) - 0.25)
        ax.set_yticks([])
        for s in ("left", "right", "top"):
            ax.spines[s].set_visible(False)
        ax.set_title(label, loc="left", fontsize=11, fontweight="bold", pad=6)
    axes[0].text(4, 5.62, "first 150 nt: stops here tend to escape decay", fontsize=8.5, color=INK2, va="center")
    axes[0].text(63.5, -0.68, "exon 1 | exon 2", fontsize=8.5, color=INK2, va="center")
    axes[1].text(139.5, 5.62, "deletion", fontsize=8.8, color=INK, va="center")
    gap = rep["first_atg_after_ptc"]["nt_between_stop_and_atg"]
    axes[1].annotate("", xy=(193.5, 0), xytext=(161, 0), arrowprops=dict(arrowstyle="<->", color=INK2, lw=1))
    axes[1].text(177, 0.2, f"{gap} nt", ha="center", va="bottom", fontsize=8.8, color=INK2)
    axes[1].text(xmax + 8, -0.52, "product would lack residues 1–65", ha="right", va="center", fontsize=8.8, color=INK2)
    axes[1].set_xlim(-62, xmax + 10)
    axes[1].set_xticks([1, 50, 100, 150, 200, 240])
    axes[1].set_xlabel("position in the coding sequence (nt)")
    handles = [plt.Line2D([], [], color=BLUE, lw=7, label="POLE reading frame"),
               plt.Line2D([], [], color=ORANGE, lw=7, label="shifted frame"),
               plt.Line2D([], [], color=AQUA, lw=7, label="POLE frame after a restart (untested)"),
               plt.Line2D([], [], color=INK, marker="o", ms=8, lw=0, label="start codon (AUG)"),
               plt.Line2D([], [], color=STOP, marker="s", ms=8, lw=0, label="stop codon")]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.01, -0.075), ncol=5, frameon=False, fontsize=8.8,
               handlelength=1.6, columnspacing=1.4)
    fig.subplots_adjust(top=0.84)
    titled(fig, "Upstream of c.138del every reading frame ends by c.160; the next start is Met66",
           "Start codons and the reading frames they open in the first 240 nt. Strength = Kozak context. Sequence facts only: no experiment shows a restart.")
    finish(fig, "c138del_translation_map")


# ------------------------------------------------------------------------------------------- 3. neighbours
def fig_neighbours() -> None:
    rows = [r for r in nt.rows() if r["kind"] in ("nonsense", "frameshift", "start_lost")]
    groups = [("start codon lost", lambda r: r["kind"] == "start_lost"),
              ("stops before Met44", lambda r: r.get("next_met") == 44),
              ("stops before Met66", lambda r: r.get("next_met") == 66),
              ("stops after Met66", lambda r: r.get("next_met") == 221)]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.axvline(62.5, color=GREY, lw=1, ls=(0, (3, 3)), zorder=1)
    for c, name in ((1, "Met1"), (130, "Met44"), (196, "Met66")):
        ax.axvline(c, color=GRID, lw=1.2, zorder=0)
        ax.text(c, 3.62, name, ha="center", va="bottom", fontsize=9, color=INK2)
    focus = {"c.137del", "c.137dup", "c.138del", "c.141del"}
    for gi, (gname, test) in enumerate(groups):
        y = len(groups) - 1 - gi
        members = [r for r in rows if test(r)]
        seen = {}
        for r in sorted(members, key=lambda r: int(re.search(r"\d+", r["hgvs_c"]).group())):
            x = int(re.search(r"\d+", r["hgvs_c"]).group())
            k = seen.get(x, 0)
            seen[x] = k + 1
            hot = r["hgvs_c"] in focus
            ax.plot([x], [y + 0.14 * k], marker="o", ms=9.5 if hot else 8.5, color=BLUE if hot else GREY,
                    mec=SURFACE, mew=1.6, zorder=4 if hot else 3)
        ax.text(-8, y + 0.05, f"{gname}  ({len(members)})", ha="right", va="center", fontsize=9.5, color=INK)
    ax.annotate("c.137del, c.137dup, c.138del, c.141del\nsame codons, near-identical product", xy=(138.5, 0.92),
                xytext=(118, 0.42), fontsize=9, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=INK2, lw=1, shrinkB=6))
    ax.text(63.5, -0.62, "exon 1 | exon 2", fontsize=8.5, color=INK2, va="center")
    ax.set_xlim(-62, 208)
    ax.set_ylim(-0.8, 3.95)
    ax.set_yticks([])
    ax.set_xticks([1, 50, 100, 150, 204])
    ax.set_xlabel("position of the variant in the coding sequence (nt)")
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    handles = [plt.Line2D([], [], color=BLUE, marker="o", ms=9, lw=0, label="c.138del and its three nearest neighbours"),
               plt.Line2D([], [], color=GREY, marker="o", ms=9, lw=0, label="other alleles recorded in dbSNP / ClinVar")]
    fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.01, -0.07), ncol=2, frameon=False, fontsize=9)
    fig.subplots_adjust(top=0.8)
    n_tr = sum(r["kind"] != "start_lost" for r in rows)
    titled(fig, f"c.138del is one of {n_tr} truncating and {len(rows) - n_tr} start-loss alleles recorded in POLE exons 1–2",
           "Grouped by the next in-frame start codon after the premature stop. Each dot is one allele, re-derived on MANE Select.")
    finish(fig, "pole_exon1-2_truncations")


# ------------------------------------------------------------------------------------------- 4. evidence on LoF
def fig_lof_evidence() -> None:
    a, n1, c, n0 = 5, 2309, 119, 59095          # Mur et al. 2020 (ledger row E01)
    b, d = n1 - a, n0 - c
    odds = (a * d) / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    lo, hi = math.exp(math.log(odds) - 1.96 * se), math.exp(math.log(odds) + 1.96 * se)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.9), gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.32})
    ax1.axvline(1, color=GREY, lw=1.2, zorder=1)
    ax1.plot([lo, hi], [0, 0], color=BLUE, lw=2, solid_capstyle="round", zorder=3)
    ax1.plot([odds], [0], marker="o", ms=10, color=BLUE, mec=SURFACE, mew=2, zorder=4)
    ax1.text(1.16, 0.16, f"odds ratio {odds:.2f}", ha="left", va="bottom", fontsize=10, color=INK)
    ax1.text(1.16, -0.16, f"95% interval {lo:.2f} to {hi:.2f}", ha="left", va="top", fontsize=9, color=INK2)
    ax1.text(1.03, 0.82, "no effect", ha="left", va="center", fontsize=8.8, color=INK2)
    ax1.set_xscale("log")
    ax1.set_xlim(0.25, 4)
    ax1.set_ylim(-1, 1)
    ax1.set_xticks([0.25, 0.5, 1, 2, 4])
    ax1.set_xticklabels(["0.25", "0.5", "1", "2", "4"])
    ax1.minorticks_off()
    ax1.set_yticks([])
    ax1.set_xlabel("odds ratio, patients versus controls (log scale)")
    ax1.set_title(f"Loss-of-function POLE/POLD1 variants:\n{a}/{n1:,} hereditary cancer patients, {c}/{n0:,} controls",
                  loc="left", fontsize=10, color=INK, pad=8)
    f, n = 0.001, 541
    rr = [1 + i * 0.25 for i in range(0, 397)]
    ax2.plot(rr, [n * r * f / (r * f + 1 - f) for r in rr], color=BLUE, lw=2, zorder=3)
    for r in (1, 2, 5, 10, 50):
        val = n * r * f / (r * f + 1 - f)
        ax2.plot([r], [val], marker="o", ms=8.5, color=BLUE, mec=SURFACE, mew=1.8, zorder=4)
        ax2.text(r * 1.12, val * 0.86, f"{val:.1f}" if val < 10 else f"{val:.0f}", ha="left", va="top", fontsize=9.5, color=INK)
    ax2.axhline(1, color=GREY, lw=1.2, ls=(0, (3, 3)), zorder=1)
    ax2.text(95, 1.12, "one carrier", ha="right", va="bottom", fontsize=8.8, color=INK2)
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlim(0.9, 100)
    ax2.set_ylim(0.3, 70)
    ax2.set_xticks([1, 2, 5, 10, 50, 100])
    ax2.set_xticklabels(["1", "2", "5", "10", "50", "100"])
    ax2.set_yticks([0.5, 1, 2, 5, 10, 20, 50])
    ax2.set_yticklabels(["0.5", "1", "2", "5", "10", "20", "50"])
    ax2.minorticks_off()
    ax2.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    ax2.set_xlabel("true relative risk of polyposis in carriers (log scale)")
    ax2.set_title(f"Carriers expected by chance in a series of {n}\nunexplained polyposis patients", loc="left", fontsize=10, color=INK, pad=8)
    for ax in (ax1, ax2):
        for s in ("left", "right", "top"):
            ax.spines[s].set_visible(False)
    fig.subplots_adjust(top=0.68)
    titled(fig, "One carrier with polyps is what chance predicts",
           "Left: Mur et al. 2020 (interval computed here). Right: assumes 1 carrier per 1,000 people; 541 is the size of Terlouw et al. 2026.")
    finish(fig, "lof_evidence")


# ------------------------------------------------------------------------------------------- 5. ledger status
def fig_ledger() -> None:
    with open(os.path.join(ROOT, "data", "claims_ledger.tsv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    names = {"VERIFIED": "Verified against a primary source", "CONTRADICTED": "Repository claim contradicted",
             "UNVERIFIED": "Not verified", "OWNER_STATEMENT": "Owner statement, document not seen",
             "INFERENCE": "Inference, untested", "NOT_FOUND": "Searched for, not found", "NOT_MEASURED": "Never measured in the patient"}
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    order = sorted(counts, key=lambda k: counts[k])
    fig, ax = plt.subplots(figsize=(10, 3.6))
    for i, k in enumerate(order):
        ax.barh(i, counts[k], height=0.52, color=BLUE, zorder=3)
        ax.text(counts[k] + 0.5, i, str(counts[k]), va="center", ha="left", fontsize=10, color=INK)
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels([names[k] for k in order], fontsize=9.5, color=INK)
    ax.set_xlim(0, max(counts.values()) * 1.12)
    ax.set_xticks([])
    ax.tick_params(axis="y", length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.subplots_adjust(top=0.78, left=0.34)
    titled(fig, f"Status of the {len(rows)} claims in the ledger",
           "data/claims_ledger.tsv, audit of 20 November 2026. Each claim has a source and a date.")
    finish(fig, "claims_ledger_status")


# ------------------------------------------------------------------------------------------- 6. clinical timeline
def fig_timeline() -> None:
    with open(os.path.join(ROOT, "data", "phenotype_timeline.tsv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    dated, undated = [], []
    for r in rows:
        m = re.fullmatch(r"~?(\d+(?:\.\d+)?)", r["age_at_diagnosis"].strip())
        (dated if m else undated).append((float(m.group(1)) if m else None, r))
    dated.sort(key=lambda t: t[0])
    fig, ax = plt.subplots(figsize=(10, 0.46 * len(dated) + 2.3))
    for i, (age, r) in enumerate(dated):
        y = len(dated) - 1 - i
        neo = bool(re.search(r"polyp|carcinoma|adenoma|tumou?r", r["finding"], re.I))
        ax.plot([age], [y], marker="o", ms=9, color=BLUE if neo else GREY, mec=SURFACE, mew=1.6, zorder=3)
        name = re.sub(r"\s*\(s/p total thyroidectomy\)", "", r["finding"]).replace("(first adenomas)", "(first polyps)")
        ax.text(age + 0.7, y, f"{name}  ·  age {age:g}", va="center", ha="left", fontsize=9.3, color=INK)
    ax.set_xlim(17, 46)
    ax.set_ylim(-0.8, len(dated) - 0.3)
    ax.set_yticks([])
    ax.set_xticks([20, 25, 30])
    ax.set_xlabel("age at diagnosis (years)")
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)
    names = "; ".join(r["finding"].split(" (")[0] for _, r in undated)
    fig.text(0.01, -0.02, "Age at diagnosis not recorded: " + names, ha="left", va="top", fontsize=8.6, color=INK2, wrap=True)
    handles = [plt.Line2D([], [], color=BLUE, marker="o", ms=9, lw=0, label="polyps and tumours"),
               plt.Line2D([], [], color=GREY, marker="o", ms=9, lw=0, label="other findings")]
    ax.legend(handles=handles, loc="upper right", frameon=False, fontsize=9)
    fig.subplots_adjust(top=0.8)
    titled(fig, "Clinical timeline of the one described carrier",
           "From data/phenotype_timeline.tsv. Descriptive only: polyp histology is undocumented and no lesion has been sequenced.")
    finish(fig, "clinical_timeline")


def main() -> int:
    rep = v.build_report()
    fig_codons(rep)
    fig_translation_map(rep)
    fig_neighbours()
    fig_lof_evidence()
    fig_ledger()
    fig_timeline()
    return 0


if __name__ == "__main__":
    sys.exit(main())
