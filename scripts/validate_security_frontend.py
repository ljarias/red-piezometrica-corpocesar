"""Pruebas estáticas de regresión para controles XSS/URL del frontend."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
APP=(ROOT/"assets/app.js").read_text(encoding="utf-8")
checks={
 "escape HTML definido": "const esc=" in APP,
 "allowlist URL definida": "const safeUrl=" in APP,
 "solo HTTPS en safeUrl": "u.protocol==='https:'" in APP,
 "dominios permitidos explícitos": "['naturalsig.org','www.naturalsig.org']" in APP,
 "opciones creadas con DOM": ".replaceChildren()" in APP and "document.createElement('option')" in APP,
 "noopener en enlaces nuevos": 'rel="noopener noreferrer"' in APP,
}
# Patrones peligrosos que no deben reaparecer en href dinámicos.
bad=[
 r'href="\$\{r\.ficha\}',
 r'href="\$\{r\.disenos_mecanicos\}',
 r'href="\$\{r\.fotos\}',
]
for pat in bad:
    checks[f"sin enlace dinámico crudo: {pat}"]=re.search(pat,APP) is None
failed=[name for name,ok in checks.items() if not ok]
for name,ok in checks.items(): print(f"[{'OK' if ok else 'FALLO'}] {name}")
if failed: raise SystemExit("ERROR hardening XSS/URL:\n- "+"\n- ".join(failed))
print("OK hardening: controles XSS/URL presentes y enlaces documentales crudos ausentes.")
