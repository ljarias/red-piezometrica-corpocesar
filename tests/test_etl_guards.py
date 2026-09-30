"""Regresión estática de precondiciones defensivas del ETL."""
from pathlib import Path

APP=(Path(__file__).resolve().parents[1]/"scripts/process_excel.py").read_text(encoding="utf-8")
REQUIRED=[
    "if master.empty:",
    "if read.empty:",
    "master['piezometro'].duplicated().any()",
    "orphans=sorted(read_ids-master_ids)",
    "if orphans:",
    "'etl_version':'3.3.1'",
]
missing=[x for x in REQUIRED if x not in APP]
for x in REQUIRED:
    print(f"[{'OK' if x in APP else 'FALLO'}] {x}")
if missing:
    raise SystemExit("Faltan guardas defensivas ETL: "+", ".join(missing))
print("OK ETL defensivo: precondiciones críticas presentes.")
