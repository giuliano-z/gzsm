# GZSM (plugin)

Metodología de software por escenario para Claude. La skill `gzsm` hace cuatro preguntas, elige el módulo de trabajo (Validar, Explorar, Construir, Implementar, Cambiar u Operar) y deriva a la skill de ese módulo, que guía el recorrido por siete estaciones con sus checklists y plantillas. `sesion-proyecto` abre y cierra cada sesión leyendo y actualizando `docs/estado.md`. Las capas `colaborar` y `con-ia` se suman cuando trabaja más de una persona o el sistema tiene un LLM adentro.

**Uso:** escribir "GZSM: ¿qué módulo es esto?" al empezar un trabajo, "abrí [proyecto]" al retomar y "cerrá la sesión" al terminar. En Claude Code, cada skill también se puede invocar como `/gzsm:[skill]`.

**Instalar en Claude Code:** `/plugin install gzsm --marketplace giuliano-z/gzsm`. En claude.ai: Customize → Plugins → Add → Add marketplace con `https://github.com/giuliano-z/gzsm`.

**Datos:** el plugin no envía datos a ningún servicio. Solo lee y escribe archivos del proyecto en el que se trabaja.

Documentación completa, plantillas y créditos: https://github.com/giuliano-z/gzsm

*Scenario-based software methodology for Claude, in Spanish. See the repository README for the English overview.*
