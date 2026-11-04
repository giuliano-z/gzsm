---
name: sesion-proyecto
description: Abre y cierra sesiones de trabajo sobre un proyecto con la regla de GZSM. Usar cuando el usuario dice "abrí X", "retomemos X", "en qué quedamos con X", "cerrá la sesión", "cerremos por hoy", o cuando termina un bloque de trabajo sobre un repo o una carpeta de proyecto.
---

# Sesión de proyecto

Lo que no está escrito no pasó. Al abrir, Claude se pone al día sin que el usuario pegue nada. Al cerrar, deja el estado escrito para la próxima sesión o para el socio.

## Abrir

1. Encontrá el `estado.md` del proyecto: `docs/estado.md` del repo, el `estado.md` de la carpeta conectada o el que está en el conocimiento del Proyecto de Claude. Si no existe, ofrecé crearlo con `assets/estado-template.md`.
2. Leé los issues abiertos (conector de GitHub o `gh issue list` en Claude Code) y los últimos commits (`git log --oneline -10`, solo lectura).
3. Respondé en cinco líneas como máximo:
   - Dónde quedamos (de la "Última sesión")
   - Módulo y estación GZSM
   - Próximo paso escrito
   - Bloqueos o esperas
   - Tu propuesta para hoy, en una frase

Si lo que dice `estado.md` no coincide con los commits o los issues, avisalo: puede estar viejo.

## Cerrar

1. Juntá lo que pasó en la sesión: qué se hizo, qué se decidió, qué quedó pendiente.
2. Actualizá `estado.md` con la forma de `assets/estado-template.md`:
   - Fecha y quién cerró
   - "Última sesión" con hechos verificables
   - Decisiones nuevas, cada una con su señal de cambio
   - Un solo próximo paso; lo demás va a issues
   - Bloqueos y esperas (a quién se espera y qué)
3. Proponé los issues a crear o cerrar y crealos solo si el usuario confirma.
4. Si hubo una decisión de peso, un cambio sobre un sistema vivo o deuda nueva, ofrecé el ADR, el CHANGE o la DEUDA correspondiente.
5. No corras comandos de git que escriban (commit, push, merge). Mostrá el diff de `estado.md` y un mensaje de commit propuesto; el commit lo hace la persona.

Si no tenés acceso de escritura al proyecto (por ejemplo, en un chat sin carpeta conectada), devolvé el `estado.md` completo listo para pegar y decí dónde va.
