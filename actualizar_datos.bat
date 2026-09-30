@echo off
setlocal
cd /d "%~dp0"
echo ==============================================
echo  Red Piezometrica - Actualizacion segura V3.3
echo ==============================================
if not exist "data\source\BaseDatos_red_piezometrica_SAC.xlsx" (
  echo [ERROR] No se encontro data\source\BaseDatos_red_piezometrica_SAC.xlsx
  pause
  exit /b 1
)
python -c "import pandas, openpyxl" >nul 2>&1
if errorlevel 1 (
  echo Instalando dependencias...
  python -m pip install -r requirements.txt
  if errorlevel 1 goto :error
)

echo.
echo [1/4] Capturando linea base publicada...
python scripts\validate_update.py --snapshot
if errorlevel 1 goto :error

echo [2/4] Procesando nuevo Excel...
python scripts\process_excel.py
if errorlevel 1 goto :error

echo [3/4] Validando privacidad del dataset publico...
python scripts\validate_public_data.py
if errorlevel 1 goto :error

echo [4/4] Comparando contra la version anterior...
python scripts\validate_update.py
if errorlevel 1 goto :blocked

echo.
echo [OK] Actualizacion procesada y controles bloqueantes superados.
echo Revise data\generated\update_report.json y pruebe el dashboard con run_local.bat.
echo Si el informe indica CONTROLES_AUTOMATICOS_OK, aun requiere revision y autorizacion institucional antes de publicar.\necho Si indica REQUIERE_REVISION, revise ademas las advertencias.
echo.
echo Para publicar, despues de la revision:
echo   git add data/generated scripts
echo   git commit -m "Actualizar datos red piezometrica"
echo   git push
pause
exit /b 0

:blocked
echo.
echo [BLOQUEADO] Se detectaron cambios que requieren correccion o autorizacion.
echo NO publique esta version. Revise data\generated\update_report.json
pause
exit /b 2

:error
echo.
echo [ERROR] La actualizacion no pudo completarse. No publique hasta corregirla.
pause
exit /b 1
