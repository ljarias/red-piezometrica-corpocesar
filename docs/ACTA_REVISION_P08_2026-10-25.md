# Acta de revisión y recomendación de cierre técnico P08

**Proyecto:** Red Piezométrica CORPOCESAR V4  
**Hallazgo:** P08 — Revisar dependencias externas y GitHub Actions por SHA  
**Fecha de corte:** 2026-10-25  
**Estado propuesto:** **LISTO PARA CIERRE TÉCNICO CONDICIONADO**  
**Estado de aprobación:** **PENDIENTE DE ACEPTACIÓN EXPRESA DE RIESGOS**  
**Responsable de decisión:** responsable técnico del proyecto, quien manifestó asumir esta función. Este registro no presume representación jurídica de CORPOCESAR.

## 1. Decisión respaldada por evidencias

La implementación de los controles preventivos y detectivos de P08 queda técnicamente acreditada. No se identificaron fallos en la última ejecución CI/CD de la rama principal. La declaración de *cierre formal* exige la aceptación de las condiciones de la sección 3.

| Evidencia | Resultado | Enlace |
|---|---|---|
| Conciliación documental del plan y del informe V4 | PR #1 fusionado, commit `532acff6` | [PR #1](https://github.com/ljarias/red-piezometrica-corpocesar/pull/1) |
| Remediación de popup de Leaflet, CSP/OSM, SBOM, licencias y CI | PR #2 fusionado, commit `ab86451c` | [PR #2](https://github.com/ljarias/red-piezometrica-corpocesar/pull/2) |
| 8 recursos y sus SHA-384, pruebas de regresión, seguridad y privacidad | 16 pruebas Python + 1 prueba Node; desplegado `SUCCESS` | [Pages #92](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40197934789) |
| Actualización de Actions a runtime Node 24 y SHA de upstream | PR #3 fusionado, commit `03562dae` | [PR #3](https://github.com/ljarias/red-piezometrica-corpocesar/pull/3) |
| Verificación final en rama principal | `SUCCESS`: SHA-384, 16 pruebas Python, 1 Node, `Reported success!`; aviso Node 20 ausente | [Pages #93](https://github.com/ljarias/red-piezometrica-corpocesar/actions/runs/40198385482) |
| SBOM directo, licencias MIT/BSD y evaluación de avisos | Inventario y documentación presentes, **sin certificar completitud transitiva** | [SBOM](SBOM_P08.json), [Evaluación](EVALUACION_P08_SEGURIDAD.md) |

**Alcance de comprobación:** lectura del código en GitHub, ejecución automatizada en GitHub Actions, bitácora del despliegue y fuentes de terceros consultadas. **No se ejecutó una revisión visual manual** del portal publicado ni se descargó el artefacto binario para cotejo de sus bytes.

## 2. Hallazgo solucionado

Los popups de Leaflet ya no incrustan datos de predio, estación, cuenca o acuífero como HTML no confiable. El contenido se construye mediante `document.createElement`, `textContent` y `createTextNode`. Se añadió un caso de prueba funcional con contenido de prueba que contiene una etiqueta HTML y un manejador de eventos; debe permanecer como texto, sin convertirse en elemento ejecutable. El cambio atiende el escenario señalado por [CVE-2025-69993](https://github.com/advisories/GHSA-h5cx-hfj5-x8v3); se conserva el registro del aviso, que [los mantenedores disputan](https://github.com/Leaflet/Leaflet/issues/10214).

Las dependencias frontend siguen fijadas a versiones explícitas y verificadas por SHA-384. Las Actions directas del pipeline están fijadas por SHA completo, al igual que la dependencia interna de subida usada por el action v5 inspeccionado. Un workflow de PR revisa cambios antes de permitir publicación y el workflow de Pages vuelve a ejecutar los controles.

## 3. Riesgos que requieren decisión del responsable

| Riesgo residual | Estado | Decisión propuesta |
|---|---|---|
| Leaflet 1.9.4 y aviso CVE-2025-69993 | Uso inseguro mitigado en la aplicación; el aviso externo permanece | Aceptar el riesgo residual con vigilancia de nuevas llamadas a popup y monitoreo de avisos |
| Proveedores externos de mapas y logos | Los servicios pueden cambiar condiciones o disponibilidad; términos ajenos a software propio | Aceptar solo para el alcance técnico actual. Clasificación de documentos/datos sigue en P01 y licencias públicas en P07 |
| pandas/openpyxl del ETL local | Directas fijadas; no se verificaron hashes de distribuciones ni árbol transitivo instalado | Registrar evaluación posterior del entorno ETL con `pip-audit` y lock con hashes; no incluir ETL dentro de la conclusión de seguridad de Pages |
| Node / Actions | Aviso Node 20 eliminado; queda deprecación menor `[DEP0040] punycode` originada en un paquete del proveedor de Actions | Aceptar como advertencia no bloqueante, vigilar nuevas versiones oficiales y no modificar SHA sin nuevas pruebas |
| Comprobación visual y artefacto final | Log `Reported success!` sin inspección manual ni verificación binaria posterior | Realizar revisión visual operativa antes de autorización institucional definitiva; no presentarla como hecha |

La aceptación de estas condiciones **no equivale a autorizar la divulgación de datos**, ni a certificar WCAG, ni a cerrar P01, P02, P03, P06, P07, P09, P10 o P12.

## 4. Registro de decisión

**Resultado recomendado por revisión técnica:** apto para cierre técnico **condicionado** de P08.

- [ ] Acepto los riesgos residuales delimitados en la sección 3 y autorizo marcar **P08 cerrado técnicamente**, con compromisos de seguimiento.
- [ ] No acepto todavía los riesgos; P08 permanece pendiente con observaciones.
- [ ] Requiero evaluación adicional antes de decidir.

**Responsable que aprueba:** ______________________________  
**Rol/cargo:** ______________________________  
**Fecha de decisión:** ______________________________  
**Enlace o número de evidencia de aprobación:** ______________________________  
**Observaciones y responsables del seguimiento:** ______________________________

> **Regla de cierre:** hasta diligenciar este registro o dejar aprobación equivalente verificable en el PR/issue institucional, el estado del plan permanecerá `LISTO PARA CIERRE TÉCNICO CONDICIONADO`, no `CERRADO`.
