# Slipway

An MLOps platform: models are tested, versioned and deployed through a gated CI/CD pipeline, then monitored for drift in production.

> **Status: planned.** This repository is a skeleton. The plan is below; work starts at M1.

## What it will do

- Trains models reproducibly and tracks experiments, parameters and artefacts.
- Promotes models through a registry only when evaluation gates pass in CI.
- Serves models behind an API with canary releases and one-step rollback.
- Monitors live inputs and predictions for drift (PSI, KS tests) and alerts on it.

## Planned stack

Python · scikit-learn · MLflow · FastAPI · Docker · GitHub Actions

## Milestones

- [x] **M0**: repository skeleton and CI
- [ ] **M1**: Reproducible training and experiment tracking
- [ ] **M2**: Model registry with evaluation gates in CI
- [ ] **M3**: Serving with canary deploys and rollback
- [ ] **M4**: Drift detection, dashboards and alerting

## Layout

```
src/slipway/   package source
tests/             unit tests
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests -v
```

---

Part of [Sagar Arora's data engineering projects](https://github.com/sagararora492).
