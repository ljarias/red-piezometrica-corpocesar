# Pruebas de seguridad del frontend · V4

## Alcance
Evidencia técnica del hardening del dashboard estático frente a inyección HTML/XSS y enlaces externos no autorizados. No constituye una prueba de penetración externa ni certificación.

## Controles
- Codificación de texto dinámico mediante `esc()`.
- URLs documentales sometidas a `safeUrl()`.
- Solo HTTPS.
- Allowlist: `naturalsig.org` y `www.naturalsig.org`.
- Opciones de filtros construidas con DOM/`textContent`.
- Enlaces en nueva pestaña con `noopener noreferrer`.
- CSP restrictiva compatible con despliegue GitHub Pages.
- `frame-ancestors` no se contabiliza: no es efectivo en CSP entregada por meta.

## Casos de regresión
El CI verifica que no reaparezcan enlaces documentales crudos como `href="${r.ficha}"`, que las funciones de escape/URL permanezcan presentes y que la política HTTPS/allowlist continúe activa.

Vectores de referencia para revisión manual controlada: etiquetas `<script>`, atributos `onerror`, esquemas `javascript:` y dominios externos no incluidos en la allowlist. No deben ejecutarse ni convertirse en enlaces navegables a partir de datos públicos.

## Limitaciones
La validación automática es principalmente estática y de defensa en profundidad. No sustituye DAST, pentest independiente ni controles HTTP que requieran encabezados del servidor. GitHub Pages no ofrece en este proyecto la misma capacidad de configuración de cabeceras que un Apache administrado.

## Criterio de cierre técnico
El frente puede cerrarse cuando CI termine correctamente con los validadores de privacidad, frontend, contraste, dependencias y hardening XSS/URL, y no existan regresiones funcionales observadas.
