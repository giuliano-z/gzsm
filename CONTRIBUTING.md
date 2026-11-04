# Contribuir

Gracias por el interés. GZSM es una metodología personal publicada para quien le sirva, así que los cambios siguen la misma regla que la metodología.

## Regla de cambio
Un cambio entra cuando el mismo patrón aparece **en dos proyectos o en dos módulos distintos**. Quien mantiene el repo decide qué se incorpora. Por eso, lo más útil es reportar una **fricción**: un momento en que la metodología no alcanzó, con el caso concreto. Hay una plantilla de issue para eso.

## Pull requests
- Un tema por PR.
- Si el cambio toca una skill, correr `python3 scripts/validar-skills.py plugins` antes de abrirlo (también corre en CI).
- Las descripciones de las skills no pueden tener los signos de menor y mayor: claude.ai las rechaza.
- Subir la versión en `plugins/gzsm/.claude-plugin/plugin.json` y sumar la entrada en `CHANGELOG.md`.

## Idioma
Las skills están en español. Las propuestas de traducción son bienvenidas como skills separadas, no mezcladas.
