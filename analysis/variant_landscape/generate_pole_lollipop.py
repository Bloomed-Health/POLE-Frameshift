#!/usr/bin/env python3
"""
Generate a lollipop plot of the POLE protein variant landscape.

Reads domain boundaries and ClinVar variants from data/ TSV files and produces
a publication-quality figure showing protein domains with variant positions.

Output: SVG and PNG (300 DPI) in the same directory as this script.
"""

import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data")

DOMAIN_FILE = os.path.join(DATA_DIR, "POLE_domain_boundaries.tsv")
VARIANT_FILE = os.path.join(DATA_DIR, "POLE_clinvar_variants.tsv")

# Domain colors
DOMAIN_COLORS = {
    "N-terminal_region": "#B0B0B0",
    "Exonuclease": "#D32F2F",
    "Linker_Exo_Pol": "#B0B0B0",
    "Polymerase": "#1565C0",
    "C-terminal": "#B0B0B0",
}

DOMAIN_LABELS = {
    "N-terminal_region": "N-terminal",
    "Exonuclease": "Exonuclease\n(Proofreading)",
    "Linker_Exo_Pol": "Linker",
    "Polymerase": "Polymerase\n(DNA Synthesis)",
    "C-terminal": "C-terminal\nRegulatory",
}

# Variant marker colors by ClinVar classification
CLASSIFICATION_COLORS = {
    "Pathogenic": "#D32F2F",
    "Likely_pathogenic": "#FF8F00",
    "VUS": "#757575",
    "Not_reported": "#7B1FA2",
}

CLASSIFICATION_LABELS = {
    "Pathogenic": "Pathogenic",
    "Likely_pathogenic": "Likely Pathogenic",
    "VUS": "VUS",
    "Not_reported": "Not in ClinVar",
}


def read_tsv(path):
    with open(path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def get_protein_position(variant):
    """Extract amino acid position from protein notation like p.Pro286Arg."""
    prot = variant["variant_protein"]
    # Parse position from e.g. p.Pro286Arg or p.Leu46Phefs*8
    import re
    match = re.search(r"p\.[A-Z][a-z]{2}(\d+)", prot)
    if match:
        return int(match.group(1))
    return None


def main():
    domains = read_tsv(DOMAIN_FILE)
    variants = read_tsv(VARIANT_FILE)

    fig, ax = plt.subplots(figsize=(14, 5))

    protein_length = 2286
    bar_y = 0
    bar_height = 0.4

    # Draw domain bars
    for d in domains:
        start = int(d["start"])
        end = int(d["end"])
        color = DOMAIN_COLORS.get(d["domain"], "#B0B0B0")
        label = DOMAIN_LABELS.get(d["domain"], d["domain"])

        rect = mpatches.FancyBboxPatch(
            (start, bar_y - bar_height / 2),
            end - start,
            bar_height,
            boxstyle="round,pad=0.02",
            facecolor=color,
            edgecolor="black",
            linewidth=0.8,
            alpha=0.85,
        )
        ax.add_patch(rect)

        # Domain label
        mid = (start + end) / 2
        ax.text(
            mid, bar_y, label,
            ha="center", va="center",
            fontsize=7, fontweight="bold",
            color="white" if color != "#B0B0B0" else "black",
        )

    # Draw lollipop markers for variants
    for v in variants:
        pos = get_protein_position(v)
        if pos is None:
            continue

        classification = v["clinvar_classification"]
        color = CLASSIFICATION_COLORS.get(classification, "#757575")
        is_this_variant = v["variant_cdna"] == "c.138del"

        # Lollipop stick
        stick_top = bar_y + bar_height / 2 + 0.6
        ax.plot(
            [pos, pos],
            [bar_y + bar_height / 2, stick_top],
            color=color, linewidth=1.5, zorder=3,
        )

        # Marker
        if is_this_variant:
            ax.plot(
                pos, stick_top,
                marker="*", markersize=18, color="#7B1FA2",
                markeredgecolor="black", markeredgewidth=0.8, zorder=5,
            )
            ax.annotate(
                f"c.138del\np.Leu46Phefs*8\n(This variant)",
                xy=(pos, stick_top),
                xytext=(pos + 180, stick_top + 0.35),
                fontsize=7.5, fontweight="bold", color="#7B1FA2",
                ha="left", va="bottom",
                arrowprops=dict(
                    arrowstyle="-|>", color="#7B1FA2",
                    connectionstyle="arc3,rad=-0.2",
                    lw=1.2,
                ),
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#F3E5F5",
                          edgecolor="#7B1FA2", alpha=0.9),
                zorder=6,
            )
        else:
            ax.plot(
                pos, stick_top,
                marker="o", markersize=9, color=color,
                markeredgecolor="black", markeredgewidth=0.8, zorder=4,
            )
            # Label
            label = v["variant_protein"].replace("p.", "")
            ax.text(
                pos, stick_top + 0.12, label,
                ha="center", va="bottom", fontsize=6.5, rotation=45,
            )

    # Truncation indicator: dashed line at residue 54
    ax.axvline(
        x=54, color="#7B1FA2", linestyle="--", linewidth=1, alpha=0.6, zorder=1,
    )
    ax.text(
        54, bar_y - bar_height / 2 - 0.15, "STOP\n(res 54)",
        ha="center", va="top", fontsize=6.5, color="#7B1FA2", fontstyle="italic",
    )

    # Axis formatting
    ax.set_xlim(-30, protein_length + 50)
    ax.set_ylim(-0.8, 1.8)
    ax.set_xlabel("Amino Acid Position", fontsize=11)
    ax.set_title(
        "POLE Variant Landscape — Domain Architecture & ClinVar Variants",
        fontsize=13, fontweight="bold", pad=15,
    )

    # Position ticks
    tick_positions = [1, 268, 471, 530, 1189, 2286]
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([str(t) for t in tick_positions], fontsize=8)

    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor="#D32F2F", edgecolor="black", label="Exonuclease Domain"),
        mpatches.Patch(facecolor="#1565C0", edgecolor="black", label="Polymerase Domain"),
        mpatches.Patch(facecolor="#B0B0B0", edgecolor="black", label="Other Regions"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#D32F2F",
                   markeredgecolor="black", markersize=8, label="Pathogenic"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#FF8F00",
                   markeredgecolor="black", markersize=8, label="Likely Pathogenic"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#757575",
                   markeredgecolor="black", markersize=8, label="VUS"),
        plt.Line2D([0], [0], marker="*", color="w", markerfacecolor="#7B1FA2",
                   markeredgecolor="black", markersize=12, label="c.138del (This Variant)"),
    ]
    ax.legend(
        handles=legend_elements, loc="upper right", fontsize=7.5,
        framealpha=0.9, ncol=2,
    )

    plt.tight_layout()

    # Save outputs
    svg_path = os.path.join(SCRIPT_DIR, "POLE_variant_landscape.svg")
    png_path = os.path.join(SCRIPT_DIR, "POLE_variant_landscape.png")

    fig.savefig(svg_path, format="svg", bbox_inches="tight")
    fig.savefig(png_path, format="png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"SVG saved: {svg_path}")
    print(f"PNG saved: {png_path}")


if __name__ == "__main__":
    main()
