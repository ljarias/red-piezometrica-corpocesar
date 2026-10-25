# Evaluación de seguridad P08 — Red Piezométrica CORPOCESAR V4

**Fecha de análisis:** 2026-10-25  
**Alcance:** dependencias Chart.js y Leaflet, ocho archivos frontend, cuatro Actions del flujo de Pages, ETL Python declarado, servicios de terceros y mitigaciones de seguridad.  
**Referencias:** cambios de la rama `security/p08-popup-supply-chain-20261025` y [conciliación documental V4](INFORME_CIERRE_AUDITORIA_V4.md). Esta evaluación es técnica, **no constituye autorización institucional de publicación ni certificación externa**.

## 1. Inventario y dependencia de proveedores

| Recurso | Versión o endpoint | Función y tratamiento | Evidencia / obligación |
|---|---|---|---|
| Chart.js | 4.4.7 | Script local compilado desde jsDelivr en cada build, SHA-384 fijo | MIT, [licencia íntegra](../licenses/Chart.js-4.4.7-MIT.txt), archivo en [SBOM](SBOM_P08.json) |
| Leaflet | 1.9.4 | JS, CSS y cinco imágenes locales, comprobados con SHA-384 | BSD-2-Clause, [licencia íntegra](../licenses/Leaflet-1.9.4-BSD-2-Clause.txt); incidencia de popups abordada |
| Actions de GitHub Pages | checkout v6; configure-pages v5; upload-pages-artifact v4; deploy-pages v4 | Cuatro dependencias directas fijadas a SHA completo | [workflow de despliegue](../.github/workflows/deploy-pages.yml), privilegios mínimos por job |
| pandas / openpyxl | 2.2.3 / 3.1.5 | Dependencias de ETL local, **no instaladas por el flujo Pages** | `requirements.txt`, sin hashes de wheels ni transitivas bloqueadas; revisión local pendiente |
| OpenStreetMap | `https://tile.openstreetmap.org/{z}/{x}/{y}.png` | Teselas solicitadas por navegador | atribución, referer y caché ordinaria; [política del proveedor](https://operations.osmfoundation.org/policies/tiles/) |
| Esri, OpenTopoMap | Endpoints HTTPS de teselas | Disponibilidad y condiciones dependientes de terceros | Mostrar atribución; validar autorización/condiciones de uso antes de liberación institucional |
| NaturalSIG | `naturalsig.org` | Logo, fichas, imágenes y documentos | Proveedor tercero y decisión de clasificación de información (P01) |

El [SBOM CycloneDX 1.5](SBOM_P08.json) cubre **cuatro dependencias directas y ocho artefactos**; es un inventario parcial y **no demuestra** que toda dependencia transitiva, paquete instalado o proveedor externo haya sido evaluado.

## 2. Vulnerabilidades consultadas y tratamiento

### Leaflet 1.9.4: aviso CVE-2025-69993 (severidad media reportada)

- [GitHub Advisory GHSA-h5cx-hfj5-x8v3](https://github.com/advisories/GHSA-h5cx-hfj5-x8v3), publicado 2026-04-14: advierte que pasar HTML no confiable a `bindPopup()` puede causar XSS.
- [Posición de mantenedores Leaflet, issue #10214](https://github.com/Leaflet/Leaflet/issues/10214), 2026-05-12: consideran que renderizar HTML es comportamiento documentado, disputan la clasificación como falla de la biblioteca y recomiendan construir nodos DOM con `textContent` o sanear.
- **Problema observado en nuestro código:** la llamada anterior a `bindPopup()` interpolaba `predio`, `estacion_de_monitoreo`, `cuenca` y `acuifero_monitoreado` sin escape.
- **Tratamiento aplicado en rama P08:** `popupContent(r)` construye nodos DOM y usa `textContent` / `createTextNode` para todos los campos de origen. `bindPopup(popupContent(r))` recibe un nodo, no una plantilla HTML. Se añadieron pruebas estáticas y una prueba funcional Node con valores hostiles.

**Riesgo residual:** Leaflet permanece en versión 1.9.4, la última estable identificada; cualquier nueva invocación de popups/tooltip con HTML no confiable requerirá la misma protección. El aviso externo puede seguir apareciendo en escáneres automatizados aunque se haya mitigado el uso inseguro en la aplicación. No se reporta como «biblioteca sin CVE».

### Chart.js y herramientas ETL

- La consulta focalizada a [Snyk, Chart.js 4.4.7](https://security.snyk.io/package/npm/chart.js/) no mostró vulnerabilidades directas registradas para esa versión al corte, **sin garantías para el futuro ni cobertura completa de transitivas**.
- [Snyk pandas 2.2.3](https://security.snyk.io/package/pip/pandas/2.2.3) y [Snyk openpyxl](https://security.snyk.io/package/pip/openpyxl) no mostraron fallos directos registrados de esas versiones en la consulta efectuada. **No se ejecutó pip-audit sobre un entorno ETL instalado**.
- Una versión más reciente no se adopta automáticamente sin prueba de compatibilidad y nuevo hash verificable. Las actualizaciones de versión deberán actualizar script, SBOM, licencias cuando cambien y pruebas funcionales.

## 3. Mejoras implementadas para prevención de regresiones

1. `scripts/validate_supply_chain.py`: verifica coincidencia del SBOM con las ocho rutas, fuentes HTTPS, versión fijada y hashes SHA-384; exige `uses:` fijados a SHA de 40 caracteres y prohíbe `pull_request_target` y `write-all`.
2. `tests/test_p08_supply_chain.py`: prueba condiciones válidas y fallos provocados por hash inconsistente, popup inseguro, URL OSM antigua y Action flotante.
3. `tests/test_p08_popup_dom.cjs`: ejecuta el constructor de popup con datos hostiles y comprueba que los trata como texto.
4. Workflow separado `verify-p08.yml` para PR: permisos `contents:read`, sin credenciales persistentes, sin publicación; workflow de Pages incorpora controles P08 bloqueantes antes del despliegue.
5. Endpoint OSM del dominio exacto y CSP más restrictiva; licencias íntegramente reproducidas desde las etiquetas oficiales Chart.js 4.4.7 y Leaflet 1.9.4.

## 4. Riesgos pendientes y decisión para el responsable

| Riesgo | Condición residual | Propuesta de tratamiento |
|---|---|---|
| Servicios de teselas externos | Sin SLA propio; política y cambios de proveedor ajenos a CI | Aceptación condicionada para prototipo de consulta; revisar términos de Esri/Topomap y mantener atribuciones. No usar descarga masiva/offline de OSM. |
| Proveedor NaturalSIG | Envío de solicitudes de navegador; disponibilidad y clasificación | Documentar en publicación y política de datos; P01 debe resolver la clasificación. |
| ETL Python transitivo | `requirements.txt` fija directas pero no hashes ni árbol transitivo | Operación técnica posterior: resolver entorno y ejecutar `pip-audit -r requirements.txt`, generar `pip freeze` y lock con hashes si se automatiza el ETL. |
| Pertenencia de riesgo CVE Leaflet | Aviso publicado pese a controversia del upstream | Mantener en registro con control de sanitización DOM y prueba de regresión; monitorizar cambios y avisos. |
| SHA verificadas en build | No sustituyen análisis de vulnerabilidades o firmas oficiales | Mantener manifest y revisar procedencia de cada cambio de versión. |
| Actions / runner | Los avisos de Node 20→24 dependen de la evolución de Actions/runner | `ubuntu-24.04` y Actions por SHA; evaluar futuras advertencias en cada pipeline. |
| Artefacto desplegado | Logs y validaciones de build no equivalen a cotejo de bytes en sitio público | Revisar la ejecución posterior a merge y realizar comprobación visual de la publicación; no declarar esa prueba si no se ejecutó. |

## 5. Criterios para recomendar cierre técnico de P08

- [ ] PR correctivo revisado, integrado y asociado a commit verificable.
- [ ] CI del PR y despliegue del commit final concluidos satisfactoriamente.
- [ ] Regresiones XSS verificadas en popup; política OSM y fuente local comprobadas.
- [ ] Inventario de dependencias, hashes, licencias y fuentes consistente.
- [ ] Riesgos residuales aceptados por el responsable técnico, con alcance registrado; especialmente evaluación ETL transitiva y servicios externos.

**Estado al redactar esta evaluación:** correcciones propuestas y pruebas definidas en una rama. La efectividad de CI y el cierre de P08 se registrarán únicamente tras comprobar los resultados reales. La liberación institucional V4 permanece condicionada por P01, P02, P03, P06, P07, P09, P10 y P12.
