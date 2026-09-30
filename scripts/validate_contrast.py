"""Auditoría reproducible de contraste para la paleta institucional del dashboard."""
from __future__ import annotations

PAIRS = [
    ("Texto principal", "#17344a", "#ffffff", 4.5),
    ("Texto secundario", "#596f7e", "#ffffff", 4.5),
    ("Eyebrow", "#3f718a", "#ffffff", 4.5),
    ("Pestaña activa", "#ffffff", "#0b5b8d", 4.5),
    ("Footer", "#5c707b", "#eef5f8", 4.5),
    ("Badge", "#34718d", "#e7f5fb", 4.5),
    ("Estado OK", "#276627", "#dff5df", 4.5),
    ("Estado incompleto", "#8b6500", "#fff0c9", 4.5),
    ("Estado crítico", "#9a3030", "#ffdada", 4.5),
    ("Ayuda de mapa", "#526b7a", "#ffffff", 4.5),
    ("Botón comparación activo", "#ffffff", "#0b5b8d", 4.5),
]

def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    rgb = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

def ratio(fg: str, bg: str) -> float:
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)

errors = []
for name, fg, bg, minimum in PAIRS:
    value = ratio(fg, bg)
    status = "OK" if value >= minimum else "FALLO"
    print(f"[{status}] {name}: {value:.2f}:1 (mínimo {minimum:.1f}:1)")
    if value < minimum:
        errors.append(f"{name}: {value:.2f}:1")

if errors:
    raise SystemExit("ERROR CONTRASTE:\n- " + "\n- ".join(errors))
print("OK contraste: combinaciones críticas de la paleta superan 4.5:1.")
