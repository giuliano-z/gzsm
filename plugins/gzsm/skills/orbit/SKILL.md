---
name: orbit
description: Orbit, marco de nueve ejes de GZSM para evaluar una idea de producto o servicio antes de invertir en ella (timing, problema real, mercado resignado, arquitectura escalable, stack fit, prueba mínima, construir, comprar o asociarse, moat y modelo de negocio). Pensado con lente latinoamericana. Usar en la estación E1 del módulo Validar, o cuando el usuario pide evaluar, puntuar o comparar ideas de negocio.
---

# Orbit: nueve ejes para evaluar una idea

> **Estado: beta.** Marco en uso para evaluar ideas propias; las preguntas de cada eje siguen en revisión.

Orbit no decide por nadie: ordena la evidencia que falta. Se usa en E1 de `gzsm:validar` y su salida alimenta las hipótesis de E2.

## Los ejes

| # | Eje | Pregunta |
|---|---|---|
| 1 | Timing | ¿Por qué ahora, y no hace tres años o dentro de tres? |
| 2 | Problema real | ¿Quién lo sufre hoy, cuánto le cuesta y qué hace hoy para resolverlo? Comportamientos, no intenciones |
| 3 | Mercado resignado | ¿La gente se acostumbró a convivir con el problema? ¿Por qué nadie lo resolvió? |
| 4 | Arquitectura escalable | ¿Escala sin que cada cliente sea un proyecto a medida? |
| 5 | Stack fit | ¿Qué se puede construir con lo que ya se sabe, y qué falta? |
| 6 | Prueba mínima viable | ¿Cuál es la prueba mínima viable y su primer paso, con fecha? |
| 7 | Construir, comprar o asociarse | ¿Conviene construirlo, comprarlo o asociarse con alguien que ya lo tiene? |
| 8 | Moat | ¿Qué lo hace difícil de copiar: dominio, datos, relaciones? |
| 9 | Modelo de negocio primitivo | ¿Quién paga, cuánto, cada cuánto y en qué moneda? |

## Cómo evaluar
1. Para cada eje: **evidencia** (qué se sabe y de dónde sale), **riesgo** (alto, medio o bajo) y **qué falta** para bajarlo.
2. Separar evidencia de opinión: una opinión se marca como supuesto.
3. Los ejes con riesgo alto se convierten en hipótesis de `gzsm:validar`.
4. Terminar siempre con el eje 6 concreto: la prueba, su primer paso y la fecha.

## Reglas
- **Lente latinoamericana:** inflación, convivencia de moneda local y dólar, cuotas, informalidad, regulación cambiante y brecha digital son el caso base, no un caso borde.
- **Doble carril:** una idea rentable y un proyecto con propósito se evalúan con criterios distintos y no se mezclan en la misma tabla.
- Sin un usuario real identificado, el eje 2 queda en riesgo alto.
- Toda evaluación termina en una decisión escrita: se descarta (con lo aprendido y la condición para revisarla) o pasa a validación con sus hipótesis.

Plantilla de la nota por idea: `assets/idea.md`.
