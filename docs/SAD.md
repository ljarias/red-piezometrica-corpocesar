# Documento de Arquitectura de Software (SAD)

## 1. Propósito
Documentar la arquitectura vigente del portal público Red Piezométrica CORPOCESAR y sus decisiones de seguridad, calidad y operación.

## 2. Alcance
Portal estático de consulta de información piezométrica. No implementa autenticación, escritura pública, PHP ni base de datos de producción. El Excel institucional permanece en zona privada/local y los artefactos JSON derivados son los únicos datos operativos publicados.

## 3. Vista de contexto
```text
Excel institucional privado
        |
        v
scripts/process_excel.py
        |
        +--> validación / lista blanca / hash SHA-256
        v
data/generated/*.json
        |
        +--> pruebas de contrato
        +--> control de privacidad
        +--> validación frontend
        v
GitHub Actions
        v
GitHub Pages
        v
Ciudadanía / personal técnico
```

## 4. Componentes
- Frontend: HTML5, CSS3, JavaScript, Chart.js y Leaflet.
- ETL: Python + pandas + openpyxl.
- Datos públicos: master.json, measurements.json, quality.json y meta.json.
- CI/CD: GitHub Actions.
- Hosting: GitHub Pages.
- Fuente oficial: Excel consolidado institucional.

## 5. Modelo conceptual
CUENCA 1:N ESTACION_MONITOREO 1:N PIEZOMETRO 1:N MEDICION.
PIEZOMETRO se relaciona además con SENSOR y DOCUMENTO. Para evolución futura, SENSOR debe manejarse como entidad histórica para conservar cambios de dispositivo.

## 6. Decisiones arquitectónicas
1. Arquitectura estática por ser un portal público de solo lectura.
2. No introducir PHP/MySQL mientras no exista requerimiento transaccional.
3. Fuente privada separada de publicación pública.
4. Privacidad por diseño mediante lista blanca.
5. Despliegue bloqueado ante fallos críticos.
6. RAW de sensores no automatizado mientras no estén formalizadas las reglas de transformación.

## 7. Calidad ISO/IEC 25010
- Seguridad: minimización, validación de URLs y pipeline.
- Fiabilidad: pruebas de contrato y conservación de versión anterior ante fallo.
- Mantenibilidad: separación ETL/frontend/datos y scripts especializados.
- Usabilidad/accesibilidad: navegación por teclado, ARIA, foco visible y diseño responsive.
- Portabilidad: sitio estático desplegable en cualquier servidor HTTP.

## 8. Riesgos pendientes
- Validación técnica formal de la fórmula de nivel absoluto.
- Límites hidrogeológicos para detección de valores atípicos.
- Clasificación institucional definitiva de coordenadas, predios, seriales, fotos y documentos.
- Dependencias cartográficas externas.
- Auditoría WCAG manual complementaria.

## 9. Recuperación
Git constituye el historial de versiones. Ante una regresión se debe identificar el último commit estable, revertir el cambio y dejar que el pipeline valide y vuelva a desplegar.
