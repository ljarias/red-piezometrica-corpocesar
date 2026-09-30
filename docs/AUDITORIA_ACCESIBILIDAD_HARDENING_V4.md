# Auditoría técnica de accesibilidad y hardening V4

**Fecha:** 2026-09-30  
**Alcance:** revisión de código y controles automatizados. No constituye certificación WCAG.

## Accesibilidad

| Control | Evidencia técnica | Estado |
|---|---|---|
| Idioma de página | html lang=es | Implementado |
| Salto a contenido | skip-link a mainContent | Implementado |
| Estructura de pestañas | tablist/tab/tabpanel + aria-selected | Implementado |
| Operación teclado pestañas | flechas, Home, End | Implementado |
| Formularios | label/for | Implementado |
| Estado dinámico | aria-live | Implementado |
| Foco visible | :focus-visible | Implementado |
| Movimiento reducido | prefers-reduced-motion | Implementado |
| Gráficas | canvas etiquetado + tablas/resúmenes equivalentes | Implementado |
| Mapas | región etiquetada + alternativa textual/listado | Implementado parcialmente |
| Comparación | aria-pressed | Implementado |
| Responsive | breakpoints y tablas desplazables | Implementado |
| Contraste de combinaciones críticas de la paleta | medición reproducible WCAG mediante scripts/validate_contrast.py | Implementado; CI bloqueante |
| Zoom/reflow 200–400 % | requiere prueba manual | Pendiente evidencia |
| Lector de pantalla | requiere prueba NVDA/VoiceOver | Pendiente evidencia |
| Teclado completo Leaflet | requiere prueba manual del componente | Pendiente evidencia |

## Cadena de suministro

Las GitHub Actions del workflow se fijaron a SHA completos resueltos desde los tags aprobados:
- checkout v6: d23441a48e516b6c34aea4fa41551a30e30af803
- configure-pages v5: 983d7736d9b0ae728b81ab479565c72886d7745b
- upload-pages-artifact v4: 7b1f4a764d45c48632c6b24a0339c27f5614fb0b
- deploy-pages v4: d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e

El workflow aplica además mínimo privilegio.

## Dependencias de navegador

Chart.js 4.4.7 y Leaflet 1.9.4 continúan cargándose desde CDN. No se incorporó un hash SRI de Chart.js sin verificarlo criptográficamente. Como siguiente hardening, se recomienda versionar copias locales verificadas de ambas librerías y Leaflet CSS/imagenes, eliminando esas dependencias CDN de ejecución.

Los mapas base permanecen necesariamente sujetos a servicios externos mientras se mantenga la arquitectura actual (OpenStreetMap, Esri y OpenTopoMap).

## Riesgo residual

El proyecto tiene controles de accesibilidad significativamente superiores a la línea base, pero no debe declararse conformidad WCAG 2.1 AA hasta completar pruebas manuales de contraste, zoom/reflow, lector de pantalla y teclado en mapas.


## Medición de contraste 2026-09-30
Se incorporó una comprobación reproducible de las combinaciones críticas de primer plano/fondo usadas por el dashboard, con umbral conservador 4.5:1. Se corrigieron previamente texto secundario, eyebrow, footer y pestaña activa. El control se ejecuta en CI antes del despliegue. Esta medición no sustituye la revisión visual de estados generados por componentes de terceros ni la prueba con lector de pantalla.
