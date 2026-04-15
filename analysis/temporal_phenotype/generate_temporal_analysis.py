#!/usr/bin/env python3
"""
Generate temporal phenotype analysis visualizations for POLE c.138del.

Produces three figures:
1. Tissue Replication Rate vs. POLE Vulnerability — bubble chart showing the
   relationship between tissue turnover rate and observed clinical findings,
   testing Model 4 (haploinsufficiency) predictions.
2. Phenotype Timeline — findings plotted against actual age-at-diagnosis on a
   numeric timeline, colored by phenotype category.
3. Turnover Rate vs. Age-at-Diagnosis — scatter plot directly testing the
   Model 4 prediction that faster-dividing tissues are diagnosed earlier.

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


def parse_age(age_str):
    """Parse age string to numeric value. Returns None if unparseable."""
    if not age_str or age_str in ("unknown", "variable", "adult", "adult_incidental"):
        return None
    age_str = age_str.strip().lstrip("~")
    try:
        return float(age_str)
    except ValueError:
        pass
    if age_str == "childhood":
        return 5  # approximate
    if age_str == "adolescence":
        return 14  # approximate
    return None


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
    """Generate phenotype timeline with actual ages on x-axis."""
    fig, ax = plt.subplots(figsize=(16, 8))

    findings = []
    x_vals = []
    colors = []
    categories = []
    has_age = []

    for row in data:
        # Use age_at_diagnosis as primary x value, fall back to age_at_onset
        age_dx = parse_age(row.get("age_at_diagnosis", ""))
        age_onset = parse_age(row.get("age_at_onset", ""))
        age = age_dx if age_dx is not None else age_onset

        findings.append(row["finding"])
        categories.append(row["phenotype_category"])
        colors.append(CATEGORY_COLORS.get(row["phenotype_category"], "#78909C"))

        if age is not None:
            x_vals.append(age)
            has_age.append(True)
        else:
            x_vals.append(33)  # place unknowns at right edge
            has_age.append(False)

    y_positions = list(range(len(findings)))

    # Draw onset-to-diagnosis ranges where both are known
    for i, row in enumerate(data):
        age_onset = parse_age(row.get("age_at_onset", ""))
        age_dx = parse_age(row.get("age_at_diagnosis", ""))
        if age_onset is not None and age_dx is not None and age_onset != age_dx:
            ax.plot(
                [age_onset, age_dx], [y_positions[i], y_positions[i]],
                color=colors[i], linewidth=3, alpha=0.3, zorder=1,
                solid_capstyle="round",
            )
            # Small marker at onset
            ax.scatter(
                age_onset, y_positions[i],
                s=40, c=colors[i], linewidth=0.5,
                marker="|", alpha=0.7, zorder=2,
            )

    # Plot diagnosis markers
    for i in range(len(findings)):
        marker = "D" if categories[i] == "Congenital Developmental" else "o"
        alpha = 0.85 if has_age[i] else 0.35
        edge = "black" if has_age[i] else "#999999"
        ax.scatter(
            x_vals[i], y_positions[i],
            s=200, c=colors[i], edgecolors=edge, linewidth=0.8,
            marker=marker, alpha=alpha, zorder=3,
        )

    # Label findings
    for i, row in enumerate(data):
        label = row["finding"]
        if len(label) > 55:
            label = label[:52] + "..."
        age_str = ""
        if has_age[i]:
            if x_vals[i] == 0:
                age_str = " (congenital)"
            else:
                age_str = f" (age ~{int(x_vals[i])})"
        else:
            age_str = " (age unknown)"

        rate = row.get("tissue_turnover_rate", "")
        rate_str = ""
        if rate and rate not in ("N/A (neural)", "N/A (immune)"):
            rate_str = f"  [{rate}]"

        ax.text(
            max(35, max(x_vals) + 2), y_positions[i],
            f"{label}{age_str}{rate_str}",
            fontsize=6.5, va="center", ha="left", color="#333333",
        )

    # Axis formatting — real age scale
    ax.set_xlabel("Age at Diagnosis (years)", fontsize=11, fontweight="bold")
    ax.set_yticks([])
    ax.set_xlim(-2, max(35, max(x_vals) + 25))

    # Life stage shading
    ax.axvspan(-1, 0.5, alpha=0.06, color="#1565C0", zorder=0)
    ax.axvspan(0.5, 12, alpha=0.04, color="#78909C", zorder=0)
    ax.axvspan(12, 18, alpha=0.04, color="#FF8F00", zorder=0)
    ax.axvspan(18, 35, alpha=0.03, color="#D32F2F", zorder=0)

    ax.text(-0.5, -0.8, "Birth", fontsize=7, ha="center", color="#1565C0",
            fontstyle="italic", alpha=0.8)
    ax.text(6, -0.8, "Childhood", fontsize=7, ha="center", color="#78909C",
            fontstyle="italic", alpha=0.8)
    ax.text(15, -0.8, "Adolescence", fontsize=7, ha="center", color="#FF8F00",
            fontstyle="italic", alpha=0.8)
    ax.text(26, -0.8, "Adulthood", fontsize=7, ha="center", color="#D32F2F",
            fontstyle="italic", alpha=0.8)

    ax.set_title(
        "POLE c.138del — Chronological Phenotype Timeline\n"
        "Age-at-Diagnosis with Tissue Turnover Rates (bars show symptom onset → diagnosis)",
        fontsize=12, fontweight="bold", pad=15,
    )

    # Model 4 annotation
    ax.annotate(
        "Model 4 prediction: high-turnover tissues\n"
        "affected first / most severely\n"
        "\n"
        "Observed: colonic epithelium (3-5 day turnover)\n"
        "→ first non-congenital diagnosis at age 19",
        xy=(0.02, 0.02), xycoords="axes fraction",
        fontsize=7.5, fontstyle="italic", color="#555555",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5",
                  edgecolor="#CCCCCC", alpha=0.9),
    )

    # Vertical line at age 19 (first non-congenital finding)
    ax.axvline(x=19, color="#D32F2F", linewidth=0.8, linestyle=":", alpha=0.4, zorder=0)
    ax.text(19, len(findings) + 0.3, "First adenomas\n(age 19)",
            fontsize=6.5, ha="center", color="#D32F2F", alpha=0.6)

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


def generate_turnover_vs_age(timeline_data, replication_data):
    """Scatter plot: tissue turnover rate vs age-at-diagnosis.

    Directly tests Model 4 prediction: faster-dividing tissues should
    present clinically at younger ages.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Build a lookup of tissue turnover rates from replication data
    turnover_lookup = {}
    for row in replication_data:
        turnover_lookup[row["tissue"]] = turnover_to_numeric(row["turnover_days"])

    # Map timeline findings to their tissue turnover and age
    plotted = []
    for row in timeline_data:
        age_dx = parse_age(row.get("age_at_diagnosis", ""))
        if age_dx is None or age_dx == 0:
            continue  # skip unknowns and congenital

        tissue = row.get("tissue", "")
        turnover = turnover_lookup.get(tissue)
        if turnover is None:
            # Try to infer from tissue_turnover_rate column
            rate_str = row.get("tissue_turnover_rate", "")
            if "3-5" in rate_str or "3–5" in rate_str:
                turnover = 4
            elif "2-8" in rate_str or "2–8" in rate_str:
                turnover = 5
            elif "monthly" in rate_str:
                turnover = 28
            elif "8 year" in rate_str:
                turnover = 2920
            elif "variable" in rate_str.lower() or "hormonal" in rate_str.lower():
                turnover = 60
            else:
                continue

        cat = row["phenotype_category"]
        color = CATEGORY_COLORS.get(cat, "#78909C")
        plotted.append((turnover, age_dx, row["finding"], color, cat))

    if not plotted:
        plt.close(fig)
        return None

    turnovers = [p[0] for p in plotted]
    ages = [p[1] for p in plotted]
    labels = [p[2] for p in plotted]
    colors = [p[3] for p in plotted]

    ax.scatter(turnovers, ages, s=180, c=colors, edgecolors="black",
               linewidth=0.8, alpha=0.85, zorder=3)

    # Annotate each point
    for i, (t, a, label, c, _) in enumerate(plotted):
        short = label if len(label) <= 40 else label[:37] + "..."
        ax.annotate(
            short,
            xy=(t, a),
            xytext=(10, 5),
            textcoords="offset points",
            fontsize=6.5, color="#333333",
            arrowprops=dict(arrowstyle="-", color="#CCCCCC", lw=0.5),
        )

    # Trend line (log-linear fit)
    log_turnovers = np.log10(turnovers)
    if len(set(log_turnovers)) > 1:
        coeffs = np.polyfit(log_turnovers, ages, 1)
        trend_x = np.linspace(min(log_turnovers) - 0.2, max(log_turnovers) + 0.2, 100)
        trend_y = np.polyval(coeffs, trend_x)
        ax.plot(10**trend_x, trend_y, color="#D32F2F", linewidth=1.5, linestyle="--",
                alpha=0.5, zorder=1, label=f"Trend (slope={coeffs[0]:.1f} yr/log₁₀day)")

    # Model 4 prediction arrow
    ax.annotate(
        "Model 4 prediction:\nfaster turnover → earlier diagnosis",
        xy=(0.05, 0.95), xycoords="axes fraction",
        fontsize=8, fontstyle="italic", color="#555555",
        va="top",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5",
                  edgecolor="#CCCCCC", alpha=0.9),
    )

    ax.set_xscale("log")
    ax.set_xlabel("Cell Turnover Period (days, log scale)", fontsize=11, fontweight="bold")
    ax.set_ylabel("Age at Diagnosis (years)", fontsize=11, fontweight="bold")
    ax.set_title(
        "POLE c.138del — Tissue Turnover Rate vs. Age at Diagnosis\n"
        "Testing Model 4: Faster-Dividing Tissues Present Earlier",
        fontsize=12, fontweight="bold", pad=15,
    )

    ax.grid(alpha=0.2, linestyle="--")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=CATEGORY_COLORS[cat], edgecolor="black", label=cat)
        for cat in ["Neoplastic", "Proliferative/Stromal", "Endometrial/Hormonal",
                     "Comorbidity"]
        if any(p[4] == cat for p in plotted)
    ]
    if legend_elements:
        ax.legend(handles=legend_elements, loc="lower right", fontsize=7.5, framealpha=0.9)

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

    # Figure 2: Phenotype timeline (real age axis)
    fig2 = generate_phenotype_timeline(timeline_data)
    for ext, fmt, dpi in [("svg", "svg", None), ("png", "png", 300)]:
        path = os.path.join(SCRIPT_DIR, f"phenotype_timeline.{ext}")
        kwargs = {"format": fmt, "bbox_inches": "tight"}
        if dpi:
            kwargs["dpi"] = dpi
        fig2.savefig(path, **kwargs)
        print(f"Saved: {path}")
    plt.close(fig2)

    # Figure 3: Turnover rate vs. age-at-diagnosis (Model 4 test)
    fig3 = generate_turnover_vs_age(timeline_data, replication_data)
    if fig3 is not None:
        for ext, fmt, dpi in [("svg", "svg", None), ("png", "png", 300)]:
            path = os.path.join(SCRIPT_DIR, f"turnover_vs_age_diagnosis.{ext}")
            kwargs = {"format": fmt, "bbox_inches": "tight"}
            if dpi:
                kwargs["dpi"] = dpi
            fig3.savefig(path, **kwargs)
            print(f"Saved: {path}")
        plt.close(fig3)


if __name__ == "__main__":
    main()
