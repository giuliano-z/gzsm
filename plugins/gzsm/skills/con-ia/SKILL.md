---
name: con-ia
description: Capa Con IA de GZSM, que se suma a cualquier módulo cuando el sistema tiene un modelo de lenguaje adentro (un asistente, un agente o una función que llama a un LLM). Exige prompts versionados, evals como tests corridos en CI, salida estructurada validada, métricas propias de costo y latencia, modelo de respaldo y trazas por conversación, y un registro de agentes. Usar cuando se construye, cambia u opera un sistema con LLM, o cuando se crea un agente o una tarea automática.
---

# Con IA

> **Estado: beta.**

Un sistema con un LLM adentro falla distinto: no da error, da una respuesta plausible y equivocada. Por eso se prueba con evals y se observa con trazas.

## Reglas

### Prompts
- Versionados en el repo, como código. Cambiar un prompt es un cambio con bump de versión y su CHANGE (`gzsm:cambiar`).

### Evals como tests
- Conversaciones de prueba con el resultado esperado (`assets/evals.md`): casos normales, casos borde y **comportamiento no deseado** (lo que el sistema no tiene que hacer nunca).
- Corren en CI. **Sin evals en verde no se publica una versión.**
- Cada incidente en producción suma un caso nuevo.

### Salida estructurada
Toda herramienta que escribe datos (reservar, cobrar, cancelar) recibe una salida con esquema validado. Si no valida, no se ejecuta.

### Operación
- Métricas propias: costo por conversación, latencia, tasa de derivación a una persona o a un modelo de respaldo.
- Modelo de respaldo definido en el runbook.
- Trazas por conversación (herramientas llamadas y con qué argumentos), guardadas por un plazo definido y sin datos personales de más.

### Agentes
| Tipo | Qué es | Dónde entra |
|---|---|---|
| Subagente | Otro Claude con un encargo pequeño, que vuelve con un resultado | E1 (investigar) y E4 (revisar con contexto limpio) |
| Agente autónomo | Corre sin una persona: tareas programadas, workflows | Operar |
| Agente como producto | Un LLM con herramientas, memoria y reglas que atiende usuarios | Esta capa |

- La salida de un subagente se revisa antes de aplicarse. E2 y E6 no se delegan.
- Todo agente figura en `docs/agentes/registro.md` (`assets/registro-agentes.md`). Un agente sin dueño ni lector se apaga.
