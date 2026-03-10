# mlruns

The local MLflow tracking store created by `src/train.py` (`file://<cwd>/mlruns`). The runs are
artefacts, not source - `mlruns/` is ignored by DVC and by git, and a fresh clone recreates it on
the first training run.
