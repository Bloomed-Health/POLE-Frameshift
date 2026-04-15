#!/usr/bin/env python3
"""
Generate temporal phenotype analysis visualizations for POLE c.138del.

Produces two figures:
1. Tissue Replication Rate vs. POLE Vulnerability — bubble chart showing the
   relationship between tissue turnover rate and observed clinical findings,
   testing Model 4 (haploinsufficiency) predictions.
2. Phenotype Timeline — horizontal bar chart showing age-at-onset categories
   for each clinical finding, colored by phenotype category.

Reads from data/tissue_replication_rates.tsv and data/phenotype_timeline.tsv.

Output: SVG and PNG (300 DPI) in the same directory as this script.
"""

import csv
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data")

REPLICATION_FILE = os.path.join(DATA_DIR, "tissue_replication_rates.tsv")
TIMELINE_FILE = os.path.join(DATA_DIR, "phenotype_timeline.tsv")

# Category colors
CATEGORY_COLORS = {
    "Neoplastic": "#D32F2F",
    "Proliferative/Stromal": "#FF8F00",
    "Endometrial/Hormonal": "#7B1FA2",
    "Congenital Developmental": "#1565C0",
    "Autoimmune/Immune": "#2E7D32",
    "Comorbidity": "#78909C",
}

# Model 4 support colors
SUPPORT_COLORS = {
    "Strong": "#D32F2F",
    "Strong (developmental)": "#1565C0",
    "Moderate": "#FF8F00",
    "Weak-Moderate": "#FBC02D",
    "Weak": "#B0B0B0",
    "Conditional": "#9C27B0",
    "Pending": "#78909C",
}

# Severity to bubble size
SEVERITY_SIZES = {
    "Severe": 400,
    "Moderate-Severe": 320,
    "Moderate": 240,
    "Mild": 160,
    "Congenital + Mild": 200,
    "Unknown": 120,
}


