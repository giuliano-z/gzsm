---
name: sesion-proyecto
description: Abre y cierra sesiones de trabajo sobre un proyecto según la regla de GZSM. Usar cuando el usuario dice "abrí X", "abre X", "retomemos X", "en qué quedamos con X", "cerrá la sesión", "cierra la sesión", "cerremos por hoy", o cuando termina un bloque de trabajo sobre un repo o una carpeta de proyecto.
---

# Sesión de proyecto

Lo que no está escrito no pasó. Al abrir, Claude se pone al día sin que nadie pegue contexto. Al cerrar, el estado queda escrito para la próxima sesión o para otra persona.

Si el proyecto tiene **nota central** en una base de notas personal (por ejemplo, un vault de Obsidian), los pasos marcados *con base de notas* aplican. La ruta de la nota central la da el `CLAUDE.md` del repo o el global. La convención de enlaces está en `gzsm:gzsm` (metodología, §9).

## Abrir

1. *Con base de notas:* leer primero la nota central. De ahí salen el `estado.md`, el índice de sesiones y el resto de los documentos.
2. Encontrar el `estado.md` del proyecto: `docs/estado.md` del repo, el de la carpeta conectada o el que esté en el conocimiento del proyecto. Si no existe, ofrecer crearlo con `assets/estado-template.md`.
3. Leer los issues abiertos (conector de GitHub o `gh issue list`) y los últimos commits (`git log --oneline -10`, solo lectura).
4. Responder en cinco líneas como máximo:
   - Dónde quedó (de "Última sesión")
   - Módulo y estación GZSM
   - Próximo paso escrito
   - Bloqueos o esperas
   - Propuesta para hoy, en una frase

Si `estado.md` no coincide con los commits o los issues, avisar: puede estar desactualizado.

## Cerrar

1. Reunir lo que pasó en la sesión: qué se hizo, qué se decidió, qué quedó pendiente, y qué notas y documentos se crearon.
2. Actualizar `estado.md` con la forma de `assets/estado-template.md`:
   - Fecha y quién cerró
   - "Última sesión" con hechos verificables ("spec 003 escrita", no "avancé con la spec"), con enlace al documento cuando lo hay
   - Decisiones nuevas, cada una con su señal de cambio
   - Un solo próximo paso; el resto va a issues
   - Bloqueos y esperas: a quién se espera y qué
3. *Con base de notas:*
   - Agregar al índice de sesiones del proyecto una línea por cada nota nueva de la sesión: enlace y una frase. El índice solo crece; las notas ya escritas no se reescriben.
   - Verificar que toda nota creada en la sesión enlace a la nota central. Si falta, agregar el enlace.
   - Los documentos nuevos del repo (spec, ADR, CHANGE, postmortem) no enlazan a la nota central, que vive fuera del repo: se suman a la nota central y a `estado.md`.
4. Proponer los issues a crear o cerrar, y crearlos solo con confirmación.
5. Si hubo una decisión de peso, un cambio sobre un sistema vivo o deuda nueva, ofrecer el ADR, el registro de cambio o la entrada de deuda.
6. No hacer commit, push ni merge al cerrar. Mostrar el diff de `estado.md` (y de las notas tocadas) y un mensaje de commit propuesto: el commit lo hace la persona.

Sin acceso de escritura al proyecto (por ejemplo, en un chat sin carpeta conectada), devolver el `estado.md` completo y las líneas para el índice de sesiones, listos para pegar, e indicar dónde va cada cosa.
