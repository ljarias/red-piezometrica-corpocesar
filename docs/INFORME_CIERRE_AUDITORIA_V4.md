# Informe consolidado de auditoría V4 — Red Piezométrica CORPOCESAR

**Fecha de corte:** 2026-09-30  
**Estado:** controles técnicos V4 implementados; cierre institucional condicionado.  
**Alcance:** arquitectura, privacidad, accesibilidad, integridad de datos, seguridad frontend, cadena de suministro, CI/CD, trazabilidad y documentación.

> Un control técnico exitoso no constituye por sí mismo aprobación científica, jurídica, de datos abiertos ni autorización institucional de publicación.

## 1. Resumen ejecutivo

La V4 evolucionó desde un dashboard funcional hacia una solución estática con controles preventivos y detectivos automatizados. El Excel institucional permanece fuera del repositorio público; el ETL publica mediante lista blanca; las actualizaciones se comparan con línea base; se incorporan SHA-256 de fuente, guardas de integridad referencial, validación de privacidad, allowlist HTTPS, hardening XSS, CSP compatible con GitHub Pages, dependencias verificadas por SHA-384, Actions fijadas por SHA, pruebas de accesibilidad y CI/CD bloqueante.

El último pipeline de consolidación técnica disponible al corte terminó en **SUCCESS**. Los pendientes principales requieren decisiones de CORPOCESAR/NaturalSIG o validación hidrogeológica.

## 2. Estado consolidado de hallazgos

| Hallazgo | Acción V4 | Estado | Riesgo residual |
|---|---|---|---|
| Publicación excesiva desde Excel | Excel excluido + whitelist pública | Cerrado técnicamente | Bajo |
| Campos personales/no necesarios | Eliminados y bloqueados en CI | Cerrado técnicamente | Bajo |
| Clasificación de coordenadas, predio, seriales y documentos | Matriz creada | Pendiente institucional | Alto |
| Accesibilidad | teclado, foco, reflow 200/400 %, contraste CI, NVDA, alternativas tabulares | Cerrado técnicamente | Bajo/medio |
| Gráficas sin equivalente | tablas/resúmenes accesibles | Cerrado técnicamente | Bajo |
| Dependencias frontend/Actions | versiones fijadas, SHA-384 y SHA exactos | Cerrado técnicamente | Bajo |
| URLs dinámicas | HTTPS + allowlist + safeUrl | Cerrado técnicamente | Bajo |
| XSS por HTML dinámico | escape de texto, DOM seguro y prueba CI | Hardening implementado | Bajo |
| Integridad ETL | fuentes vacías, IDs duplicados y lecturas huérfanas bloqueadas | Cerrado técnicamente | Bajo |
| Trazabilidad de fuente | SHA-256 + versión ETL | Cerrado técnicamente | Bajo |
| Aprobación automática ambigua | CONTROLES_AUTOMATICOS_OK + alcance explícito | Corregido | Bajo |
| Fórmula de nivel absoluto | documentada | Pendiente hidrogeología | Alto |
| Rangos de plausibilidad | no inventados desde software | Pendiente hidrogeología | Alto |
| Muestreo 12 h sin hora en Excel | limitación documentada | Mitigado | Medio |
| Gobierno de publicación | procedimiento/registro creados | Pendiente responsables | Medio/alto |
| Licencias de terceros | THIRD_PARTY_NOTICES.md | Documentado | Bajo |

## 3. Marco normativo y evidencia

### Ley 1581 de 2012
La arquitectura aplica minimización y privacidad por diseño: el archivo fuente no se publica, existe whitelist de campos y el CI bloquea campos prohibidos. La decisión sobre si coordenadas, predio, seriales, fichas y fotografías pueden divulgarse permanece sujeta a clasificación institucional y análisis del contexto de identificación.

### Resolución MinTIC 1519 de 2020
Se implementaron controles técnicos de accesibilidad WCAG 2.1 AA: navegación por teclado, foco visible, reflow/zoom, contraste, lector de pantalla NVDA y equivalentes textuales/tabulares. También existen controles de seguridad digital. El cierre técnico interno no se presenta como certificación externa.

### Ley 1712 de 2014
El proyecto favorece disponibilidad y acceso electrónico a información pública, pero la apertura formal y reutilización requieren que la entidad defina clasificación, licencia y condiciones de publicación.

### Decreto 1078 de 2015
Se implementa defensa en profundidad para confidencialidad, integridad y disponibilidad: privacidad por diseño, validaciones de integridad, CI/CD, trazabilidad, procedimiento de incidentes, dependencias verificadas y controles de seguridad del frontend.

## 4. Seguridad y cadena de suministro

Controles implementados:
- CSP compatible con despliegue estático.
- `frame-ancestors` no se contabiliza como protección porque CSP se entrega mediante `meta`.
- Escape de texto dinámico y validación de URLs.
- `noopener noreferrer` en enlaces externos.
- Chart.js y Leaflet vendorizados durante build con SHA-384.
- GitHub Actions fijadas a SHA exacto.
- CI bloquea regresiones de privacidad, frontend, contraste, XSS/URLs, datos y dependencias.

Limitación residual: GitHub Pages no ofrece en este proyecto el mismo control de encabezados HTTP que un servidor Apache administrado. Una migración futura a infraestructura institucional permitiría HSTS, X-Frame-Options/frame-ancestors vía header, Referrer-Policy y otros encabezados gestionados en servidor.

## 5. Evidencia de accesibilidad

P04 queda **cerrado técnicamente** al 2026-09-30 con evidencia de teclado, foco, navegación de pestañas, zoom/reflow 200 % y 400 %, contraste automatizado y prueba dirigida exitosa con NVDA. P05, equivalentes tabulares/textuales de las visualizaciones, también está cerrado técnicamente.

Esto no se declara como certificación independiente de conformidad WCAG.

## 6. Pendientes que bloquean el cierre institucional

1. **P01:** aprobar clasificación de coordenadas, predio, seriales, fichas, diseños y fotografías.
2. **P02:** validar científicamente la fórmula de nivel absoluto.
3. **P03:** definir rangos hidrogeológicos de plausibilidad.
4. **P06:** designar responsable de publicación/aprobación.
5. **P07:** definir licencia y condiciones de reutilización.
6. **P09:** asignar responsables al procedimiento de incidentes y continuidad.
7. **P10:** aprobar formalmente SAD, manuales y matrices.
8. **P12:** completar responsable y aprobación del registro de liberación.

## 7. Criterio de liberación

`CONTROLES_AUTOMATICOS_OK` significa únicamente que los controles técnicos automatizados no encontraron bloqueos. Antes de publicar una actualización deben existir revisión de los resultados, atención de advertencias, prueba funcional y autorización conforme al gobierno definido por la entidad.

## 8. Conclusión

La deuda técnica crítica identificada en la auditoría inicial se ha reducido sustancialmente. Los controles de desarrollo, accesibilidad, integridad, privacidad preventiva, seguridad frontend y cadena de suministro están implementados y automatizados. El proyecto puede mantenerse como **candidato técnico controlado**, mientras que la declaración de producción institucional definitiva depende de las decisiones y validaciones enumeradas en la sección 6.
