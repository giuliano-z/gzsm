# Fundamentos y créditos

GZSM no inventa la mayoría de sus piezas: las toma de prácticas conocidas y las ordena por escenario. Esta página dice qué toma de cada fuente, dónde lo usa y qué es propio.

## Qué toma de cada fuente

| Fuente | Autor | Qué toma GZSM | Dónde |
|---|---|---|---|
| [Skills For Real Engineers](https://github.com/mattpocock/skills) | Matt Pocock | Las skills que ejecutan dentro de cada estación: interrogar, especificar, partir en tickets, TDD, revisar, diagnosticar | Todas las estaciones |
| Spec-Driven Development ([Spec Kit](https://github.com/github/spec-kit), [curso Hello SDD](https://github.com/mouredev/hello-sdd)) | GitHub · MoureDev | Especificar antes de implementar, specs pequeñas y numeradas junto al código, constitución del proyecto | Construir, Cambiar |
| [EARS](https://alistairmavin.com/ears/) (Easy Approach to Requirements Syntax, 2009) | Alistair Mavin y otros, Rolls-Royce | La sintaxis de los requisitos y, en especial, el patrón "SI… ENTONCES" para el comportamiento no deseado | Plantilla de spec |
| [Architecture Decision Records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011) | Michael Nygard | Registrar cada decisión con contexto, alternativas y consecuencias | Todos los módulos |
| ISO/IEC 14764 (antes IEEE 1219) | ISO / IEEE | Los cuatro tipos de mantenimiento: correctivo, adaptativo, perfectivo y preventivo | Variantes de Cambiar |
| Leyes de Lehman (1974–1996) | Meir M. Lehman | Un sistema en uso tiene que cambiar o pierde valor: el mantenimiento es parte del ciclo, no un anexo | Operar, Cambiar |
| *Refactoring* (1999) | Martin Fowler | Refactor seguro: tests primero, pasos pequeños, comportamiento observable intacto | Cambiar (preventivo) |
| *Clean Architecture* (2017) | Robert C. Martin | Dominio separado de la infraestructura | Construir |
| *The Lean Startup* (2011) | Eric Ries | Validar con la prueba más barata antes de construir | Validar |
| *The Mom Test* (2013) | Rob Fitzpatrick | Preguntar por comportamientos pasados, no por intenciones | Validar, Orbit |
| Método MoSCoW (1994) | Dai Clegg | Priorizar el alcance del MVP: debe, debería, podría, no ahora | Construir |
| Cinco porqués | Sakichi Toyoda, sistema de producción de Toyota | Buscar la causa raíz antes de arreglar | Operar (incidentes) |
| [Cultura de postmortems](https://sre.google/sre-book/postmortem-culture/) (*Site Reliability Engineering*, 2016) | Google | Postmortem sin culpas, con acciones de prevención | Operar |
| Niveles de severidad de incidentes | Práctica común de la industria, inspirada en la matriz de impacto y urgencia de ITIL | Triage P1 a P4 antes de actuar | Operar |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | OWASP | Checklist corto de seguridad antes de cada deploy | Cambiar, Construir |
| [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) | Olivier Lacan | Formato del CHANGELOG | Cambiar |
| [Semantic Versioning](https://semver.org/lang/es/) | Tom Preston-Werner | Qué número sube en cada tipo de cambio | Cambiar |
| [Agent Skills](https://agentskills.io) | Especificación abierta | El formato de las skills de este plugin | Todo el plugin |

## Qué es propio de GZSM

- **El selector por escenario.** Cuatro preguntas eligen el proceso; ningún trabajo recorre la ceremonia completa si no la necesita.
- **Operar e Implementar como módulos propios.** Las rutinas, los incidentes y el alta de clientes de un producto replicable tienen su recorrido, no se fuerzan dentro de "desarrollo".
- **Las siete estaciones con delegación explícita.** E1 y E4 se pueden delegar a un agente; E2 y E6 los decide una persona.
- **La señal de cambio.** Toda decisión dice qué tendría que pasar para revisarla.
- **La validación con el usuario sin staging.** Validación con el usuario real, requisito por requisito, con un checklist escrito antes de implementar.
- **La regla de cierre.** Toda sesión termina actualizando `estado.md`, con un chequeo automático que lo exige.
- **Orbit.** Nueve ejes para evaluar ideas, con lente latinoamericana y doble carril (rentable y con propósito).
- **Las reglas de ritmo** para trabajar con un agente de código sobre un sistema en producción.

## Relación con las skills de Matt Pocock

GZSM no reemplaza esas skills: decide **cuándo** se usa cada una y **qué tiene que quedar escrito** antes y después. Si mañana cambian las skills, GZSM no cambia. Para no duplicar trabajo, todo lo que esas skills ya hacen bien (spec, tickets, TDD, revisión, ADRs) se delega en ellas.
