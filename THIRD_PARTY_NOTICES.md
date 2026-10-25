# Avisos de software de terceros

Este proyecto utiliza componentes de código abierto descargados y verificados durante la preparación/despliegue.

## Chart.js
- Versión fijada: 4.4.7
- Proyecto: Chart.js
- Licencia: MIT
- Uso: visualizaciones estadísticas y series temporales.
- El archivo utilizado se obtiene mediante `scripts/vendor_frontend.py` y se valida con SHA-384.
- [Texto íntegro de licencia MIT incluido en la distribución](licenses/Chart.js-4.4.7-MIT.txt) ([fuente original v4.4.7](https://github.com/chartjs/Chart.js/blob/v4.4.7/LICENSE.md)).

## Leaflet
- Versión fijada: 1.9.4
- Proyecto: Leaflet
- Licencia: BSD-2-Clause
- Uso: mapas interactivos.
- JavaScript, CSS e imágenes se obtienen mediante `scripts/vendor_frontend.py` y se validan con SHA-384.
- [Texto íntegro de licencia BSD-2-Clause incluido en la distribución](licenses/Leaflet-1.9.4-BSD-2-Clause.txt) ([fuente original v1.9.4](https://github.com/Leaflet/Leaflet/blob/v1.9.4/LICENSE)).

## Mapas base
El dashboard puede solicitar teselas de OpenStreetMap, Esri y OpenTopoMap. Sus atribuciones se muestran en el propio mapa. El uso de estos servicios está sujeto a las condiciones de sus respectivos proveedores.

## Alcance
La inclusión de este archivo documenta dependencias y licencias identificadas; no transfiere derechos sobre datos institucionales, documentos técnicos ni información de CORPOCESAR/NaturalSIG.

## Inventario y revisión de seguridad (P08)

- [SBOM directo CycloneDX 1.5](docs/SBOM_P08.json): componentes frontend, herramientas de ETL y ocho archivos con SHA-384 en base64.
- [Evaluación de riesgo de cadena de suministro](docs/EVALUACION_P08_SEGURIDAD.md): CVE-2025-69993, manejo de popups, proveedores externos y pendientes.
- El SBOM no incluye dependencias transitivas Python instaladas, ni reemplaza una herramienta de revisión actualizada de vulnerabilidades.
- El uso de OpenStreetMap, Esri y OpenTopoMap requiere atribución, respeto a condiciones de uso y tratamiento de transferencia a terceros.
