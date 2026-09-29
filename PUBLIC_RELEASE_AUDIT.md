# Public Release Audit

## Sources consulted

- Read-only master project: `player-sale-share-optimization`.
- Final two-page Problem 8 paper.
- Final findings and decision report and its validation results.
- Final handoff, claim ledger, scientific summary, model documentation, result tables, figure
  manifest, and validation scripts.

## Included artifacts

- Final paper under a clean public filename.
- Research-generated R0 held-out failure, dimensional-diagnosis, and R4 post-hoc figures.
- Aggregate dataset, forecast, R0, R4, and model-status results.
- Public-safe validation and summary-figure scripts.
- Methodology, provenance, reproducibility, limitations, model-status, and figure-registry notes.
- Researcher photograph and collaboration logo supplied for release use.

## Excluded artifacts

- Raw, processed, row-level, player-level, database, Parquet, and serialized-model files.
- Scenario-level predictions and identifiable player examples.
- Internal reports, planning notes, reviewer discussions, and earlier manuscripts.
- Exploratory and superseded figures and outputs.
- Proprietary formulas or software internals.

## Data redistribution decision

No raw or row-level data are included because public redistribution rights are not established for
every source. The package contains only aggregate outputs, schemas, and reconstruction guidance.
Reproducibility is therefore partial.

## Official software screenshot decision

The screenshot embedded in the final paper is application context rather than a research-model
output. No standalone screenshot is included because repository redistribution permission was not
documented. The final paper remains unchanged and retains its explicit context caption.

## Figure audit

- `r0_heldout_failure.png`: research-generated; held-out R0 result.
- `r0_dimensional_mismatch_diagnosis.png`: research-generated; post-hoc mechanism diagnosis.
- `r4_posthoc_evidence.png`: research-generated; post-hoc evidence, not independently validated.

## Scientific consistency

- Data: 8,433 events; 1,132 players; La Liga; 2022-07-01 to 2025-06-30; zero leakage violations.
- Coverage: 12-month primary 54.06%; 24-month 25.36% low-confidence; 36-month 0%.
- Forecast: held-out log-MAE 0.526; persistence 0.577; Spearman 0.582.
- R0: 148,176 held-out scenarios; 100% recommend at least 99.9% sale; not supported.
- R4: 59.4% outside the at-least-99% bucket; +EUR167,138 mean versus B3; 95% interval
  [+EUR14,634, +EUR243,196]; regret EUR992,618 versus EUR1,159,756.
- R4 remains post-hoc on the already-open test set and requires fresh-data validation.
- The known disputed R0-versus-B3 euro amount is deliberately omitted; only the final qualitative
  conclusion that R0 did not clearly outperform B3 is published.

## License decision

The MIT license applies only to repository software. It does not grant rights to the paper, data,
software screenshots, logos, trademarks, photographs, or external assets.

## Validation and publication

- Public release validator: PASS.
- Public-safe summary-figure generation: PASS.
- Python compilation: PASS.
- `CITATION.cff` YAML parse: PASS.
- README relative links: PASS; six local links resolved.
- Final paper: PASS; two A4 pages and all headline results present.
- Secret and credential scan: PASS.
- Restricted-file and row-level-data scan: PASS.
- Symlink, portability, and large-file scans: PASS.
- Internal-person/reviewer phrase scan: PASS.
- Staged-path inspection: PASS; 25 intended public-release files and no restricted extensions.
- Content release commit: `bb2be5bbe3da3601940157d15819119248222850`.
- Remote: `https://github.com/RupayanHalder39/MITSloanProblem8-Player-Sale-Share-Optimization.git`
- Remote preflight: reachable and empty.
- Push status: SUCCESS; `main` published to `origin/main` without force.

## Remaining limitations

Full empirical reproduction requires authorized source data. R4 has no genuinely fresh-data
validation, offer prices are scenarios rather than observed bids, optimal-share labels are absent,
and risk preferences are not calibrated to a real club.
