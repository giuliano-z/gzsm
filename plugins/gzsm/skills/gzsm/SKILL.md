---
name: gzsm
description: Aplica la metodología GZSM para decidir cómo encarar un trabajo de software o de servicio tecnológico (idea nueva, bug, funcionalidad, migración, cliente nuevo de un producto, rutina o incidente en producción). Usar cuando el usuario dice "GZSM", "qué módulo es esto", "por dónde arranco", "cómo encaro esto", "en qué estación estamos", o cuando empieza un trabajo nuevo y el proceso no está claro.
---

# GZSM

GZSM decide **qué tipo de trabajo es**, **en qué orden se hace** y **qué tiene que quedar escrito**. Las skills de Matt Pocock y los conectores ejecutan dentro de cada estación. La guía completa está en `references/metodologia.md`: leela cuando necesites el detalle de un módulo, una capa o una regla.

## 1. Elegí el módulo con el selector

Hacé estas preguntas en orden. Si el usuario ya dio la respuesta, no la repitas.

1. ¿Ya existe y tiene usuarios?
   - Sí, y es una rutina o un incidente → **OPERAR**
   - Sí, y es algo nuevo o un arreglo → **CAMBIAR**
   - Sí, y es un cliente nuevo del mismo producto → **IMPLEMENTAR**
2. Si no existe: ¿sabemos que alguien lo quiere o lo paga? No → **VALIDAR**
3. Si sí: ¿sabemos cómo construirlo? No → **EXPLORAR** · Sí → **CONSTRUIR**
4. ¿Trabaja alguien más? → suma la capa **COLABORAR**. ¿Tiene un LLM adentro? → suma **CON IA**.

Si una respuesta es "no sé", elegí el módulo más barato que la conteste (Validar o Explorar), nunca Construir.

## 2. Mostrá las estaciones que aplican

| Estación | Pregunta | Herramienta típica |
|---|---|---|
| E0 Entrada | ¿Qué es esto? | Este selector; `/triage` para pedidos que llegan |
| E1 Entender | ¿Qué queremos y por qué? | `/grill-with-docs` (en un repo) o `/grill-me`, `/research`, `/diagnosing-bugs` para reproducir |
| E2 Especificar | ¿Qué tiene que pasar, también cuando sale mal? | `/to-spec` con "Comportamiento no deseado" en EARS; ADR con `domain-modeling`. En un bug, el test rojo es la spec |
| E3 Construir | Hacerlo | `/to-tickets`, `/implement`, `/tdd`, `/prototype`, `/wizard`; Context7 para docs de librerías |
| E4 Revisar | ¿Cumple la spec y los estándares? | `/code-review` |
| E5 Entregar | ¿Lo usa quien lo pidió y funciona? | Deploy y validación con el usuario requisito por requisito (Paso 6) |
| E6 Cerrar | ¿Qué quedó y qué sigue? | Skill `sesion-proyecto` (cerrar) |

Qué estaciones recorre cada módulo:
- **Validar:** E0, E1, E2 (hipótesis), E3 (prueba real: entrevistas, landing con precio, preventa), E5 (decisión escrita), E6.
- **Explorar:** E0, E1, E3 (prototipo con fecha de descarte), E5 (decisión de salida: se tira o pasa a Construir), E6.
- **Construir y Cambiar (funcionalidad):** todas.
- **Cambiar (bug):** todas; E1 es reproducir y E2 es el test que falla.
- **Implementar:** E0, E1 (checklist de alta), E3 (configuración), E4, E5, E6.
- **Operar:** E0, E3 (rutina o incidente), E5, E6.

## 3. Respondé con este formato

```
Módulo: [MÓDULO] [+ Colaborar] [+ Con IA]
Por qué: [una línea con la respuesta del selector que lo decidió]
Estaciones: [lista]
Ahora: [estación actual] → [skill o acción concreta], por ejemplo "E1 → /grill-me sobre …"
Queda escrito: [qué artefacto sale de esta etapa: hipótesis, spec, ADR, issue, estado.md…]
```

## Reglas

- E2 Especificar y E6 Cerrar las decide una persona. E1 y E4 se pueden delegar a un subagente, y su salida se revisa antes de aplicarse.
- Toda decisión lleva su señal de cambio ("revisamos el hosting cuando pasemos los N clientes o los X USD por mes").
- Las decisiones van a un ADR o a un issue, no solo al chat.
- Una herramienta por trabajo: si dos skills hacen lo mismo, usá la de la tabla.
- Si una skill nombrada no está instalada, decilo en una línea y seguí con lo que haya; no inventes su comportamiento.
