#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
SOURCE="data/source/BaseDatos_red_piezometrica_SAC.xlsx"
if [[ ! -f "$SOURCE" ]]; then
  echo "[ERROR] No se encontró $SOURCE"
  exit 1
fi
python3 -m pip install -r requirements.txt
python3 scripts/process_excel.py
echo "[OK] JSON regenerados en data/generated/"
echo 'Revise el dashboard y luego: git add data/generated && git commit -m "Actualizar datos" && git push'
