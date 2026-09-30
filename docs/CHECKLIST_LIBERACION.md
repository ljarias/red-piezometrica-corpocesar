# Lista de verificación de liberación institucional

## Antes de procesar
- [ ] Confirmar fuente oficial y responsable de entrega.
- [ ] Verificar que el Excel permanezca fuera de Git.
- [ ] Registrar fecha de recepción y campaña/periodo.
- [ ] Confirmar que no existen cambios metodológicos no documentados.

## Procesamiento
- [ ] Ejecutar actualizar_datos.bat.
- [ ] Resultado distinto de BLOQUEADO.
- [ ] Revisar update_report.json.
- [ ] Confirmar conteos, piezómetros y fechas.
- [ ] Confirmar ausencia de nuevos nulos/duplicados/anomalías no justificadas.
- [ ] Confirmar meta.json, versión ETL y hash SHA-256.

## Revisión funcional
- [ ] Ejecutar run_local.bat.
- [ ] Probar filtros y pestañas.
- [ ] Probar mapa y capas.
- [ ] Probar gráficas y alternativas accesibles.
- [ ] Probar enlaces documentales autorizados.
- [ ] Probar navegación por teclado.

## Publicación
- [ ] Revisar git status.
- [ ] Confirmar que data/source no está staged.
- [ ] Commit descriptivo.
- [ ] Push a main o flujo institucional aprobado.
- [ ] GitHub Actions finaliza SUCCESS.
- [ ] Verificar portal público después del despliegue.

## Cierre
- [ ] Actualizar REGISTRO_PUBLICACION.md.
- [ ] Registrar commit y evidencia CI.
- [ ] Registrar responsable de revisión.
- [ ] Documentar advertencias aceptadas.
