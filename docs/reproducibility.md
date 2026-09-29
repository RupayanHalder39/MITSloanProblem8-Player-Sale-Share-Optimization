# Reproducibility

This is a partial reproduction package. It validates the public aggregate results and regenerates
release-safe summary figures without distributing restricted player-level data.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_release.py
python src/build_release_figures.py
```

The validator checks the data foundation, forecast metrics, R0 held-out failure, R4 post-hoc
metrics, evidence labels, required files, links, portability, restricted formats, symlinks, large
files, and selected secret patterns.

Full reconstruction requires authorized source data and the chronological feature pipeline. Any
fresh R4 evaluation must use data untouched by the post-hoc development process.
