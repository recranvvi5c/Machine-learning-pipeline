# Configs

Three layers, composed by Hydra:

- `data_preprocess.yaml` - paths and text cleaning for the preprocessing step.
- `hyperparameters.yaml` - the model grid. Values are literals (lists and numbers); they are parsed
  with `ast.literal_eval`, never evaluated.
- `model/` - one file per estimator (`random_forest.yaml`, `svc.yaml`) holding the pipeline steps.

`.` - run overrides on the command line, e.g. `svc__C=10`.
