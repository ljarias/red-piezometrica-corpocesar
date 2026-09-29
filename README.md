# Red Piezométrica CORPOCESAR — V4

Dashboard web estático para consulta y seguimiento de la red piezométrica. Está preparado para publicación mediante **GitHub Pages + GitHub Actions**.

## Arquitectura

- `index.html`, `assets/`: frontend estático.
- `data/generated/`: JSON que consume el dashboard y que sí se publica.
- `data/source/`: Excel institucional local. Por seguridad, los `.xlsx` están ignorados por Git.
- `scripts/process_excel.py`: transforma el Excel consolidado en JSON.
- `.github/workflows/deploy-pages.yml`: despliega automáticamente a GitHub Pages al hacer `push` a `main` o manualmente desde Actions.

## Actualizar datos (cada ~60 días o cuando se requiera)

1. Copie el nuevo Excel como `data/source/BaseDatos_red_piezometrica_SAC.xlsx`.
2. En Windows ejecute `actualizar_datos.bat`.
3. Revise localmente con `run_local.bat` y abra `http://localhost:8000`.
4. Si los datos son correctos:
   - `git add data/generated`
   - `git commit -m "Actualizar datos red piezometrica"`
   - `git push`
5. GitHub Actions publicará automáticamente la nueva versión.

> El Excel fuente no se sube al repositorio por defecto. Esto evita exponer columnas o metadatos que no sean necesarios para el portal público.

## Primera publicación

1. Cree un repositorio vacío en GitHub, por ejemplo `red-piezometrica-corpocesar`.
2. Desde esta carpeta:
   - `git init`
   - `git branch -M main`
   - `git add .`
   - `git commit -m "V3: dashboard red piezometrica"`
   - `git remote add origin https://github.com/USUARIO/red-piezometrica-corpocesar.git`
   - `git push -u origin main`
3. En GitHub: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Revise **Actions** hasta que `Publicar Red Piezométrica` termine correctamente.

## Dominio personalizado (opcional)

Primero publique y valide la URL `usuario.github.io/repositorio/`. Después configure el dominio personalizado en **Settings → Pages** y finalmente el DNS en su proveedor. No agregue un archivo `CNAME` manualmente antes de configurar el dominio en GitHub.

## Fuente consolidada actual

- 23 piezómetros en maestro.
- 22 con lecturas.
- 7.193 lecturas consolidadas.
- Periodo: 25/09/2024 a 26/03/2025.
- Muestreo declarado: 12 horas.

## Nota técnica

El dashboard usa el Excel consolidado como fuente oficial. No se automatiza todavía la conversión directa de archivos RAW de sensores porque existen formatos diferentes y falta documentar completamente las reglas de transformación/compensación.


## Documentación institucional

- [Documento de Arquitectura de Software (SAD)](docs/SAD.md)
- [Diccionario de datos](docs/DICCIONARIO_DATOS.md)
- [Manual técnico](docs/MANUAL_TECNICO.md)
- [Manual de usuario](docs/MANUAL_USUARIO.md)
- [Matriz de cumplimiento](docs/MATRIZ_CUMPLIMIENTO.md)
- [Política de seguridad](SECURITY.md)

La documentación identifica expresamente los controles implementados y los puntos que todavía requieren decisión o validación institucional antes de declarar conformidad plena.
