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
    'id="chartAltRows"',
    'id="compareAlt"',
    'id="levelAltRows"',
    'aria-pressed="true"',
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


# V4 hardening: las librerias de ejecucion no deben cargarse directamente desde CDN.
for forbidden_runtime_cdn in (
    "cdn.jsdelivr.net/npm/chart.js",
    "unpkg.com/leaflet@",
):
    if forbidden_runtime_cdn in HTML:
        errors.append(f"Dependencia CDN de ejecucion no permitida: {forbidden_runtime_cdn}")

for required_local_asset in (
    "assets/vendor/chartjs/chart.umd.min.js",
    "assets/vendor/leaflet/leaflet.js",
    "assets/vendor/leaflet/leaflet.css",
):
    if required_local_asset not in HTML:
        errors.append(f"Falta dependencia frontend local: {required_local_asset}")


# V4 hardening: política CSP mínima obligatoria.
for required_csp in (
    'http-equiv="Content-Security-Policy"',
    "default-src 'self'",
    "script-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
):
    if required_csp not in HTML:
        errors.append(f"Falta directiva CSP requerida: {required_csp}")

if "script-src 'self' 'unsafe-inline'" in HTML:
    errors.append("CSP no debe permitir unsafe-inline para scripts.")
if "script-src 'self' 'unsafe-eval'" in HTML:
    errors.append("CSP no debe permitir unsafe-eval para scripts.")


# V4.1: controles estáticos adicionales de reflow y accesibilidad.
for required_css in (
    ":focus-visible",
    "prefers-reduced-motion:reduce",
    "text-size-adjust:100%",
    "min-height:44px",
):
    if required_css not in CSS:
        errors.append(f"Falta control CSS de accesibilidad: {required_css}")

for required_semantic in (
    'role="status"',
    'aria-atomic="true"',
    '<caption>Datos de la serie temporal seleccionada</caption>',
    '<caption>Datos de nivel piezométrico</caption>',
):
    if required_semantic not in HTML:
        errors.append(f"Falta control semantico de accesibilidad: {required_semantic}")

if errors:
    raise SystemExit("ERROR FRONTEND:\n- " + "\n- ".join(errors))

print("OK frontend: controles estaticos de accesibilidad e integridad superados.")
