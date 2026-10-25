"""Regresiones de la cadena de suministro P08; sin dependencias de pip."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_supply_chain import (  # noqa: E402
    SBOM_PATH,
    VENDOR_PATH,
    audit,
    audit_assets,
    audit_frontend,
    audit_workflows,
)


class SupplyChainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sbom = json.loads(SBOM_PATH.read_text(encoding="utf-8"))
        cls.assets = runpy.run_path(str(VENDOR_PATH))["ASSETS"]
        cls.app = (ROOT / "assets" / "app.js").read_text(encoding="utf-8")
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_declared_components_and_actions_consistent(self):
        self.assertEqual([], audit())

    def test_manifest_fails_when_expected_digest_is_modified(self):
        changed = copy.deepcopy(self.sbom["components"])
        asset = next(x for x in changed if x.get("type") == "file")
        prop = next(x for x in asset["properties"] if x["name"] == "p08:sha384-base64")
        prop["value"] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        issues = audit_assets(self.assets, changed)
        self.assertTrue(any("No coincide hash" in x for x in issues), issues)

    def test_popup_html_string_regression_detected(self):
        changed = self.app.replace(
            ".bindPopup(popupContent(r))",
            ".bindPopup('texto no confiable')",
        )
        problems = audit_frontend(changed, self.html)
        self.assertTrue(any("Popup Leaflet" in x for x in problems), problems)

    def test_osm_deprecated_subdomains_rejected(self):
        changed = self.app.replace(
            "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        )
        problems = audit_frontend(changed, self.html)
        self.assertTrue(any("OSM" in x for x in problems), problems)

    def test_action_sha_changes_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "changed.yml"
            path.write_text(
                "steps:\\n  - uses: actions/checkout@" + "0" * 40 + "\\n",
                encoding="utf-8",
            )
            problems = audit_workflows(Path(directory))
            self.assertTrue(any("SHA distinto" in x for x in problems), problems)

    def test_unpinned_action_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe.yml"
            path.write_text("jobs:\n  build:\n    steps:\n      - uses: actions/checkout@v6\n", encoding="utf-8")
            problems = audit_workflows(Path(directory))
            self.assertTrue(any("Action no fijada" in x for x in problems), problems)


if __name__ == "__main__":
    unittest.main()
