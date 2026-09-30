# Procedimiento de gestión de incidentes y continuidad — V4

## 1. Objetivo
Definir la respuesta técnica ante indisponibilidad, publicación incorrecta, exposición de información, corrupción de datos o fallo del proceso de despliegue de la Red Piezométrica CORPOCESAR.

## 2. Alcance
Aplica al repositorio, GitHub Actions, GitHub Pages, artefactos JSON públicos, scripts ETL y archivos fuente institucionales usados para generar la publicación.

## 3. Clasificación operativa
| Nivel | Ejemplo | Respuesta inicial |
|---|---|---|
| Crítico | Exposición de datos no autorizados, credencial/secreto publicado | Suspender publicación afectada, preservar evidencia y escalar inmediatamente |
| Alto | Dataset incorrecto publicado, integridad comprometida | Revertir a última versión estable y bloquear nueva publicación |
| Medio | Función del dashboard degradada sin pérdida de integridad | Registrar, corregir y validar mediante CI |
| Bajo | Defecto cosmético o documental | Incorporar en mantenimiento ordinario |

## 4. Flujo
1. Detectar y registrar fecha, versión/commit, síntoma y fuente del reporte.
2. Contener: evitar nuevos despliegues cuando exista riesgo de exposición o integridad.
3. Preservar evidencia: commit, ejecución CI, meta.json, update_report.json y capturas/logs disponibles.
4. Evaluar impacto sobre confidencialidad, integridad, disponibilidad y datos personales.
5. Recuperar mediante reversión al último commit estable cuando corresponda.
6. Ejecutar nuevamente pruebas y validadores.
7. Confirmar disponibilidad y consistencia del portal.
8. Documentar causa raíz, acción correctiva y preventiva.
9. Escalar a los responsables institucionales cuando el incidente involucre datos personales, seguridad o decisiones de publicación.

## 5. Continuidad y recuperación
Git mantiene el historial del código y artefactos públicos. El Excel fuente debe conservarse en el repositorio documental/almacenamiento institucional autorizado, fuera del repositorio público. La recuperación del portal se basa en el último commit estable y un nuevo despliegue validado por CI/CD.

## 6. Evidencia mínima
- identificador del incidente;
- fecha/hora;
- reportante;
- versión/commit;
- categoría y severidad;
- información afectada;
- acciones de contención;
- commit de recuperación;
- resultado CI;
- responsable que autoriza cierre.

## 7. Responsabilidades pendientes de designación
CORPOCESAR debe asignar formalmente: responsable funcional, responsable de publicación/datos, responsable TI/seguridad y canal de escalamiento jurídico/protección de datos.

## 8. Regla de seguridad
Nunca se debe copiar a un Issue público información personal, credenciales, secretos o contenido cuya publicación sea objeto del incidente.
