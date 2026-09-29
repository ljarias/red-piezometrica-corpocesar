"""Valida una actualización generada contra la versión publicada anterior.

Debe ejecutarse después de process_excel.py. La línea base se captura antes de
regenerar los JSON mediante --snapshot. No modifica datos; genera un informe y
devuelve código distinto de cero únicamente ante condiciones bloqueantes.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "data" / "generated"
BASELINE = ROOT / "data" / ".update_baseline.json"
REPORT = GEN / "update_report.json"


def load(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def snapshot() -> int:
    meta = load(GEN / "meta.json", {})
    master = load(GEN / "master.json", [])
    quality = load(GEN / "quality.json", [])
    baseline = {
        "meta": meta,
        "piezometros": sorted({r.get("piezometro") for r in master if r.get("piezometro")}),
        "quality": {r.get("piezometro"): r for r in quality if r.get("piezometro")},
    }
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE.write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Linea base capturada: {meta.get('registros', 0)} lecturas.")
    return 0


def validate() -> int:
    old = load(BASELINE, {})
    new_meta = load(GEN / "meta.json", {})
    new_master = load(GEN / "master.json", [])
    new_quality = load(GEN / "quality.json", [])

    if not old:
        print("[ERROR] No existe linea base. Ejecute --snapshot antes de regenerar.")
        return 2

    old_meta = old.get("meta", {})
    old_ids = set(old.get("piezometros", []))
    new_ids = {r.get("piezometro") for r in new_master if r.get("piezometro")}
    old_count = int(old_meta.get("registros") or 0)
    new_count = int(new_meta.get("registros") or 0)
    old_max = old_meta.get("fecha_max")
    new_max = new_meta.get("fecha_max")

    blockers = []
    warnings = []

    if new_count < old_count:
        blockers.append(f"Las lecturas disminuyeron de {old_count} a {new_count}.")
    if old_max and new_max and new_max < old_max:
        blockers.append(f"La fecha maxima retrocedio de {old_max} a {new_max}.")
    removed = sorted(old_ids - new_ids)
    added = sorted(new_ids - old_ids)
    if removed:
        blockers.append("Piezometros eliminados del maestro: " + ", ".join(removed))
    if added:
        warnings.append("Piezometros nuevos: " + ", ".join(added))

    duplicates = sum(int(q.get("duplicados") or 0) for q in new_quality)
    nulls = sum(int(q.get("nulos") or 0) for q in new_quality)
    no_data = sorted(q.get("piezometro") for q in new_quality if q.get("estado") == "sin_datos")
    critical = sorted(q.get("piezometro") for q in new_quality if q.get("estado") == "critico")
    if duplicates:
        warnings.append(f"Se detectaron {duplicates} filas duplicadas.")
    if nulls:
        warnings.append(f"Se detectaron {nulls} valores nulos en variables de medicion.")
    if no_data:
        warnings.append("Piezometros sin datos: " + ", ".join(no_data))
    if critical:
        warnings.append("Piezometros con calidad critica: " + ", ".join(critical))

    status = "BLOQUEADO" if blockers else ("REQUIERE_REVISION" if warnings else "APTO_PARA_PUBLICAR")
    report = {
        "fecha_control": date.today().isoformat(),
        "estado": status,
        "anterior": {
            "registros": old_count,
            "piezometros": len(old_ids),
            "fecha_min": old_meta.get("fecha_min"),
            "fecha_max": old_max,
        },
        "nuevo": {
            "registros": new_count,
            "piezometros": len(new_ids),
            "fecha_min": new_meta.get("fecha_min"),
            "fecha_max": new_max,
        },
        "diferencias": {
            "lecturas": new_count - old_count,
            "piezometros_nuevos": added,
            "piezometros_eliminados": removed,
            "duplicados": duplicates,
            "nulos": nulls,
        },
        "bloqueos": blockers,
        "advertencias": warnings,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n==============================================")
    print(" CONTROL DE ACTUALIZACION - RED PIEZOMETRICA")
    print("==============================================")
    print(f"Lecturas:       {old_count} -> {new_count} ({new_count-old_count:+d})")
    print(f"Piezometros:    {len(old_ids)} -> {len(new_ids)}")
    print(f"Fecha maxima:   {old_max or '-'} -> {new_max or '-'}")
    print(f"Nuevos:         {len(added)}")
    print(f"Eliminados:     {len(removed)}")
    print(f"Duplicados:     {duplicates}")
    print(f"Nulos:          {nulls}")
    print("----------------------------------------------")
    print("RESULTADO:", status)
    for msg in blockers:
        print("[BLOQUEO]", msg)
    for msg in warnings:
        print("[REVISAR]", msg)
    print("Informe:", REPORT.relative_to(ROOT))
    print("==============================================\n")
    return 1 if blockers else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", action="store_true")
    args = parser.parse_args()
    raise SystemExit(snapshot() if args.snapshot else validate())
