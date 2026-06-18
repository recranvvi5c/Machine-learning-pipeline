import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from config_safety import metric_from_name, parse_grid_value  # noqa: E402


class GridParsingTests(unittest.TestCase):
    def test_reads_literal_lists_and_numbers(self):
        self.assertEqual(parse_grid_value("[0.1, 1, 10]"), [0.1, 1, 10])
        self.assertEqual(parse_grid_value("3"), 3)

    def test_rejects_code(self):
        for bad in ("__import__('os').getcwd()", "open('/etc/passwd')", "x + 1"):
            with self.assertRaises(ValueError) as ctx:
                parse_grid_value(bad)
            self.assertIn("not a literal", str(ctx.exception))


class MetricRegistryTests(unittest.TestCase):
    def test_known_metric_resolves(self):
        from sklearn.metrics import f1_score
        self.assertIs(metric_from_name("f1_score"), f1_score)

    def test_unknown_metric_lists_the_accepted_names(self):
        with self.assertRaises(ValueError) as ctx:
            metric_from_name("macro_f1")
        self.assertIn("f1_score", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
