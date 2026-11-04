---
name: colaborar
description: Capa Colaborar de GZSM, que se suma a cualquier módulo cuando trabaja más de una persona (socio, equipo, empleado o grupo de facultad). Define cómo se reparten las tareas con dueño, cómo entra el código por PR, dónde se toman y registran las decisiones, qué puede hacer el agente en repos compartidos y el ritmo de reunión. Usar cuando un proyecto se comparte con alguien o se suma una persona nueva.
---

# Colaborar

> **Estado: estable** en sus reglas de base; la parte de empleados todavía no se usó.

Con dos personas y dos agentes, el riesgo no es técnico: es que cada uno trabaje con un contexto distinto y las decisiones queden en un chat.

## Reglas

### Repo y código
- Repo en una organización compartida, no en la cuenta personal de nadie.
- Rama principal protegida: todo entra por PR, con `/code-review` antes de mergear.
- El agente puede crear ramas y abrir PRs; **nunca** mergea ni pushea a la rama principal.

### Tareas
- Cada issue y cada spec tienen **un dueño**.
- `/triage` etiqueta `ready-for-agent` (lo puede hacer un agente) o `ready-for-human` (necesita a una persona).
- Estados: Activa, Esperando a alguien (dice a quién), Algún día, Hecha.

### Mismo contexto para todos
- Un solo `CLAUDE.md` y un solo glosario del dominio (`GLOSSARY.md`) en el repo: los agentes de cada persona hablan el mismo idioma.
- `estado.md` lo actualiza quien cierra la sesión (`gzsm:sesion-proyecto`).

### Decisiones
- Se toman y se registran en un solo lugar: un ADR o un issue. Nunca solo en un chat de mensajería.
- Cada una lleva su señal de cambio.
- Trabajo en paralelo con plazo: escribir la señal. "Si al [fecha] no está [X], lo toma [persona]".

### Ritmo
Reunión semanal de 30 minutos con tres puntos: qué se hizo, qué se decide, qué sigue. Las decisiones salen escritas.

### Personas nuevas
- Permisos mínimos para empezar; se amplían con el uso.
- Onboarding escrito: qué leer, cómo levantar el entorno, a quién preguntar.
- Primera tarea pequeña y con dueño de apoyo.
