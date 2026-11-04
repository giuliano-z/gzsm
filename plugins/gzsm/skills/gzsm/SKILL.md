---
name: gzsm
description: Punto de entrada de la metodología GZSM. Elige el módulo de trabajo (Validar, Explorar, Construir, Implementar, Cambiar u Operar) para una tarea de software o de servicio tecnológico, indica las estaciones que aplican y deriva a la skill del módulo. Usar cuando el usuario dice "GZSM", "qué módulo es esto", "por dónde arranco", "cómo encaro esto", "en qué estación estamos", o cuando empieza un trabajo nuevo y el proceso no está claro.
---

# GZSM: selector de módulo

GZSM decide **qué tipo de trabajo es**, **en qué orden se hace** y **qué tiene que quedar escrito**. Las skills de ingeniería (por ejemplo, las de Matt Pocock) ejecutan dentro de cada estación. La metodología completa está en `references/metodologia.md`.

## 1. Elegir el módulo

Hacer estas preguntas en orden. Si el usuario ya dio la respuesta, no repetirla.

1. ¿Ya existe y tiene usuarios?
   - Sí, y es una rutina o un incidente → **OPERAR** (`gzsm:operar`)
   - Sí, y es algo nuevo, un arreglo o una mejora interna → **CAMBIAR** (`gzsm:cambiar`)
   - Sí, y es un cliente nuevo del mismo producto → **IMPLEMENTAR** (`gzsm:implementar`)
2. Si no existe: ¿hay evidencia de que alguien lo quiere o lo paga? No → **VALIDAR** (`gzsm:validar`)
3. Si la hay: ¿se sabe cómo construirlo? No → **EXPLORAR** (`gzsm:explorar`) · Sí → **CONSTRUIR** (`gzsm:construir`)
4. ¿Trabaja alguien más? → capa **COLABORAR** (`gzsm:colaborar`). ¿El sistema tiene un LLM adentro? → capa **CON IA** (`gzsm:con-ia`).

Si una respuesta es "no sé", elegir el módulo más barato que la conteste (Validar o Explorar), nunca Construir.

Una pregunta comercial (precio, mercado, modelo de cobro) va a Validar aunque el producto ya exista.

## 2. Estaciones

| Estación | Pregunta |
|---|---|
| E0 Entrada | ¿Qué es esto? |
| E1 Entender | ¿Qué queremos y por qué? |
| E2 Especificar | ¿Qué tiene que pasar, también cuando algo sale mal? |
| E3 Construir | Hacerlo |
| E4 Revisar | ¿Cumple la spec y los estándares? |
| E5 Entregar | ¿Lo usa quien lo pidió y funciona? |
| E6 Cerrar | ¿Qué quedó y qué sigue? |

| Módulo | E0 | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|---|
| Validar | ● | ● | hipótesis | prueba real | — | decisión | ● |
| Explorar | ● | ● | límites | prototipo | — | decisión de salida | ● |
| Construir | ● | ● | ● | ● | ● | ● | ● |
| Implementar | ● | checklist | — | configuración | ● | ● | ● |
| Cambiar | ● | ● | ● | ● | ● | ● | ● |
| Operar | ● | — | — | rutina o incidente | — | ● | ● |

## 3. Responder con este formato

```
Módulo: [MÓDULO] [+ Colaborar] [+ Con IA]
Por qué: [la respuesta del selector que lo decidió, en una línea]
Estaciones: [las que aplican]
Ahora: [estación actual] → [skill o acción concreta]
Queda escrito: [el artefacto de esta etapa: hipótesis, spec, ADR, issue, estado.md…]
```

Después, aplicar la skill del módulo elegido para el detalle del recorrido.

## Reglas

- E2 Especificar y E6 Cerrar las decide una persona. E1 Entender y E4 Revisar se pueden delegar a un subagente, y su salida se revisa antes de aplicarse.
- Toda decisión lleva su **señal de cambio**: la condición que obliga a revisarla ("revisar el hosting al superar N clientes o X USD por mes").
- Las decisiones se registran en un ADR o en un issue, no solo en el chat.
- Una herramienta por trabajo: si dos skills hacen lo mismo, usar la que nombra el módulo.
- En Claude Code, las skills de otros plugins llevan su prefijo (por ejemplo, `/mattpocock-skills:grill-me`); aquí se usa el nombre corto.
- Si una skill nombrada no está instalada, decirlo en una línea y seguir con lo disponible, sin inventar su comportamiento.
