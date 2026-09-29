# Data provenance and availability

The study combined player valuation history and football performance/context information to form
chronological player-decision events. The master audit found no public redistribution permission
covering every raw source and derived player-level record.

Accordingly, this repository excludes raw data, processed row-level data, player-level analytical
tables, databases, Parquet files, serialized models, and scenario-level predictions. It publishes
only aggregate metrics and scientific figures.

An authorized reconstruction requires fields sufficient to represent event date, stable player
identity, competition, current value, future qualifying value, player attributes and performance
context available at the decision date, chronological split assignment, forecast outputs,
uncertainty, offer scenario, discount rate, risk setting, candidate sale share, and realized-value
evaluation.

The study contains no general historical optimal-share labels and no historical offer-price
dataset. Scenario offers must never be presented as observed transactions. No license in this
repository grants rights to excluded or third-party data.
