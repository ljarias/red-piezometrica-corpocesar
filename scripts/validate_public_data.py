"""Control de privacidad del artefacto público antes del despliegue."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data/generated/master.json"

FORBIDDEN_FIELDS = {
    "propietario",
    "x",
    "y",
    "fecha_prueba_bombeo",
}

if not MASTER.exists():
    raise SystemExit("ERROR: no existe data/generated/master.json")

records = json.loads(MASTER.read_text(encoding="utf-8"))
if not isinstance(records, list):
    raise SystemExit("ERROR: master.json debe contener una lista")

found = sorted({
    key
    for row in records
    if isinstance(row, dict)
    for key in row
    if key in FORBIDDEN_FIELDS
})

if found:
    raise SystemExit(
        "ERROR DE PRIVACIDAD: campos no autorizados en master.json: "
        + ", ".join(found)
    )

print(f"OK privacidad: {len(records)} registros revisados; sin campos prohibidos.")
