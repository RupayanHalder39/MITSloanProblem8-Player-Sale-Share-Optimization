"""Generate public-safe summary figures from aggregate release tables."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def rows(name: str) -> dict[str, str]:
    with (ROOT / "results" / name).open(newline="", encoding="utf-8") as handle:
        return {row["metric"]: row["value"] for row in csv.DictReader(handle)}


def save(fig, output: Path, name: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    fig.savefig(output / f"{name}.png", dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def r0_summary(output: Path) -> None:
    r0 = rows("r0_heldout_summary.csv")
    fig, ax = plt.subplots(figsize=(8.8, 4.8), facecolor="white")
    offers = np.arange(0.7, 1.31, 0.1)
    ax.plot(offers, np.repeat(100.0, len(offers)), "o-", color="#B6403C", linewidth=2.3)
    ax.set_ylim(98.8, 100.25)
    ax.set_xlabel("Offer multiplier")
    ax.set_ylabel("Recommended sale share (%)")
    ax.set_title("Original R0 held-out failure", loc="left", fontsize=16, fontweight="bold")
    ax.text(0.7, 98.95,
            f"{r0['percent_recommending_at_least_99_9_percent_sale']}% of "
            f"{int(r0['scenarios']):,} scenarios recommended at least 99.9% sale",
            color="#B6403C", fontweight="bold")
    ax.grid(axis="y", color="#E5E7EB")
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.98, 0.02, "Held-out result - verdict: NOT SUPPORTED", ha="right", color="#234F6D")
    save(fig, output, "r0_heldout_summary")


def r4_summary(output: Path) -> None:
    r4 = rows("r4_posthoc_summary.csv")
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2), facecolor="white")
    axes[0].bar(["R0", "R4"], [0, float(r4["percent_outside_at_least_99_percent_sale_bucket"])],
                color=["#A0A0A0", "#7C50A6"])
    axes[0].set_title("Decision diversity")
    axes[0].set_ylabel("Scenarios outside >=99% sale (%)")
    axes[1].bar(["R4 vs. B3"], [float(r4["mean_realized_value_difference_vs_b3_eur"])], color="#7C50A6")
    axes[1].set_title("Mean realized-value difference")
    axes[1].set_ylabel("EUR")
    axes[2].bar(["B3", "R4"], [float(r4["mean_regret_b3_eur"]), float(r4["mean_regret_r4_eur"])],
                color=["#909090", "#7C50A6"])
    axes[2].set_title("Mean regret")
    axes[2].set_ylabel("EUR - lower is better")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#ECEFF1")
    fig.suptitle("R4 aggregate evidence relative to B3", fontsize=17, fontweight="bold")
    fig.text(0.5, -0.02,
             "Post-hoc analysis on the already-open test set - not independent validation",
             ha="center", color="#B6403C", fontweight="bold")
    fig.tight_layout()
    save(fig, output, "r4_posthoc_summary")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "figures" / "reproduced")
    args = parser.parse_args()
    r0_summary(args.output_dir)
    r4_summary(args.output_dir)
    print(f"Generated public-safe summary figures in {args.output_dir}")


if __name__ == "__main__":
    main()
