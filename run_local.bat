@echo off
echo Preparando dependencias frontend verificadas...
python scripts\vendor_frontend.py
if errorlevel 1 (
  echo [ERROR] No fue posible preparar las dependencias frontend.
  pause
  exit /b 1
)
start http://localhost:8000
python -m http.server 8000
