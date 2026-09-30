# Registro de publicación — Red Piezométrica CORPOCESAR

Este documento define el control mínimo de cada liberación pública. Debe diligenciarse al aprobar una nueva campaña o un cambio funcional significativo.

## Registro

| Versión | Fecha | Fuente | Periodo de datos | Registros | Piezómetros | Commit | Resultado CI | Responsable de revisión | Observaciones |
|---|---|---|---|---:|---:|---|---|---|---|
| V4 / ETL 3.3 | 2026-09-30 | BaseDatos_red_piezometrica_SAC.xlsx | 2024-09-25 a 2025-03-26 | 7193 | 23 | 8412f76 (datos) / 4706d1e (corrección CI) | SUCCESS · run 36715664963 | Pendiente designación CORPOCESAR | update_report: APTO_PARA_PUBLICAR; 22 piezómetros con datos; SA-06A condición histórica sin datos |

## Evidencias mínimas por liberación

- `meta.json` con hash SHA-256 de la fuente cuando sea regenerado con ETL V3.3+.
- `update_report.json` para actualizaciones de datos.
- ejecución CI/CD satisfactoria;
- revisión visual local;
- decisión sobre advertencias;
- commit identificable;
- aprobación del responsable designado.

## Regla de publicación

Un resultado `BLOQUEADO` no debe publicarse. Un resultado `REQUIERE_REVISION` exige decisión humana documentada. `APTO_PARA_PUBLICAR` indica que los controles automáticos no encontraron las incidencias configuradas, pero no sustituye la revisión institucional.
