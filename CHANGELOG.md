# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Versionado [SemVer](https://semver.org/lang/es/).

## [1.1.0] - 2026-11-15
### Agregado
- Convención de enlaces entre documentos (metodología, §9): Markdown relativo dentro de los repos, el formato de la base de notas fuera de ellos y backticks para rutas y comandos.
- Base de notas personal opcional: nota central por proyecto, un solo `estado.md` e índice de sesiones.
- Plantilla de ADR en `construir` y `cambiar`, con señal de cambio.

### Cambiado
- `sesion-proyecto`: al abrir lee primero la nota central; al cerrar suma las notas nuevas al índice de sesiones y verifica que enlacen a la nota central.
- Plantillas de `estado.md`, spec, CHANGE y postmortem con enlaces Markdown relativos.
- `construir`: el alta crea la nota central y su fila en el índice general.
- `implementar`: lo del cliente vive en `docs/clientes/` del repo y se enlaza desde la nota central del producto, sin nota central propia.
- `colaborar`: nada que el otro necesite queda solo en notas personales.
- Bloque de `CLAUDE.md` con la regla de enlaces.

## [1.0.0] - 2026-11-04
### Agregado
- Variante de adaptación (mantenimiento adaptativo) en `cambiar`.
- Una skill por módulo: `validar`, `explorar`, `construir`, `implementar`, `cambiar` y `operar`, cada una con su recorrido por estaciones, plantillas y criterio de cierre.
- Skills de capa: `colaborar` y `con-ia`.
- `orbit`: nueve ejes para evaluar una idea, usada en Validar.
- Plantillas: spec con EARS, CHANGE, deuda técnica, runbook, calendario de mantenimiento, postmortem, constitución, bloque de `CLAUDE.md`, hipótesis, idea, prototipo, alta de cliente, evals y registro de agentes.
- Reglas de ritmo para trabajar con un agente sobre un sistema en producción y protocolo de escritura en producción.
- Scripts de pre-commit: `check-estado.sh` (exige `estado.md` al cambiar código) y `check-sensibles.sh` (lista de bloqueo externa).
- Validación de skills en CI (`scripts/validar-skills.py`).
- `docs/fundamentos.md` con las fuentes y los créditos.
- README en inglés y en español, ícono, guía de contribución y plantilla de issue para fricciones.

### Cambiado
- `gzsm` deriva a la skill del módulo elegido.
- Redacción en español neutro.

## [0.2.0] - 2026-11-04
### Agregado
- Primera versión pública: skills `gzsm` y `sesion-proyecto`, marketplace y metodología de referencia.

[1.1.0]: https://github.com/giuliano-z/gzsm/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/giuliano-z/gzsm/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/giuliano-z/gzsm/releases/tag/v0.2.0
