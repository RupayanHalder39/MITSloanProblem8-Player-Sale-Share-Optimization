"""Verify the Problem 8 public release without restricted data."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def check(value: bool, message: str) -> None:
    if not value:
        ERRORS.append(message)


def table(name: str) -> list[dict[str, str]]:
    with (ROOT / "results" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def metric_map(name: str) -> dict[str, str]:
    return {row["metric"]: row["value"] for row in table(name)}


required = [
    "README.md", "LICENSE", "CITATION.cff", "PUBLIC_RELEASE_AUDIT.md",
    "paper/Problem8_Player_Sale_Share_Optimization.pdf", "figures/r0_heldout_failure.png",
    "figures/r4_posthoc_evidence.png", "figures/r0_dimensional_mismatch_diagnosis.png",
    "results/dataset_summary.csv", "results/forecast_metrics.csv",
    "results/r0_heldout_summary.csv", "results/r4_posthoc_summary.csv",
    "results/variant_status.csv", "docs/model_status.md", "docs/figure_registry.md",
]
for path in required:
    check((ROOT / path).is_file(), f"missing required file: {path}")

data = metric_map("dataset_summary.csv")
expected_data = {
    "player_decision_events": "8433", "players": "1132", "competition": "La Liga",
    "start_date": "2022-07-01", "end_date": "2025-06-30",
    "temporal_leakage_violations": "0", "primary_horizon_months": "12",
    "primary_horizon_usable_coverage_percent": "54.06",
    "24_month_usable_coverage_percent": "25.36", "36_month_usable_coverage_percent": "0",
}
for key, expected in expected_data.items():
    check(data.get(key) == expected, f"dataset summary mismatch: {key}")

forecast = metric_map("forecast_metrics.csv")
for key, expected in {"heldout_log_mae": 0.526, "persistence_log_mae": 0.577,
                      "heldout_spearman": 0.582}.items():
    check(key in forecast and abs(float(forecast[key]) - expected) < 1e-12,
          f"forecast mismatch: {key}")

r0 = metric_map("r0_heldout_summary.csv")
check(r0.get("scenarios") == "148176", "R0 scenario count mismatch")
check(r0.get("percent_recommending_at_least_99_9_percent_sale") == "100", "R0 collapse mismatch")
check(r0.get("verdict") == "NOT SUPPORTED", "R0 verdict mismatch")

r4 = metric_map("r4_posthoc_summary.csv")
expected_r4 = {
    "percent_outside_at_least_99_percent_sale_bucket": 59.4,
    "mean_realized_value_difference_vs_b3_eur": 167138,
    "bootstrap_95_low_eur": 14634, "bootstrap_95_high_eur": 243196,
    "mean_regret_r4_eur": 992618, "mean_regret_b3_eur": 1159756,
}
for key, expected in expected_r4.items():
    check(key in r4 and abs(float(r4[key]) - expected) < 1e-9, f"R4 mismatch: {key}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for fragment in ["8,433", "1,132", "54.06%", "0.526", "0.577", "0.582", "148,176",
                 "59.4%", "+EUR167,138", "+EUR14,634", "+EUR243,196", "EUR992,618",
                 "EUR1,159,756",
                 "Because R4 was developed after examining the held-out results, these findings require confirmation on genuinely fresh data."]:
    check(fragment in readme, f"README missing: {fragment}")
check("production-ready" not in readme.lower(), "README contains production-ready claim")
check(("/" + "Users/") not in readme, "README contains absolute local path")

restricted = {".parquet", ".duckdb", ".db", ".sqlite", ".sqlite3", ".joblib", ".pkl"}
local_prefix = "/" + "Users/rupayan/"
for path in ROOT.rglob("*"):
    if path.is_symlink():
        ERRORS.append(f"symlink present: {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in restricted:
        ERRORS.append(f"restricted file present: {path.relative_to(ROOT)}")
    if path.is_file() and path.stat().st_size > 25 * 1024 * 1024:
        ERRORS.append(f"unexpected large file: {path.relative_to(ROOT)}")
    if path.is_file() and path.suffix.lower() in {".md", ".py", ".csv", ".cff", ".txt"}:
        text = path.read_text(encoding="utf-8", errors="replace")
        check(local_prefix not in text, f"absolute local path: {path.relative_to(ROOT)}")
        check(not re.search(r"AKIA[0-9A-Z]{16}", text), f"possible AWS key: {path.relative_to(ROOT)}")

if ERRORS:
    print("PUBLIC RELEASE VERIFICATION: FAIL")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print("PUBLIC RELEASE VERIFICATION: PASS")
print("Forecast: held-out log-MAE 0.526; persistence 0.577; Spearman 0.582")
print("R0: 148,176 scenarios; 100% at least 99.9% sale; NOT SUPPORTED")
print("R4: post-hoc, promising, not independently validated")
print("Reproducibility: PARTIAL")
