"""Auditoría P08 sin dependencias externas: integridad, workflows, URL y XSS."""
from __future__ import annotations

import base64
import binascii
import json
import re
import runpy
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SBOM_PATH = ROOT / "docs" / "SBOM_P08.json"
VENDOR_PATH = ROOT / "scripts" / "vendor_frontend.py"
WORKFLOWS = ROOT / ".github" / "workflows"

EXPECTED_LIBRARIES = {
    "pkg:npm/chart.js@4.4.7": ("chart.js", "4.4.7", "MIT"),
    "pkg:npm/leaflet@1.9.4": ("leaflet", "1.9.4", "BSD-2-Clause"),
}
EXPECTED_ETL = {"pandas": "2.2.3", "openpyxl": "3.1.5"}
VENDOR_HOSTS = {"cdn.jsdelivr.net", "unpkg.com"}
EXPECTED_ASSETS = 8


def audit_assets(assets: list[dict], components: list[dict]) -> list[str]:
    """Coteja SHA-384, procedencia, versión y rutas de los 8 recursos."""
    problems = []
    files = {c.get("name"): c for c in components if c.get("type") == "file"}
    if len(assets) != EXPECTED_ASSETS or len(files) != EXPECTED_ASSETS:
        problems.append("Se requieren exactamente ocho recursos vendor declarados.")
    seen = set()
    for asset in assets:
        rel = str(asset["path"].relative_to(ROOT)).replace("\\", "/")
        url = asset["url"]
        if rel in seen:
            problems.append(f"Archivo duplicado: {rel}")
        seen.add(rel)
        entry = files.get(rel)
        if not entry:
            problems.append(f"Archivo sin entrada en SBOM: {rel}")
            continue
        props = {x["name"]: x["value"] for x in entry.get("properties", [])}
        urls = [x["url"] for x in entry.get("externalReferences", [])]
        expected = asset["sha384"]
        if expected != props.get("p08:sha384-base64") or urls != [url]:
            problems.append(f"No coincide hash u origen declarado: {rel}")
        try:
            digest = base64.b64decode(expected, validate=True)
            if len(digest) != 48:
                raise ValueError("SHA-384 requiere 48 bytes")
        except (binascii.Error, ValueError, TypeError):
            problems.append(f"Hash SHA-384 inválido: {rel}")
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in VENDOR_HOSTS:
            problems.append(f"Origen de descarga no autorizado: {rel}")
        if rel.startswith("assets/vendor/chartjs/"):
            if "chart.js@4.4.7/" not in parsed.path:
                problems.append(f"Versión Chart.js no fijada: {rel}")
            expected_package = "pkg:npm/chart.js@4.4.7"
        elif rel.startswith("assets/vendor/leaflet/"):
            if "leaflet@1.9.4/" not in parsed.path:
                problems.append(f"Versión Leaflet no fijada: {rel}")
            expected_package = "pkg:npm/leaflet@1.9.4"
        else:
            problems.append(f"Ruta vendor no autorizada: {rel}")
            continue
        if props.get("p08:source-component") != expected_package:
            problems.append(f"Componente fuente incorrecto: {rel}")
    if set(files) != seen:
        problems.append("SBOM y script vendor contienen archivos distintos.")
    return problems


def audit_workflows(workflows: Path) -> list[str]:
    """Prohíbe acciones por etiqueta, PR privilegiados y privilegios globales amplios."""
    problems = []
    files = sorted(workflows.glob("*.yml")) + sorted(workflows.glob("*.yaml"))
    if not files:
        return ["No existen workflows YAML."]
    pinned = 0
    for path in files:
        source = path.read_text(encoding="utf-8")
        if re.search(r"^\s*pull_request_target\s*:", source, re.MULTILINE):
            problems.append(f"pull_request_target no autorizado: {path.name}")
        if re.search(r"^\s*permissions\s*:\s*write-all", source, re.MULTILINE):
            problems.append(f"Privilegios globales excesivos: {path.name}")
        for line in source.splitlines():
            match = re.match(r"^\s*-\s*uses\s*:\s*(\S+)", line)
            if not match:
                continue
            pinned += 1
            action = match.group(1)
            if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[a-f0-9]{40}", action):
                problems.append(f"Action no fijada con SHA completo: {path.name} / {action}")
    if pinned < 4:
        problems.append("Se esperan al menos las cuatro Actions originales fijadas por SHA.")
    return problems


