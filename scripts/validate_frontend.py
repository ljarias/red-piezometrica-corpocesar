"""Validaciones estáticas mínimas del frontend antes de publicar."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
APP = (ROOT / "assets/app.js").read_text(encoding="utf-8")
CSS = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

errors = []

for required in [
    'lang="es"',
    'id="mainContent"',
    'class="skip-link"',
    'role="tablist"',
    'role="tabpanel"',
    'aria-live="polite"',
]:
    if required not in HTML:
        errors.append(f"Falta requisito accesible: {required}")

ids = re.findall(r'\bid="([^"]+)"', HTML)
duplicates = sorted({x for x in ids if ids.count(x) > 1})
if duplicates:
    errors.append("IDs HTML duplicados: " + ", ".join(duplicates))

for label_for in re.findall(r'<label\s+for="([^"]+)"', HTML):
    if f'id="{label_for}"' not in HTML:
        errors.append(f"Label apunta a ID inexistente: {label_for}")

if "javascript:" in HTML.lower() or "javascript:" in APP.lower():
    errors.append("Se detecto esquema javascript: no autorizado.")

if not CSS.strip() or not APP.strip():
    errors.append("CSS o JavaScript principal vacio.")

if errors:
    raise SystemExit("ERROR FRONTEND:\n- " + "\n- ".join(errors))

print("OK frontend: controles estaticos de accesibilidad e integridad superados.")
