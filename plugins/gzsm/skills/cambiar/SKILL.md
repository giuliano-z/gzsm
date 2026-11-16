---
name: cambiar
description: Módulo Cambiar de GZSM para modificar un sistema que ya tiene usuarios. Cubre funcionalidad nueva (mantenimiento perfectivo), adaptación a un entorno que cambió (adaptativo), mejora interna o deuda técnica (preventivo) y arreglo de un bug sin incidente en curso (correctivo), con análisis de impacto, spec con comportamiento no deseado, validación con el usuario requisito por requisito y cierre con CHANGELOG. Usar cuando hay que agregar, corregir, migrar o refactorizar algo en producción.
---

# Cambiar

> **Estado: estable.** Proceso usado en un sistema en producción con usuarios reales.

Un sistema vivo no se modifica como una hoja en blanco: alguien depende de él y tiene datos reales. Cambiar absorbe los cuatro tipos de mantenimiento de ISO/IEC 14764 (antes IEEE 1219).

| Variante | Cuándo | Versión |
|---|---|---|
| **Funcionalidad** (perfectivo) | Alguien pide algo nuevo o distinto | MINOR |
| **Adaptación** (adaptativo) | Cambió el entorno: versión de una dependencia, una API externa, la plataforma o una regulación | PATCH, o MINOR si cambia el comportamiento |
| **Preventivo** | Deuda técnica o degradación medible, sin pedido externo | PATCH |
| **Bug** (correctivo) | Algo funciona mal, sin incidente en curso | PATCH |

Si algo está roto **ahora** en producción, primero `gzsm:operar` (incidente) y después Cambiar para el arreglo de fondo.

## Recorrido

### E0 Entrada
Clasificar la variante y abrir el registro del cambio con `assets/change.md` (`docs/changes/CHANGE-NNN.md`).

### E1 Entender
- **Análisis de impacto, siempre**, antes de tocar código:
  1. ¿Qué módulos, modelos o endpoints toca directamente?
  2. ¿Qué depende de lo que va a cambiar?
  3. ¿Qué tests existentes pueden romperse?
  4. ¿Qué datos en producción pueden quedar inconsistentes?
- **Fase 0 de solo lectura:** leer el código que se va a tocar y todo lo que escribe sobre los mismos datos. Ningún diff antes de terminarla.
- Funcionalidad: `/grill-with-docs` para cerrar el pedido y el vocabulario.
- Bug: `/diagnosing-bugs` hasta **reproducirlo**. Sin reproducción no hay arreglo.

### E2 Especificar (decide una persona)
- Funcionalidad o adaptación: `/to-spec`, que publica la spec en el gestor de issues. El bloque GZSM del `CLAUDE.md` le suma requisitos en EARS y la sección **Comportamiento no deseado** ("SI [situación no deseada], ENTONCES el sistema [respuesta]"). Si el repo guarda las specs como archivos, usar `assets/spec.md`.
- Bug: el **test que falla por el motivo correcto** es la spec.
- Preventivo: la señal de degradación medida y el comportamiento que **no** debe cambiar.
- Escribir el **checklist de validación con el usuario ahora**, derivado de los requisitos. No se improvisa después del deploy.
- Decisión de peso → ADR con `domain-modeling` o con `assets/adr.md`, con su señal de cambio.

### E3 Construir
- Rama propia. Slices de **dos días como máximo** y desplegables solos.
- `/to-tickets` → `/implement` ticket por ticket, con `/tdd`. `/implement` no commitea: termina con el diff y el mensaje propuesto.
- Con interfaz: `/prototype` o UI UX Pro Max antes de implementar.
- Migraciones: mostrarlas completas y revisarlas línea por línea. Backup verificado antes de aplicarlas.
- Reglas de trabajo con el agente: `references/reglas-de-ritmo.md`.

### E4 Revisar
- `/code-review` desde la rama base: estándares del repo y spec.
- Checklist de deploy: `references/checklist-deploy.md`.
- CHANGELOG y versión actualizados **antes** del push.

### E5 Entregar
- Deploy y monitoreo activo después.
- **Validación con el usuario.** Quien pidió el cambio lo prueba sobre el flujo real, requisito por requisito, con el checklist de E2, y el resultado se registra en el CHANGE. Si no hay staging, se valida en producción con ese checklist: un staging con datos sintéticos suele no detectar los defectos que aparecen con datos reales. Si el cambio toca hardware (impresoras, lectores), la prueba incluye el hardware real.
- Si el usuario dice que no: anotar la brecha concreta y volver a E2. No improvisar en el momento.

### E6 Cerrar
- CHANGE completo con el resultado de la validación.
- Deuda detectada en el camino → `assets/deuda.md` (`docs/tech_debt.md`).
- `estado.md` al día con `gzsm:sesion-proyecto`.

## Variante preventiva: cuándo vale la pena

| Señal | Indica | Actuar cuando |
|---|---|---|
| Un archivo supera 300–400 líneas | Responsabilidades mezcladas | Encontrar dónde cambiar algo lleva más de 10 minutos |
| Un cambio simple toca 5 o más archivos | Acoplamiento alto | Pasa dos veces seguidas en la misma zona |
| Cobertura menor a 60 % en un módulo crítico | Riesgo de regresión | De inmediato si tiene lógica de negocio |
| Tiempo de respuesta 20 % peor | N+1, índice o caché | Es medible y reproducible |
| La misma lógica en 3 o más lugares | Duplicación | Toca reglas de negocio |

Priorizar el refactor si el próximo pedido toca esa zona, si hubo dos o más bugs ahí en el último mes o si la cobertura es baja en un área crítica. Priorizar la funcionalidad si hay una fecha comprometida y la deuda no la bloquea.

**Refactor seguro** (Fowler): tests que cubren el comportamiento actual antes de tocar nada; un cambio pequeño por vez con tests verdes en cada paso; rama propia, nunca mezclado con funcionalidad; una línea con el motivo en el PR o el CHANGELOG.

## Criterio de cierre

- [ ] CHANGE escrito con impacto, requisitos y checklist de validación
- [ ] Tests del cambio en verde y ningún test anterior roto; CI en verde
- [ ] Checklist de deploy completo
- [ ] Validación hecha por el usuario y registrada
- [ ] CHANGELOG y versión actualizados
- [ ] `estado.md` al día
