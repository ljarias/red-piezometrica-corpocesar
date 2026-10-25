# Plan de pendientes y cierre institucional V4

| ID | Acción | Responsable sugerido | Prioridad | Bloquea cierre si está pendiente | Estado y evidencia |
|---|---|---|---|---|---|
| P01 | Aprobar clasificación de coordenadas, predio, seriales y documentos | Jurídica + Seguridad + responsable de información | Crítica | Sí | Pendiente de aprobación institucional |
| P02 | Validar fórmula de nivel absoluto | Hidrogeología | Crítica | Sí | Pendiente de validación científica |
| P03 | Definir rangos de plausibilidad por variable | Hidrogeología / calidad de datos | Alta | Sí | Pendiente de definición científica |
| P04 | Ejecutar auditoría WCAG 2.1 AA integral | Desarrollo + accesibilidad | Alta | Sí | **Cerrado técnicamente 2026-09-30 · teclado, reflow, contraste y NVDA validados** |
| P05 | Incorporar equivalente tabular/textual completo para gráficas | Desarrollo | Alta | Sí | **Cerrado técnicamente V4** |
| P06 | Designar responsable de publicación y aprobación | CORPOCESAR | Alta | Sí | Pendiente de designación institucional |
| P07 | Definir licencia y condiciones de reutilización | Jurídica / datos abiertos | Alta | Sí para apertura formal | Pendiente de definición jurídica |
| P08 | Revisar dependencias externas y Actions por SHA | Desarrollo / seguridad | Media | No | **LISTO PARA CIERRE TÉCNICO CONDICIONADO · PR #2 y #3 integrados · CI/Pages #93 SUCCESS · aceptación de riesgos residuales pendiente** |
| P09 | Definir procedimiento de incidentes y continuidad | Seguridad TI | Alta | Sí | **Procedimiento técnico creado; falta asignar responsables institucionales** |
| P10 | Aprobar SAD, manual técnico, manual de usuario y matrices | Responsable institucional | Alta | Sí | Pendiente de aprobación institucional |
| P11 | Regenerar dataset con ETL V3.3+ para incorporar hash de fuente | Operación de datos | Alta | Sí | **Cerrado 2026-09-30 · CI SUCCESS** |
| P12 | Completar registro de primera liberación institucional | Responsable publicación | Alta | Sí | **Registro técnico creado; falta responsable institucional** |

**Lectura de la matriz:** «Bloquea cierre si está pendiente» expresa la condición del hallazgo no resuelto, no su estado actual. «Estado y evidencia» registra la situación conocida; las pruebas técnicas no sustituyen la aprobación institucional. Las fechas anteriores son referencias históricas, no nuevas pruebas ejecutadas el 25/10/2026.

## Seguimiento y evidencia de P08 (revisión documental del 2026-10-25)

**Estado diferenciado:** los controles de integridad de las dependencias frontend y de fijación de GitHub Actions están **implementados y ejecutados satisfactoriamente**. El hallazgo P08 **no se declara cerrado integralmente ni aprobado institucionalmente**, porque la evidencia disponible no cubre toda la revisión de la cadena de suministro. Su condición de **no bloqueante** en este plan se mantiene; no se confunde con una autorización de publicación.

**Implementación comprobada en la referencia `main@70f468dfd4d93c301d34bc1039c8ea511ad34ae6`:**

- [Workflow de Pages](../.github/workflows/deploy-pages.yml): cuatro acciones directas fijadas a SHA completos y validación previa al despliegue.
- [Script de dependencias](../scripts/vendor_frontend.py): descarga de ocho recursos Chart.js 4.4.7 y Leaflet 1.9.4, verificados individualmente con SHA-384; una discrepancia interrumpe el proceso.
- [Frontend](../index.html): carga las bibliotecas desde `assets/vendor/`; [validador](../scripts/validate_frontend.py) comprueba las rutas locales y bloquea referencias CDN de ejecución específicas.

**Ejecuciones existentes examinadas, no reproducidas en esta revisión:**

- [GitHub Actions #90](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/36722048949), commit `70f468d`: `SUCCESS` (2026-09-30). El [job](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/36722048949/job/109909367616) registra los ocho recursos `[OK]`, verificaciones de CI y publicación.
- [GitHub Actions #61](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/36717957874): `FAILURE` al detectar SHA-384 incorrecto de `layers-2x.png`; prueba histórica del bloqueo. No representa un defecto persistente de la referencia actual.

**Pendiente de acreditar:** inventario/SBOM y análisis de vulnerabilidades de dependencias directas y transitivas, revisión independiente de licencias y procedencia, seguimiento de proveedores externos de mapas e imágenes, revisión de la advertencia de migración Node.js 20/24 observada en #90 y aceptación formal del responsable competente. La carga de bibliotecas se verifica **durante el build** desde proveedores remotos; las teselas cartográficas siguen dependiendo de servicios externos. El log confirma la carga del artefacto, pero en esta auditoría no se descargó ni cotejó binariamente el artefacto final.

**Criterio de próxima decisión:** registrar responsable, fecha, comprobaciones de seguridad de dependencias y riesgos aceptados antes de cambiar P08 a «cerrado integralmente». La expresión «cerrado técnicamente» del informe V4 se limita a los controles criptográficos y de ejecución descritos, no a una aprobación integral de cadena de suministro.

## Orden recomendado

**Hito A — Decisiones institucionales:** P01, P06, P07 y P09.  
**Hito B — Validación científica:** P02 y P03.  
**Hito C — Evidencia técnica:** P04, P05, P08 y P11.  
**Hito D — Aprobación:** P10 y P12.

El cierre se produce únicamente cuando los elementos marcados como bloqueantes tengan evidencia verificable y responsable identificado.

## Avance correctivo de P08 — 2026-10-25

La conciliación documental [PR #1](https://github.com/ljarias/red-piezometrica-corpocesar/pull/1) quedó integrada (`532acff6`). El correctivo [PR #2](https://github.com/ljarias/red-piezometrica-corpocesar/pull/2) quedó integrado (`ab86451c`) tras pruebas de seguridad y [Pages #92 SUCCESS](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40197934789). Se corrigió el popup de Leaflet que interpolaba datos como HTML, se añadió SBOM parcial, licencias completas y guardas CI, y se ajustó OpenStreetMap al endpoint oficial. La revisión de advertencias Node 20→24 se resolvió mediante [PR #3](https://github.com/ljarias/red-piezometrica-corpocesar/pull/3), integrado en `03562dae`; el [despliegue #93](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40198385482) finalizó en SUCCESS con 16 pruebas Python, una prueba Node y sin el aviso anterior de Actions Node 20. El aviso menor `[DEP0040] punycode` no impidió publicar. La [recomendación de cierre y aceptación residual](ACTA_REVISION_P08_2026-10-25.md) sigue sin firma.

**No marcar P08 como cerrado integralmente hasta registrar la aceptación expresa de los riesgos residuales (teselas externas, ETL Python y vulnerabilidades futuras).** Su condición de no bloqueante para el cierre institucional V4 no equivale a validar P01/P07 ni a autorizar publicación de datos.
