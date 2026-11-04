---
name: validar
description: Módulo Validar de GZSM para una idea de producto o servicio sin evidencia de que alguien la quiera o la pague. Convierte la idea en hipótesis escritas con criterio de éxito, diseña la prueba real más barata (entrevistas, landing con precio, preventa, servicio manual) y termina en una decisión escrita. Usar cuando aparece una idea nueva, alguien trae una propuesta, o hay que decidir precio o modelo de cobro de algo que todavía no tiene clientes que paguen.
---

# Validar

> **Estado: beta.** El proceso está definido y se usó en casos puntuales; todavía no en varios proyectos completos.

**Principio:** nada pasa a Construir sin evidencia de que alguien lo quiere. Lo que cuenta como evidencia es un comportamiento (pagó, se anotó, volvió a usarlo), no una opinión ("me encantaría").

## Recorrido

### E1 Entender
- Evaluar la idea con los nueve ejes de `gzsm:orbit`.
- `/research` para mercado, competencia y costos reales.
- `/grill-me` a quien trae la idea, o a uno mismo.
- Entrevistas al estilo de *The Mom Test*: preguntar por lo que la persona hizo la última vez que tuvo el problema y cuánto le costó, no por lo que haría.

### E2 Especificar las hipótesis (decide una persona)
Con `assets/hipotesis.md`. Cada hipótesis tiene un **criterio de éxito numérico decidido antes de probar**:
- Problema: "[segmento] tiene [problema] al menos [frecuencia]"
- Disposición a pagar: "[n] de [m] aceptan pagar [precio] por [período]"
- Canal: "se consiguen [n] interesados en [días] por [canal]"

### E3 Prueba real
La más barata que conteste la hipótesis más riesgosa:
| Prueba | Contesta |
|---|---|
| Cinco o más entrevistas sobre comportamiento pasado | ¿El problema existe y duele? |
| Landing con precio y lista de espera | ¿Hay interés con un precio a la vista? |
| Preventa o anticipo | ¿Pagan de verdad? |
| Servicio manual (concierge) | ¿El resultado les sirve antes de automatizarlo? |

Simular personas con IA sirve para afilar preguntas, **nunca como evidencia**.

### E5 Decisión escrita
| Decisión | Qué queda |
|---|---|
| Se descarta | Archivo con lo aprendido y la condición para revisarla |
| Se explora | Pasa a `gzsm:explorar` con la pregunta técnica abierta |
| Se construye | Pasa a `gzsm:construir` con las hipótesis validadas como insumo |

### E6 Cerrar
Registro completo y `estado.md` o nota de la idea al día.

## Reglas
- Ponerle fecha límite a la validación. Sin fecha, una idea se valida para siempre.
- Sin un usuario real identificado, el problema no está validado.
- Proyectos rentables y proyectos con propósito se evalúan con criterios distintos y no se mezclan.

## Criterio de cierre
- [ ] Hipótesis con criterio de éxito escrito antes de probar
- [ ] Al menos una prueba real con resultado registrado
- [ ] Decisión escrita con su señal de cambio