def read_tsv(path):
    with open(path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def turnover_to_numeric(turnover_days_str):
    """Convert turnover_days string to a numeric value for plotting."""
    mapping = {
        "3-5": 4,
        "2-8": 5,
        "~28 (monthly)": 28,
        "~40 (HSC cycling)": 40,
        "Variable (~hormonal)": 60,
        "200-300": 250,
        "~365": 365,
        "Variable": 180,
        "~2920 (~8 years)": 2920,
    }
    return mapping.get(turnover_days_str, 100)


def generate_replication_bubble_chart(data):
    """Generate tissue replication rate vs. POLE vulnerability bubble chart."""
    fig, ax = plt.subplots(figsize=(14, 8))

    tissues = []
    x_vals = []
    y_labels = []
    sizes = []
    colors = []
    edge_colors = []

    for i, row in enumerate(data):
        numeric_days = turnover_to_numeric(row["turnover_days"])
        tissues.append(row["tissue"])
        x_vals.append(numeric_days)
        y_labels.append(row["tissue"])
        sizes.append(SEVERITY_SIZES.get(row["finding_severity"], 150))
        colors.append(SUPPORT_COLORS.get(row["model4_support"], "#B0B0B0"))
        edge_colors.append("black")

    y_positions = list(range(len(tissues)))

    # Plot bubbles
    for i in range(len(tissues)):
        ax.scatter(
            x_vals[i], y_positions[i],
            s=sizes[i], c=colors[i], edgecolors=edge_colors[i],
            linewidth=0.8, alpha=0.85, zorder=3,
        )

    # Add finding annotations
    for i, row in enumerate(data):
        finding_short = row["patient_finding"]
        if len(finding_short) > 55:
            finding_short = finding_short[:52] + "..."
        ax.annotate(
            finding_short,
            xy=(x_vals[i], y_positions[i]),
            xytext=(15, 0),
            textcoords="offset points",
            fontsize=6.5, va="center", ha="left",
            color="#333333",
        )

    # Axis formatting
    ax.set_xscale("log")
    ax.set_xlabel("Cell Turnover Period (days, log scale)", fontsize=11, fontweight="bold")
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=9)
    ax.set_title(
        "Tissue Replication Rate vs. POLE c.138del Clinical Findings\n"
        "Testing Model 4: Haploinsufficiency Predicts High-Turnover Tissue Vulnerability",
        fontsize=12, fontweight="bold", pad=15,
    )

    # Add prediction zone
    ax.axvspan(1, 30, alpha=0.08, color="#D32F2F", zorder=0)
    ax.axvspan(30, 100, alpha=0.05, color="#FF8F00", zorder=0)
    ax.axvspan(100, 5000, alpha=0.03, color="#B0B0B0", zorder=0)

    ax.text(5, len(tissues) - 0.3, "HIGH VULNERABILITY\n(rapid turnover)",
            fontsize=7, color="#D32F2F", alpha=0.7, ha="center", fontstyle="italic")
    ax.text(55, len(tissues) - 0.3, "MODERATE",
            fontsize=7, color="#FF8F00", alpha=0.7, ha="center", fontstyle="italic")
    ax.text(700, len(tissues) - 0.3, "LOW\n(slow turnover)",
            fontsize=7, color="#757575", alpha=0.7, ha="center", fontstyle="italic")

    # Legend
    support_legend = [
        mpatches.Patch(facecolor=SUPPORT_COLORS["Strong"], edgecolor="black",
                       label="Strong Model 4 support"),
        mpatches.Patch(facecolor=SUPPORT_COLORS["Strong (developmental)"], edgecolor="black",
                       label="Strong (developmental)"),
        mpatches.Patch(facecolor=SUPPORT_COLORS["Moderate"], edgecolor="black",
                       label="Moderate support"),
        mpatches.Patch(facecolor=SUPPORT_COLORS["Conditional"], edgecolor="black",
                       label="Conditional (needs LOH data)"),
        mpatches.Patch(facecolor=SUPPORT_COLORS["Pending"], edgecolor="black",
                       label="Pending (testing needed)"),
    ]
    size_legend = [
        plt.scatter([], [], s=400, c="gray", edgecolors="black", alpha=0.5, label="Severe"),
        plt.scatter([], [], s=240, c="gray", edgecolors="black", alpha=0.5, label="Moderate"),
        plt.scatter([], [], s=120, c="gray", edgecolors="black", alpha=0.5, label="Unknown"),
    ]

    leg1 = ax.legend(handles=support_legend, loc="lower right", fontsize=7.5,
                     title="Model 4 Support", title_fontsize=8, framealpha=0.9)
    ax.add_artist(leg1)
    ax.legend(handles=size_legend, loc="lower left", fontsize=7.5,
              title="Finding Severity", title_fontsize=8, framealpha=0.9)

    ax.set_xlim(1.5, 5000)
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    return fig


