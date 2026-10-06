import importlib
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import nltk  # noqa: E402


class ImportIsOfflineTests(unittest.TestCase):
    def test_import_does_not_download(self):
        with mock.patch.object(nltk, "download") as download:
            sys.modules.pop("preprocessing", None)
            importlib.import_module("preprocessing")
            download.assert_not_called()

    def test_ensure_with_no_packages_touches_nothing(self):
        preprocessing = importlib.import_module("preprocessing")
        with mock.patch.object(nltk, "download") as download:
            preprocessing.ensure_nltk_data(packages=())
            download.assert_not_called()


if __name__ == "__main__":
    unittest.main()
