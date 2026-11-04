---
name: sesion-proyecto
description: Abre y cierra sesiones de trabajo sobre un proyecto según la regla de GZSM. Usar cuando el usuario dice "abrí X", "abre X", "retomemos X", "en qué quedamos con X", "cerrá la sesión", "cierra la sesión", "cerremos por hoy", o cuando termina un bloque de trabajo sobre un repo o una carpeta de proyecto.
---

# Sesión de proyecto

Lo que no está escrito no pasó. Al abrir, Claude se pone al día sin que nadie pegue contexto. Al cerrar, el estado queda escrito para la próxima sesión o para otra persona.

## Abrir

1. Encontrar el `estado.md` del proyecto: `docs/estado.md` del repo, el de la carpeta conectada o el que esté en el conocimiento del proyecto. Si no existe, ofrecer crearlo con `assets/estado-template.md`.
2. Leer los issues abiertos (conector de GitHub o `gh issue list`) y los últimos commits (`git log --oneline -10`, solo lectura).
3. Responder en cinco líneas como máximo:
   - Dónde quedó (de "Última sesión")
   - Módulo y estación GZSM
   - Próximo paso escrito
   - Bloqueos o esperas
   - Propuesta para hoy, en una frase

Si `estado.md` no coincide con los commits o los issues, avisar: puede estar desactualizado.

## Cerrar

1. Reunir lo que pasó en la sesión: qué se hizo, qué se decidió, qué quedó pendiente.
2. Actualizar `estado.md` con la forma de `assets/estado-template.md`:
   - Fecha y quién cerró
   - "Última sesión" con hechos verificables ("spec 003 escrita", no "avancé con la spec")
   - Decisiones nuevas, cada una con su señal de cambio
   - Un solo próximo paso; el resto va a issues
   - Bloqueos y esperas: a quién se espera y qué
3. Proponer los issues a crear o cerrar, y crearlos solo con confirmación.
4. Si hubo una decisión de peso, un cambio sobre un sistema vivo o deuda nueva, ofrecer el ADR, el registro de cambio o la entrada de deuda.
5. No hacer commit, push ni merge al cerrar. Mostrar el diff de `estado.md` y un mensaje de commit propuesto: el commit lo hace la persona.

Sin acceso de escritura al proyecto (por ejemplo, en un chat sin carpeta conectada), devolver el `estado.md` completo listo para pegar e indicar dónde va.
