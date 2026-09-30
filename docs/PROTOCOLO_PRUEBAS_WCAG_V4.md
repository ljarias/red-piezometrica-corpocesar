# Protocolo de pruebas manuales WCAG 2.1 AA — V4

**Fecha de preparación:** 2026-09-30  
**Alcance:** dashboard Red Piezométrica CORPOCESAR.  
**Criterio:** este protocolo genera evidencia manual complementaria a los validadores automáticos. No debe declararse conformidad integral hasta completar y aprobar todos los controles aplicables.

## A. Navegación por teclado
1. Cargar el portal y no utilizar el ratón.
2. Pulsar Tab: debe aparecer “Saltar al contenido principal”.
3. Activarlo con Enter: el foco debe llegar al contenido principal.
4. Recorrer filtros, botón Limpiar filtros y pestañas.
5. En pestañas probar Flecha izquierda/derecha, Home y End.
6. Abrir “Ver datos de la gráfica en tabla” con teclado.
7. Comprobar que el foco siempre sea visible y que no exista trampa de teclado.

**Resultado:** [x] Cumple [ ] No cumple  
**Observaciones:** Prueba manual reportada exitosa el 2026-09-30.

## B. Zoom y reflow
Realizar en navegador de escritorio:
- 200 %: [x] sin pérdida de información/controles
- 400 %: [x] contenido principal utilizable sin desplazamiento horizontal global
- comprobar filtros, tarjetas, pestañas, tablas, gráficas y mapas.

Se admite desplazamiento interno en tablas extensas cuando es necesario para preservar su estructura.

**Resultado:** [x] Cumple [ ] No cumple  
**Observaciones:** Prueba manual reportada exitosa el 2026-09-30.

## C. Contraste y estados
Verificar texto normal, encabezados, botones, enlaces, foco, estados de calidad y textos sobre fondos coloreados. Registrar cualquier combinación que no alcance el contraste aplicable.

**Resultado:** [ ] Cumple [ ] No cumple  
**Herramienta/evidencia:**  
**Observaciones:**

## D. Lector de pantalla
Prueba recomendada en Windows con NVDA:
1. título y encabezados comprensibles;
2. filtros anunciados con sus etiquetas;
3. pestañas anunciadas como pestañas y con estado seleccionado;
4. botón Limpiar filtros con nombre accesible;
5. regiones de mapa con nombre;
6. canvas con nombre accesible;
7. tablas alternativas navegables;
8. mensajes dinámicos anunciados por la región aria-live.

**Resultado:** [ ] Cumple [ ] No cumple  
**Lector/versión:**  
**Observaciones:**

## E. Mapas
- [ ] El mapa no es la única forma de acceder a los datos.
- [ ] La tabla/listado equivalente permite identificar piezómetros.
- [ ] Los controles esenciales pueden alcanzarse por teclado.
- [ ] El cambio de mapa base no impide continuar la navegación.
- [ ] El zoom del navegador no oculta permanentemente controles.

**Resultado:** [ ] Cumple [ ] No cumple  
**Observaciones:**

## F. Gráficas
- [x] Variable seleccionada tiene tabla equivalente.
- [x] Comparación tiene resumen textual.
- [x] Nivel piezométrico tiene tabla equivalente.
- [ ] La información esencial no depende exclusivamente del color.

**Resultado:** [ ] Cumple [ ] No cumple  
**Observaciones:**

## G. Responsive
Probar al menos 320 CSS px, 375/390 px, 768 px y escritorio.
- [ ] sin contenido esencial recortado;
- [ ] controles utilizables;
- [ ] objetivos interactivos suficientemente amplios;
- [ ] tablas mantienen desplazamiento interno cuando procede.

**Resultado:** [ ] Cumple [ ] No cumple  
**Observaciones:**

## Acta de resultado
**Responsable de prueba:**  
**Fecha:**  
**Navegador/versión:**  
**Sistema operativo:**  
**Resultado global:** [ ] Aprobado [ ] Aprobado con observaciones [ ] No aprobado  
**Incidencias asociadas:**  
**Firma/aprobación institucional:** pendiente.


## Evidencia de ejecución 2026-09-30
- Navegación por teclado: reportada exitosa.
- Reflow/zoom 200 % y 400 %: reportado exitoso.
- Alternativas accesibles de gráficas: reportadas exitosas.
- CI asociado: run 36718474081, resultado SUCCESS.
- Pendientes para cierre integral de P04: contraste medido y prueba con lector de pantalla (NVDA o equivalente).
