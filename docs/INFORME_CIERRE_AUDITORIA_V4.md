# Informe de cierre de auditoría V4 — Red Piezométrica CORPOCESAR

**Estado:** candidata técnica condicionada para institucionalización.  
**Alcance:** arquitectura, privacidad, accesibilidad, integridad de datos, seguridad, CI/CD, trazabilidad y documentación.  
**Criterio:** un control implementado no equivale por sí mismo a certificación jurídica, de seguridad o de accesibilidad.

## 1. Resumen ejecutivo

La versión inicial era funcional, pero presentaba riesgos relevantes de publicación de información no minimizada, accesibilidad incompleta, dependencia de validaciones manuales, ausencia de pruebas automatizadas y documentación institucional insuficiente.

La V4 incorpora privacidad por diseño, lista blanca de campos públicos, controles de URLs, navegación accesible, pruebas de contrato, validación estática del frontend, comparación segura de actualizaciones, hash de fuente, CI/CD bloqueante y un paquete documental institucional.

No se recomienda declarar todavía cumplimiento integral. Permanecen decisiones que requieren aprobación de CORPOCESAR y validaciones técnicas especializadas.

## 2. Comparativo de hallazgos

| Hallazgo inicial | Criticidad inicial | Acción V4 | Estado | Riesgo residual |
|---|---|---|---|---|
| Excel institucional podía inducir publicación excesiva | Crítica | Excel fuera de Git + lista blanca | Corregido | Bajo |
| propietario y otros campos innecesarios en JSON | Crítica | Eliminados y bloqueados en CI | Corregido | Bajo |
| Documentos públicos sin clasificación formal | Crítica | Matriz de clasificación | Parcial | Alto hasta decisión institucional |
| WCAG sin controles suficientes | Alta | ARIA, teclado, labels, foco, skip-link, reduced-motion | Parcial avanzado | Medio |
| Gráficas sin equivalente completo | Alta | Etiquetas accesibles; alternativa completa pendiente | Parcial | Medio |
| Mapa como componente visual | Alta | Región accesible + alternativa textual existente | Parcial avanzado | Bajo/medio |
| Dependencias externas | Alta | Documentadas y controladas parcialmente | Parcial | Medio |
| URLs procedentes de datos sin allowlist | Alta | HTTPS + dominios autorizados | Corregido | Bajo |
| Ausencia de pruebas automatizadas | Alta | unittest + validadores CI | Corregido | Bajo/medio |
| Actualizaciones podían reducir datos sin advertencia | Alta | Comparación y bloqueo | Corregido | Bajo |
| Sin trazabilidad fuerte de fuente | Media | SHA-256 + versión ETL | Corregido al regenerar con V3.3+ | Bajo |
| Fórmula hidrogeológica sin validación formal | Alta | Documentada como riesgo | Pendiente especialista | Alto |
| Muestreo 12 h sin hora en Excel | Alta | Limitación documentada | Mitigado, no resuelto | Medio |
| Manual técnico insuficiente | Alta | Manual técnico V4 | Corregido | Bajo |
| Manual de usuario ausente | Media | Manual de usuario V4 | Corregido | Bajo |
| Clasificación de información inexistente | Crítica | Matriz y registro de decisión | Parcial | Alto hasta aprobación |
| Registro de publicaciones inexistente | Media | Registro formal creado | Corregido estructuralmente | Bajo |
| Rollback no formalizado | Media | Procedimiento Git documentado | Corregido | Bajo |

## 3. Riesgos residuales prioritarios

### R1 — Clasificación institucional
**Nivel:** Alto.  
Coordenadas exactas, predio, seriales, fichas, diseños y fotografías requieren decisión institucional documentada.

### R2 — Validación hidrogeológica
**Nivel:** Alto.  
La relación usada para nivel absoluto y los límites de plausibilidad deben ser aprobados por profesional competente. No deben inventarse umbrales desde desarrollo.

### R3 — Conformidad WCAG integral
**Nivel:** Medio.  
Los controles base están implementados, pero falta evaluación completa con herramientas y pruebas manuales, incluyendo equivalentes de gráficas.

### R4 — Cadena de suministro
**Nivel:** Medio.  
Chart.js, Leaflet, mapas y GitHub Actions mantienen dependencias externas. Se recomienda continuar con versionado local cuando sea viable y fijación verificable de Actions.

### R5 — Gobierno operativo
**Nivel:** Medio.  
Debe designarse formalmente quién aprueba publicaciones, atiende incidentes, valida datos y autoriza excepciones.

## 4. Criterios para producción institucional

La solución puede considerarse candidata técnica cuando el pipeline permanezca exitoso y no existan bloqueos de datos. Para cierre institucional se requieren, como mínimo:

1. decisión firmada de clasificación de los campos/documentos pendientes;
2. validación hidrogeológica de fórmulas y reglas de plausibilidad;
3. auditoría final de accesibilidad con evidencias;
4. designación de responsables de datos, publicación, seguridad y operación;
5. definición de licencia/reutilización y tratamiento como datos abiertos cuando aplique;
6. aprobación del paquete documental.

## 5. Conclusión de auditoría

La V4 reduce de forma sustancial los riesgos críticos identificados en la versión inicial y transforma el proyecto de un dashboard funcional a una solución con controles de ingeniería y gobierno. Los riesgos residuales de mayor importancia ya no dependen principalmente de programación: corresponden a clasificación institucional, validación hidrogeológica, accesibilidad integral y gobierno operativo.

Por tanto, el estado recomendado es **candidata técnica condicionada**, no “cumplimiento total” ni “producción institucional definitiva”.
