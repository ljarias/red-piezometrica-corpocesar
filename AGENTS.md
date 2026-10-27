# Instrucciones para Codex · V1.0 (2026-10-27)

## Reglas transversales
- Trabajar en español. Antes de actuar: comprobar la rama, cambios sin confirmar, README, documentación de continuidad, decisiones, PR y pruebas disponibles.
- Respetar el trabajo existente y el alcance de la tarea. No reinicializar instalaciones, repetir migraciones ni mezclar aplicaciones o entornos distintos.
- Mantener separadas las categorías PROPUESTO, IMPLEMENTADO, PROBADO, VALIDADO, DESPLEGADO y BLOQUEADO. No inventar ejecuciones, validaciones, accesos ni aprobación humana.
- En auditorías, no modificar nada salvo autorización; para una implementación autorizada, preferir cambios reversibles y mínimos. Cambios de datos reales, permisos, secretos, gasto, CI productiva o despliegue requieren autorización específica.
- Revisar sintaxis, compatibilidad, dependencias, entradas, errores y seguridad; ejecutar pruebas pertinentes cuando sea posible, o explicar por qué no.
- No publicar credenciales, tokens, información personal de alumnos, clientes o familiares ni datos productivos en trazas, documentación o pruebas.
- Entregar un cierre con archivos afectados, evidencias (incluidos hashes/PR cuando correspondan), pruebas realmente ejecutadas, limitaciones y siguiente paso.
- Verificar existencia, integridad y ruta de cualquier archivo descargable antes de enlazarlo; no afirmar haber probado una descarga desde navegador sin haberlo hecho.

## Red Piezométrica CORPOCESAR V4
- Dashboard estático GitHub Pages; `index.html`, `assets/`, `data/generated/`, scripts Python, tests y `.github/workflows/deploy-pages.yml`.
- Leer `docs/SAD.md`, `docs/PLAN_PENDIENTES_V4.md`, `docs/INFORME_CIERRE_AUDITORIA_V4.md`, `docs/EVALUACION_P08_SEGURIDAD.md` y `SECURITY.md` antes de intervenir hallazgos; confrontar con código y CI actuales.
- Mantener `data/source/` con Excel institucional fuera de Git; nunca subir datos fuente no destinados al público.
- No publicar JSON nuevos sin validar columnas, tipos, registros, unidades, timestamps y reglas de calidad de datos; no atribuir a sensores o compensación RAW reglas que no estén documentadas.
- Revisar `requirements.txt`, `scripts/`, `tests/` y workflows antes de ejecutar transformación. Proteger histórico y aviso de licencias.
- Hacer distinción estricta entre control implementado, prueba automatizada, aprobación institucional y publicación. Un merge en `main` puede disparar GitHub Pages.
