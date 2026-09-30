#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
SOURCE="data/source/BaseDatos_red_piezometrica_SAC.xlsx"
if [[ ! -f "$SOURCE" ]]; then
  echo "[ERROR] No se encontró $SOURCE"
  exit 1
fi
python3 -m pip install -r requirements.txt
echo "[1/4] Capturando línea base..."
python3 scripts/validate_update.py --snapshot
echo "[2/4] Procesando Excel..."
python3 scripts/process_excel.py
echo "[3/4] Validando privacidad..."
python3 scripts/validate_public_data.py
echo "[4/4] Comparando actualización..."
python3 scripts/validate_update.py
echo "[OK] Controles automáticos completados."
echo "Revise data/generated/update_report.json y pruebe el dashboard."
echo "CONTROLES_AUTOMATICOS_OK no equivale a aprobación científica, jurídica ni autorización institucional de publicación."