def audit_frontend(app: str, html: str) -> list[str]:
    """Detecta regresión en el sink Leaflet y política de teselas."""
    problems = []
    calls = re.findall(r"\.bindPopup\s*\(([^)]*)\)", app)
    # Hay una única invocación de bindPopup en la aplicación.
    if calls != ["popupContent(r"]:
        problems.append("Popup Leaflet no usa el generador DOM de texto seguro.")
    begin = app.find("function popupContent(r){")
    end = app.find("function renderMap(", begin)
    if begin < 0 or end <= begin:
        problems.append("No se encontró generador DOM de popups.")
    else:
        snippet = app[begin:end]
        for required in ("document.createElement", ".textContent=", "document.createTextNode", "return wrapper;"):
            if required not in snippet:
                problems.append(f"Falta escape DOM en popup: {required}")
        if ".innerHTML" in snippet or "insertAdjacentHTML" in snippet:
            problems.append("El generador de popups no debe interpretar HTML.")
    if "https://tile.openstreetmap.org/{z}/{x}/{y}.png" not in app:
        problems.append("URL OSM no respeta el endpoint oficial.")
    if "{s}.tile.openstreetmap.org" in app:
        problems.append("No usar subdominios OSM antiguos.")
    if "https://tile.openstreetmap.org" not in html:
        problems.append("CSP no permite host oficial OSM.")
    if "https://*.tile.openstreetmap.org" in html:
        problems.append("CSP conserva subdominios OSM innecesarios.")
    for item in (
        "assets/vendor/chartjs/chart.umd.min.js",
        "assets/vendor/leaflet/leaflet.js",
        "assets/vendor/leaflet/leaflet.css",
    ):
        if item not in html:
            problems.append(f"Dependencia runtime ausente: {item}")
    return problems


def audit() -> list[str]:
    problems = []
    sbom = json.loads(SBOM_PATH.read_text(encoding="utf-8"))
    if sbom.get("bomFormat") != "CycloneDX" or sbom.get("specVersion") != "1.5":
        problems.append("El inventario no identifica el formato CycloneDX 1.5.")
    components = sbom.get("components", [])
    libraries = {c.get("bom-ref"): c for c in components if c.get("type") == "library"}
    for ref, (name, version, license_id) in EXPECTED_LIBRARIES.items():
        item = libraries.get(ref, {})
        if item.get("name") != name or item.get("version") != version:
            problems.append(f"Dependencia JS no coincide: {ref}")
        if license_id not in [v.get("license", {}).get("id") for v in item.get("licenses", [])]:
            problems.append(f"Licencia no documentada: {ref}")
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
    declared = dict(line.split("==", 1) for line in requirements if "==" in line)
    if declared != EXPECTED_ETL:
        problems.append("Requirements ETL se apartan del inventario aprobado.")
    for name, version in EXPECTED_ETL.items():
        if f"pkg:pypi/{name}@{version}" not in libraries:
            problems.append(f"Dependencia ETL omitida del inventario: {name}")
    assets = runpy.run_path(str(VENDOR_PATH))["ASSETS"]
    problems.extend(audit_assets(assets, components))
    problems.extend(audit_workflows(WORKFLOWS))
    problems.extend(audit_frontend(
        (ROOT / "assets" / "app.js").read_text(encoding="utf-8"),
        (ROOT / "index.html").read_text(encoding="utf-8"),
    ))
    return problems


def main() -> int:
    problems = audit()
    if problems:
        print("ERROR P08: \n- " + "\n- ".join(problems))
        return 1
    print("OK P08: BOM, 8 SHA-384, 4+ Actions SHA, licencias, CSP, OSM y popup DOM.")
    print("Alcance: controles preventivos; no equivale a escaneo CVE en línea ni aprobación jurídica.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
