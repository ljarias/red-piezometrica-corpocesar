# Política de seguridad

## Alcance

Este repositorio publica un dashboard estático de solo lectura. El Excel institucional y otros archivos fuente privados no deben incorporarse al repositorio público.

## Reporte responsable

Los hallazgos de seguridad deben comunicarse de forma privada al responsable institucional del proyecto. No publique datos personales, credenciales, secretos ni detalles explotables en Issues públicos.

## Controles de publicación

Antes del despliegue, GitHub Actions valida:

- sintaxis de los JSON públicos;
- contrato e integridad referencial del dataset;
- ausencia de campos expresamente prohibidos;
- HTTPS y dominios autorizados para enlaces documentales;
- requisitos estáticos mínimos de accesibilidad e integridad del frontend.

Un fallo crítico bloquea el despliegue y conserva la versión previamente publicada.

## Secretos y datos personales

No se requieren secretos de aplicación para ejecutar el portal. No deben almacenarse contraseñas, tokens, datos personales no autorizados ni el Excel fuente en el repositorio.

## Dependencias

Las dependencias de frontend y las acciones de CI/CD deben revisarse periódicamente. La fijación criptográfica por SHA de GitHub Actions y la reducción de dependencias CDN forman parte del hardening progresivo.
