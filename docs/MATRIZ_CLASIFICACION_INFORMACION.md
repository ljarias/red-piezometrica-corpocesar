# Matriz de clasificación de información — Red Piezométrica CORPOCESAR

> Instrumento técnico para decisión institucional. La clasificación definitiva corresponde a CORPOCESAR y debe quedar respaldada por el acto, fundamento y responsable competente. La conveniencia técnica por sí sola no constituye reserva.

## Criterio jurídico de trabajo

La Ley 1712 de 2014 parte de máxima publicidad y distingue información pública, pública clasificada y pública reservada. Cuando solo una parte de un documento esté protegida, debe evaluarse una versión pública que oculte únicamente la parte indispensable. El Índice de Información Clasificada y Reservada debe mantenerse actualizado.

## Matriz de decisión

| Activo / campo | Finalidad en el portal | Publicación actual | Riesgo identificado | Clasificación técnica preliminar | Acción propuesta | Aprobación institucional |
|---|---|---|---|---|---|---|
| cuenca | Contexto territorial | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| departamento | Contexto territorial | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| municipio | Contexto territorial | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| estación de monitoreo | Identificar red | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| piezómetro | Identificar punto | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| latitud / longitud exactas | Mapa y análisis espacial | Sí | Localización exacta de infraestructura | Requiere evaluación | Mantener provisionalmente; valorar precisión reducida o publicación exacta | Pendiente |
| predio | Contextualizar ubicación | Sí | Puede vincular infraestructura con inmueble/persona | Requiere evaluación | Revisar necesidad; considerar nombre generalizado | Pendiente |
| propietario | No requerido por interfaz | No | Dato personal/privado potencial | No publicable por defecto | Mantener excluido | Pendiente ratificación |
| serial_sensor | Identificación técnica | Sí | Inventario detallado de activo | Requiere evaluación | Revisar necesidad pública; posible exclusión | Pendiente |
| ficha técnica | Consulta documental | Sí | Puede contener campos no destinados a publicación | Documento por documento | Publicar solo versión aprobada | Pendiente |
| diseño mecánico | Consulta técnica | Sí | Detalle de infraestructura | Documento por documento | Evaluar versión pública parcial | Pendiente |
| fotografías | Evidencia visual | Sí | Puede revelar personas, placas, accesos o ubicación sensible | Documento por documento | Revisión previa y versión pública cuando aplique | Pendiente |
| mediciones piezométricas | Seguimiento ambiental | Sí | Bajo, sujeto a calidad/metodología | Publicable | Mantener | Pendiente ratificación |
| temperatura | Seguimiento ambiental | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| conductividad | Seguimiento ambiental | Sí | Bajo | Publicable | Mantener | Pendiente ratificación |
| hash SHA-256 de fuente | Trazabilidad | Sí | Bajo; no revela contenido del Excel | Publicable | Mantener | Pendiente ratificación |
| Excel consolidado fuente | Fuente institucional completa | No | Puede contener datos no destinados a difusión | No publicar automáticamente | Mantener privado; generar versión pública separada si se autoriza | Pendiente |

## Campos ya bloqueados técnicamente

El pipeline impide actualmente la reaparición automática de: `propietario`, `x`, `y` y `fecha_prueba_bombeo`. La lista blanca de exportación evita que columnas nuevas del Excel se publiquen por defecto.

## Procedimiento de aprobación

1. Responsable funcional identifica la finalidad de publicación.
2. Gestión de información / jurídica determina si existe excepción legal aplicable.
3. Seguridad revisa riesgo técnico y exposición de infraestructura.
4. Protección de datos revisa datos personales o semiprivados.
5. CORPOCESAR registra decisión, fundamento, fecha, responsable y plazo cuando corresponda.
6. Desarrollo traduce la decisión a la lista blanca y controles CI/CD.
7. Si un documento contiene partes protegidas y públicas, se prepara versión pública parcial.
8. La decisión se revisa cuando cambie el dataset, el portal o el marco aplicable.

## Registro de decisión

| Campo/documento | Decisión final | Fundamento | Acto/soporte | Responsable | Fecha | Plazo/revisión |
|---|---|---|---|---|---|---|
| Coordenadas exactas | Pendiente | — | — | — | — | — |
| Predio | Pendiente | — | — | — | — | — |
| Serial de sensor | Pendiente | — | — | — | — | — |
| Fichas técnicas | Pendiente | — | — | — | — | — |
| Diseños mecánicos | Pendiente | — | — | — | — | — |
| Fotografías | Pendiente | — | — | — | — | — |
