---
name: construir
description: Módulo Construir de GZSM para un sistema nuevo cuya demanda ya está validada, sea un producto propio o un sistema a medida para un cliente. Arma el repo con constitución, CLAUDE.md, glosario, ADRs, specs numeradas con EARS e issues, y exige estado.md desde el primer día y runbook antes de producción. Usar cuando se arranca un proyecto nuevo de software que ya pasó por Validar o tiene un cliente comprometido.
---

# Construir

> **Estado: estable** en la estructura del repo y las specs; la variante para clientes se usó en menos proyectos.

**Entrada:** una decisión escrita de Validar (o un cliente que firmó el alcance). Sin eso, volver a `gzsm:validar`. Si no se sabe cómo construirlo, primero `gzsm:explorar`.

## Recorrido

### E1 Entender
- `/grill-with-docs` sobre el producto hasta que no queden decisiones abiertas. Deja el glosario del dominio (`GLOSSARY.md` en las versiones actuales de las skills de Matt; antes `CONTEXT.md`) y los primeros ADRs.
- `/research` para lo técnico desconocido (APIs, costos, límites).

### E2 Especificar (decide una persona)
- **Constitución** (`docs/constitution.md`, plantilla `assets/constitucion.md`): cinco a siete principios verificables que no se negocian.
- **Alcance del MVP** con MoSCoW: debe, debería, podría, no ahora.
- **Una spec por funcionalidad** con `/to-spec`, que la publica en el gestor de issues. Si el repo guarda las specs como archivos, van numeradas en `specs/NNN-nombre/spec.md` con `assets/spec.md`. En los dos casos, con requisitos EARS y Comportamiento no deseado.
- ADRs de arranque con `domain-modeling`: stack, hosting, modelo de datos, autenticación. Cada uno con su señal de cambio.

### E3 Construir
1. Repo con `CLAUDE.md` corto (bloque GZSM en `assets/claude-md.md`), glosario del dominio, `docs/estado.md` y CI desde el primer commit.
2. `/setup-matt-pocock-skills` una vez, con el gestor de issues elegido.
3. `/to-tickets` por spec y `/implement` ticket por ticket con `/tdd`.
4. Con interfaz: `/prototype` o UI UX Pro Max **antes** de implementar la pantalla.
5. Dominio separado de la infraestructura: la lógica de negocio no depende del framework ni de la base.

### E4 Revisar
`/code-review` por cada rama y el checklist de deploy de `gzsm:cambiar` antes de la primera salida.

### E5 Entregar
- **Runbook escrito antes de producción** (plantilla en `gzsm:operar`) y calendario de mantenimiento.
- Primera versión en producción y validación con un usuario real, requisito por requisito.
- A partir de aquí el sistema pasa a **Operar**, y los cambios a **Cambiar**.

### E6 Cerrar
`estado.md`, CHANGELOG con la primera versión y issues para lo que quedó afuera.

## Variante cliente (sistema a medida)
- **Alcance firmado** antes de E3, con "fuera de alcance" explícito.
- Cuentas, dominios y servicios a nombre del cliente desde el inicio.
- **Traspaso:** runbook, credenciales en el gestor del cliente, documentación de uso y una sesión de capacitación registrada.

## Criterio de cierre
- [ ] Constitución, glosario y ADRs de arranque escritos
- [ ] Specs del MVP con comportamiento no deseado
- [ ] CI en verde y checklist de deploy completo
- [ ] Runbook y calendario listos antes de producción
- [ ] Primera versión validada por un usuario real
- [ ] `estado.md` al día; el sistema pasa a Operar
