# Manual técnico

## Requisitos
Windows con Python, Git y acceso al repositorio. Dependencias Python definidas en requirements.txt.

## Estructura principal
- assets/: frontend.
- data/source/: Excel privado, ignorado por Git.
- data/generated/: JSON públicos.
- scripts/: ETL y validadores.
- tests/: pruebas automatizadas.
- .github/workflows/: CI/CD.

## Actualización
1. Reemplazar data/source/BaseDatos_red_piezometrica_SAC.xlsx.
2. Ejecutar actualizar_datos.bat.
3. Revisar data/generated/update_report.json.
4. Ejecutar run_local.bat y validar visualmente.
5. Publicar solo si no existen bloqueos:
   git add data/generated scripts
   git commit -m "Actualizar datos red piezometrica - AAAA-MM-DD"
   git push
6. Confirmar que GitHub Actions finalice con success.

## Estados del control
- APTO_PARA_PUBLICAR: sin incidencias detectadas.
- REQUIERE_REVISION: existen advertencias que requieren revisión humana.
- BLOQUEADO: no publicar hasta corregir o autorizar formalmente el cambio.

## Seguridad
Nunca agregar el Excel fuente, tokens, contraseñas o datos personales no autorizados. La lista blanca de process_excel.py determina qué columnas pueden salir al artefacto público.

## Pruebas
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_frontend.py
python scripts/validate_public_data.py

## Rollback
Revertir el commit defectuoso mediante Git, hacer push y verificar que el pipeline despliegue nuevamente la versión estable.
