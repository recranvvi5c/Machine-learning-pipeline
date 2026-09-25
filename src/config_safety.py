"""Safe parsing for Hydra config values.

The parameter grid holds YAML strings such as "[0.1, 1, 10]" and the metric name is a
plain string. Parsing them with `eval` would execute arbitrary code from a config file,
so both entry points are explicit here and raise a message that names the offending key.
"""

import ast
from sklearn import metrics

_METRICS = {
    "f1_score": metrics.f1_score,
    "accuracy_score": metrics.accuracy_score,
    "roc_auc_score": metrics.roc_auc_score,
    "precision_recall_fscore_support": metrics.precision_recall_fscore_support,
    "confusion_matrix": metrics.confusion_matrix,
}


def parse_grid_value(text):
    """Parse one grid value. Only literals are accepted - never names or calls."""
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError) as exc:
        raise ValueError("grid value %r is not a literal: %s" % (text, exc)) from exc


def metric_from_name(name):
    """Resolve a metric by name instead of evaluating it."""
    try:
        return _METRICS[name]
    except KeyError:
        raise ValueError(
            "unknown metric %r; accepted: %s" % (name, ", ".join(sorted(_METRICS)))
        ) from None