def generate_phenotype_timeline(data):
    """Generate phenotype timeline showing onset categories by phenotype category."""
    fig, ax = plt.subplots(figsize=(14, 7))

    # Map onset types to numeric x positions
    onset_order = {
        "Congenital": 0,
        "Childhood": 1,
        "Adolescent": 2,
        "Adult": 3,
        "Unknown": 3.5,
    }
    onset_labels = ["Congenital\n(in utero)", "Childhood", "Adolescence", "Adulthood", "Unknown\nonset"]

    findings = []
    x_vals = []
    colors = []
    categories = []

    for row in data:
        onset = row["onset_type"]
        if onset == "adult_incidental":
            onset = "Unknown"  # discovered incidentally, true onset unknown
        findings.append(row["finding"])
        x_vals.append(onset_order.get(onset, 3.5))
        cat = row["phenotype_category"]
        colors.append(CATEGORY_COLORS.get(cat, "#78909C"))
        categories.append(cat)

    y_positions = list(range(len(findings)))

    # Draw connecting lines from congenital to each finding (developmental trajectory)
    for i in range(len(findings)):
        ax.plot(
            [0, x_vals[i]], [y_positions[i], y_positions[i]],
            color=colors[i], linewidth=1, alpha=0.3, zorder=1,
        )

    # Plot markers
    for i in range(len(findings)):
        marker = "D" if categories[i] == "Congenital Developmental" else "o"
        ax.scatter(
            x_vals[i], y_positions[i],
            s=200, c=colors[i], edgecolors="black", linewidth=0.8,
            marker=marker, alpha=0.85, zorder=3,
        )

    # Label tissues with replication rate info
    for i, row in enumerate(data):
        rate = row.get("tissue_turnover_rate", "")
        label = f"{row['finding']}"
        if rate and rate != "N/A (neural)" and rate != "N/A (immune)":
            label += f"  [{rate}]"
        ax.text(
            max(x_vals) + 0.3, y_positions[i], label,
            fontsize=7, va="center", ha="left", color="#333333",
        )

    # Axis formatting
    ax.set_xticks(list(onset_order.values()))
    ax.set_xticklabels(onset_labels, fontsize=10, fontweight="bold")
    ax.set_yticks([])
    ax.set_xlim(-0.5, max(x_vals) + 5.5)
    ax.set_title(
        "POLE c.138del — Temporal Phenotype Map\n"
        "Age-at-Onset by Phenotype Category with Tissue Turnover Rates",
        fontsize=12, fontweight="bold", pad=15,
    )

    # Model 4 prediction annotation
    ax.annotate(
        "Model 4 prediction: high-turnover tissues\n"
        "affected first / most severely",
        xy=(0.02, 0.02), xycoords="axes fraction",
        fontsize=8, fontstyle="italic", color="#555555",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5",
                  edgecolor="#CCCCCC", alpha=0.9),
    )

    # Add vertical lines for life stages
    for x_pos in onset_order.values():
        ax.axvline(x=x_pos, color="#E0E0E0", linewidth=0.8, linestyle="--", zorder=0)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=CATEGORY_COLORS["Neoplastic"], edgecolor="black",
                       label="Neoplastic"),
        mpatches.Patch(facecolor=CATEGORY_COLORS["Proliferative/Stromal"], edgecolor="black",
                       label="Proliferative/Stromal"),
        mpatches.Patch(facecolor=CATEGORY_COLORS["Endometrial/Hormonal"], edgecolor="black",
                       label="Endometrial/Hormonal"),
        mpatches.Patch(facecolor=CATEGORY_COLORS["Congenital Developmental"], edgecolor="black",
                       label="Congenital Developmental"),
        mpatches.Patch(facecolor=CATEGORY_COLORS["Autoimmune/Immune"], edgecolor="black",
                       label="Autoimmune/Immune"),
        mpatches.Patch(facecolor=CATEGORY_COLORS["Comorbidity"], edgecolor="black",
                       label="Comorbidity (hEDS/POTS)"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", fontsize=7.5, framealpha=0.9)

    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()
    return fig


def main():
    replication_data = read_tsv(REPLICATION_FILE)
    timeline_data = read_tsv(TIMELINE_FILE)

    # Figure 1: Tissue replication bubble chart
    fig1 = generate_replication_bubble_chart(replication_data)
    for ext, fmt, dpi in [("svg", "svg", None), ("png", "png", 300)]:
        path = os.path.join(SCRIPT_DIR, f"tissue_replication_vulnerability.{ext}")
        kwargs = {"format": fmt, "bbox_inches": "tight"}
        if dpi:
            kwargs["dpi"] = dpi
        fig1.savefig(path, **kwargs)
        print(f"Saved: {path}")
    plt.close(fig1)

    # Figure 2: Phenotype timeline
    fig2 = generate_phenotype_timeline(timeline_data)
    for ext, fmt, dpi in [("svg", "svg", None), ("png", "png", 300)]:
        path = os.path.join(SCRIPT_DIR, f"phenotype_timeline.{ext}")
        kwargs = {"format": fmt, "bbox_inches": "tight"}
        if dpi:
            kwargs["dpi"] = dpi
        fig2.savefig(path, **kwargs)
        print(f"Saved: {path}")
    plt.close(fig2)


if __name__ == "__main__":
    main()
