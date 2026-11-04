---
name: explorar
description: Módulo Explorar de GZSM para cuando no se sabe si algo se puede hacer o cómo: prototipo descartable, prueba de concepto, sondeo técnico o prueba de una herramienta. Permite ir rápido, incluso sin tests, pero con una pregunta escrita, un límite de tiempo, fecha de descarte y una decisión de salida. Usar cuando el usuario quiere probar si algo funciona antes de comprometerse a construirlo.
---

# Explorar

> **Estado: beta.**

Explorar existe para ir rápido sin que el prototipo se convierta en producción sin querer. Se permite el "vibe coding"; lo que no se permite es explorar sin una salida escrita.

## Recorrido

### E1 Entender
Escribir **la pregunta** que el prototipo tiene que contestar: "¿se puede leer un código de barras desde la cámara del celular con menos de un segundo de demora?". Si no hay pregunta, no hay exploración.

### E2 Límites (con `assets/prototipo.md`)
- Tiempo máximo (horas o días).
- **Fecha de descarte** escrita antes de empezar.
- Qué resultado contesta la pregunta por sí y qué resultado la contesta por no.

### E3 Prototipo
- `/prototype` para preguntas de diseño o de lógica; una o varias variantes.
- Carpeta o rama aislada (`prototipos/[nombre]`), sin datos reales de nadie y nunca conectada a producción.

### E5 Decisión de salida
| Decisión | Qué pasa con el código |
|---|---|
| Se descarta | Se borra; queda el registro con lo aprendido |
| Pasa a Construir | **Se reescribe** con el proceso de `gzsm:construir`. El prototipo sirve como referencia, no se promueve |

### E6 Cerrar
Registro con la respuesta a la pregunta y la decisión.

## Criterio de cierre
- [ ] Pregunta, límite de tiempo y fecha de descarte escritos antes de empezar
- [ ] Respuesta registrada (sí, no o depende de qué)
- [ ] Decisión de salida escrita y el prototipo descartado o archivado
