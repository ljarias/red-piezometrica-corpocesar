"""Pruebas de contrato para los artefactos públicos del dashboard."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "data" / "generated"


def load(name):
    return json.loads((GEN / name).read_text(encoding="utf-8"))


class PublicDataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = load("master.json")
        cls.measurements = load("measurements.json")
        cls.quality = load("quality.json")
        cls.meta = load("meta.json")

    def test_required_files_are_lists_or_object(self):
        self.assertIsInstance(self.master, list)
        self.assertIsInstance(self.measurements, list)
        self.assertIsInstance(self.quality, list)
        self.assertIsInstance(self.meta, dict)

    def test_master_piezometers_are_unique(self):
        ids = [r.get("piezometro") for r in self.master]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_measurements_reference_master(self):
        ids = {r["piezometro"] for r in self.master}
        unknown = sorted({r.get("piezometro") for r in self.measurements if r.get("piezometro") not in ids})
        self.assertEqual([], unknown, f"Lecturas con piezometro inexistente: {unknown}")

    def test_coordinates_are_geographic(self):
        for row in self.master:
            lat, lon = row.get("latitud"), row.get("longitud")
            if lat is not None:
                self.assertGreaterEqual(float(lat), -90)
                self.assertLessEqual(float(lat), 90)
            if lon is not None:
                self.assertGreaterEqual(float(lon), -180)
                self.assertLessEqual(float(lon), 180)

    def test_meta_counts_match_artifacts(self):
        self.assertEqual(self.meta.get("piezometros_maestro"), len(self.master))
        self.assertEqual(self.meta.get("registros"), len(self.measurements))

    def test_dates_are_not_reversed(self):
        self.assertLessEqual(self.meta.get("fecha_min"), self.meta.get("fecha_max"))

    def test_no_forbidden_public_fields(self):
        forbidden = {"propietario", "x", "y", "fecha_prueba_bombeo"}
        found = forbidden.intersection({k for row in self.master for k in row})
        self.assertFalse(found, f"Campos prohibidos publicados: {sorted(found)}")


if __name__ == "__main__":
    unittest.main()
