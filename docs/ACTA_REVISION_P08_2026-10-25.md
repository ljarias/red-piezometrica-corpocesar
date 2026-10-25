# Acta de aprobación y cierre técnico P08

**Proyecto:** Red Piezométrica CORPOCESAR V4  
**Hallazgo:** P08 — Revisar dependencias externas y GitHub Actions por SHA  
**Fecha de corte:** 2026-10-25  
**Estado aprobado:** **CERRADO TÉCNICAMENTE CON RIESGOS RESIDUALES ACEPTADOS PARA SEGUIMIENTO**  
**Estado de aprobación:** **APROBADO POR EL RESPONSABLE TÉCNICO EL 2026-10-25**  
**Responsable de decisión:** responsable técnico del proyecto, quien manifestó asumir esta función. Este registro no presume representación jurídica de CORPOCESAR.

## 1. Decisión respaldada por evidencias

La implementación de los controles preventivos y detectivos de P08 quedó técnicamente acreditada. El responsable del proyecto aprobó explícitamente en conversación el 2026-10-25 el **cierre de P08**, después de recibir el detalle de sus riesgos residuales. Se registra la aprobación como decisión de **cierre técnico condicionado al seguimiento**, sin afirmar que exista firma digital independiente ni aprobación institucional de CORPOCESAR.

