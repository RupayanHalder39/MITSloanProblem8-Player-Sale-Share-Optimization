# Methodology

## Data and time design

The canonical unit is a player-decision event. The study contains 8,433 events for 1,132 La Liga
players from 2022-07-01 through 2025-06-30. Chronological separation produced zero temporal-leakage
violations in the final audit.

The primary forecast horizon is 12 months. Usable label coverage is 54.06%. Twenty-four-month
coverage is 25.36% and low-confidence; 36-month coverage is unavailable.

## Forecast

A gradient-boosted model forecasts approximately 12-month future player value. Held-out evaluation
uses log-MAE and Spearman correlation. Persistence is the naive reference.

## Decision framework

For each scenario, the framework combines current player value, forecast future value, offer size,
share sold, immediate cash, retained upside, discounting, uncertainty, and a risk preference. Offer
amounts and risk settings are scenario inputs rather than historical labels or calibrated club
preferences.

R0 is the original mean-variance objective. B3 is the transparent risk-neutral boundary comparator.
After R0 failed its held-out test, R1 through R5 were examined as post-hoc reformulations. R4 uses a
CRRA certainty-equivalent approach and is the most promising of those post-hoc variants.

## Evidence separation

R0's collapse and verdict are held-out findings. The dimensional diagnosis and every R1-R5 result
are post-hoc. R4 was evaluated on the same already-open held-out test set and has no independent
fresh-data confirmation.
