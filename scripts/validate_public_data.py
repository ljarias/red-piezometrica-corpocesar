"""Control de privacidad del artefacto público antes del despliegue."""
import json
from urllib.parse import urlparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data/generated/master.json"

ALLOWED_URL_HOSTS = {"naturalsig.org", "www.naturalsig.org"}
URL_FIELDS = {"ficha", "disenos_mecanicos", "fotos", "icon_ft", "icon_dm", "icon_foto"}

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

bad_urls = []
for i, row in enumerate(records, start=1):
    if not isinstance(row, dict):
        continue
    for field in URL_FIELDS:
        value = row.get(field)
        if not value:
            continue
        parsed = urlparse(str(value))
        if parsed.scheme != "https" or parsed.hostname not in ALLOWED_URL_HOSTS:
            bad_urls.append(f"fila {i}, {field}: {value}")

if bad_urls:
    raise SystemExit(
        "ERROR DE SEGURIDAD: URL no autorizada en dataset público: "
        + " | ".join(bad_urls[:10])
    )

print(f"OK privacidad: {len(records)} registros revisados; sin campos prohibidos ni URLs no autorizadas.")