| Evidencia | Resultado | Enlace |
|---|---|---|
| Conciliación documental del plan y del informe V4 | PR #1 fusionado, commit `532acff6` | [PR #1](https://github.com/ljarias/red-piezometrica-corpocesar/pull/1) |
| Remediación de popup de Leaflet, CSP/OSM, SBOM, licencias y CI | PR #2 fusionado, commit `ab86451c` | [PR #2](https://github.com/ljarias/red-piezometrica-corpocesar/pull/2) |
| 8 recursos y sus SHA-384, pruebas de regresión, seguridad y privacidad | 16 pruebas Python + 1 prueba Node; desplegado `SUCCESS` | [Pages #92](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40197934789) |
| Actualización de Actions a runtime Node 24 y SHA de upstream | PR #3 fusionado, commit `03562dae` | [PR #3](https://github.com/ljarias/red-piezometrica-corpocesar/pull/3) |
| Verificación de remediación en rama principal | `SUCCESS`: SHA-384, 16 pruebas Python, 1 Node, `Reported success!`; aviso Node 20 ausente | [Pages #93](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40198385482) |
| Última ejecución confirmada antes del cierre | Commit `c1243cfb91d9a20a9ebe142aad00dcb6faa00e67` · `SUCCESS`; 16 pruebas Python, 1 Node, 8 hashes correctos, despliegue reportado exitoso | [Pages #94](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40198758354) |
| SBOM directo, licencias MIT/BSD y evaluación de avisos | Inventario y documentación presentes, **sin certificar completitud transitiva** | [SBOM](SBOM_P08.json), [Evaluación](EVALUACION_P08_SEGURIDAD.md) |

**Alcance de comprobación:** lectura del código en GitHub, ejecución automatizada en GitHub Actions, bitácora del despliegue y fuentes de terceros consultadas. **No se ejecutó una revisión visual manual** del portal publicado ni se descargó el artefacto binario para cotejo de sus bytes.

## 2. Hallazgo solucionado

Los popups de Leaflet ya no incrustan datos de predio, estación, cuenca o acuífero como HTML no confiable. El contenido se construye mediante `document.createElement`, `textContent` y `createTextNode`. Se añadió un caso de prueba funcional con contenido de prueba que contiene una etiqueta HTML y un manejador de eventos; debe permanecer como texto, sin convertirse en elemento ejecutable. El cambio atiende el escenario señalado por [CVE-2025-69993](https://github.com/advisories/GHSA-h5cx-hfj5-x8v3); se conserva el registro del aviso, que [los mantenedores disputan](https://github.com/Leaflet/Leaflet/issues/10214).

Las dependencias frontend siguen fijadas a versiones explícitas y verificadas por SHA-384. Las Actions directas del pipeline están fijadas por SHA completo, al igual que la dependencia interna de subida usada por el action v5 inspeccionado. Un workflow de PR revisa cambios antes de permitir publicación y el workflow de Pages vuelve a ejecutar los controles.

## 3. Riesgos residuales aceptados para seguimiento

| Riesgo residual | Estado | Aceptación y seguimiento |
|---|---|---|
| Leaflet 1.9.4 y aviso CVE-2025-69993 | Uso inseguro mitigado en la aplicación; el aviso externo permanece | Aceptar el riesgo residual con vigilancia de nuevas llamadas a popup y monitoreo de avisos |
| Proveedores externos de mapas y logos | Los servicios pueden cambiar condiciones o disponibilidad; términos ajenos a software propio | Aceptar solo para el alcance técnico actual. Clasificación de documentos/datos sigue en P01 y licencias públicas en P07 |
| pandas/openpyxl del ETL local | Directas fijadas; no se verificaron hashes de distribuciones ni árbol transitivo instalado | Registrar evaluación posterior del entorno ETL con `pip-audit` y lock con hashes; no incluir ETL dentro de la conclusión de seguridad de Pages |
| Node / Actions | Aviso Node 20 eliminado; queda deprecación menor `[DEP0040] punycode` originada en un paquete del proveedor de Actions | Aceptar como advertencia no bloqueante, vigilar nuevas versiones oficiales y no modificar SHA sin nuevas pruebas |
| Comprobación visual y artefacto final | Log `Reported success!` sin inspección manual ni verificación binaria posterior | Realizar revisión visual operativa antes de autorización institucional definitiva; no presentarla como hecha |

**Alcance de aceptación:** el responsable acepta estos riesgos para el cierre técnico de P08, sin dar por realizados controles todavía pendientes. La evaluación del ETL y de los servicios externos continúa como actividad de seguimiento; el aviso `punycode` se registra como no bloqueante. La aceptación **no equivale a autorizar la divulgación de datos**, certificar WCAG o cerrar P01, P02, P03, P06, P07, P09, P10 o P12.

## 4. Registro de aprobación del responsable

- [x] **APROBADO:** acepto para el alcance técnico de P08 los riesgos residuales de la sección 3 y autorizo marcar P08 como **cerrado técnicamente**, con compromisos de seguimiento.
- [ ] No aprobado.
- [ ] Requiere evaluación adicional antes del cierre técnico.

**Persona que toma la decisión:** responsable técnico del proyecto, según su manifestación expresa en la conversación.  
**Rol:** responsable del proyecto.  
**Fecha de la aprobación comunicada:** **2026-10-25** (zona horaria Colombia).  
**Evidencia de aprobación:** instrucción expresa del responsable en la conversación de ChatGPT: «Aprobamos el cierre de p08». La conversación es la fuente de autorización; el registro en GitHub es la evidencia documental de su ejecución. No se aporta firma digital ni identidad institucional adicional.  
**Tipo de decisión:** cierre **técnico** y aceptación delimitada de riesgos residuales; no autoriza la liberación institucional V4.

## 5. Seguimiento posterior al cierre técnico

| Tarea | Responsable de seguimiento | Oportunidad de control |
|---|---|---|
| Vigilar avisos de seguridad de Leaflet, Chart.js y Actions; preservar protección DOM en nuevos popups | Responsable técnico o delegado de seguridad | En cada cambio de dependencia y revisión periódica de seguridad |
| Revisar términos, atribuciones y continuidad de teselas Esri, OpenTopoMap y OSM | Responsable técnico y responsable institucional de publicación | Antes de una liberación institucional definitiva y ante cambios de proveedores |
| Auditar entorno ETL local con `pip-audit`, obtener dependencias transitivas y lock reproducible cuando se automatice | Responsable de operación de datos / desarrollo | Antes del siguiente cambio operativo relevante de ETL |
| Vigilar advertencia `[DEP0040] punycode` y futuras versiones oficiales Node 24 | Responsable técnico | En cada actualización de Actions |
| Realizar prueba visual del portal y verificar publicación institucional de datos, cuando proceda | Responsable de publicación designado | Antes de cada liberación institucional |

**Decisión final:** **P08 CERRADO TÉCNICAMENTE CON SEGUIMIENTO** desde la aprobación expresa del 2026-10-25. Los demás hallazgos y autorizaciones mantienen su estado independiente. Esta acta no constituye certificación de ausencia de vulnerabilidades.
