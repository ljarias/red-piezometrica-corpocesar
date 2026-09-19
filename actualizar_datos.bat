@echo off
setlocal
cd /d "%~dp0"
echo ==============================================
echo  Red Piezometrica - Actualizacion de datos
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
echo Procesando Excel...
python scripts\process_excel.py
if errorlevel 1 goto :error
echo.
echo [OK] JSON regenerados en data\generated\
echo Ahora revise el dashboard con run_local.bat y, si todo esta correcto,
echo ejecute: git add data/generated ^&^& git commit -m "Actualizar datos" ^&^& git push
pause
exit /b 0
:error
echo.
echo [ERROR] La actualizacion no pudo completarse. No publique hasta corregirla.
pause
exit /b 1
