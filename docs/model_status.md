# Model status

| Component | Status | Interpretation |
|---|---|---|
| Twelve-month forecast | Held-out tested | Modest predictive skill relative to persistence |
| R0 original decision rule | Held-out tested — **not supported** | Collapsed to near-total sale across all 148,176 scenarios |
| B3 comparator | Transparent reference | Risk-neutral boundary rule with no fitted risk preference |
| R1, R2, R3, R5 | Post-hoc | Diagnostic or graduated alternatives without favorable validated evidence |
| R4 | Post-hoc — promising, not independently validated | Aggregate advantage versus B3 on the already-open test set |
| Production deployment | Not established | Fresh-data validation and operational calibration are required |
| Historical optimal-share learning | Not performed | Labels are unavailable |
| Historical offer-price modeling | Not performed | Offers are scenario inputs |
| Real-club risk-preference calibration | Not performed | Risk settings are demonstrations, not learned club preferences |

R4 must not be presented as the held-out winner. The scientific sequence is forecast skill, R0
held-out failure, post-hoc diagnosis, post-hoc reformulation, and required fresh-data testing.
