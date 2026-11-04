---
name: operar
description: Módulo Operar de GZSM para mantener vivo un sistema en producción. Cubre rutinas de mantenimiento con calendario, incidentes (triage P1 a P4, protocolo de seis pasos, cinco porqués y postmortem sin culpas), escrituras seguras sobre datos de producción, adopción de un sistema ajeno o heredado, y pausa o baja de un sistema. Usar cuando algo se cayó o falla en producción, cuando toca un mantenimiento recurrente, cuando hay que tocar datos reales, o cuando se recibe un sistema existente.
---

# Operar

> **Estado: estable.** Proceso usado en un sistema en producción con usuarios reales.

El mantenimiento recurrente no es un cambio: es una rutina, y si nada la dispara se olvida. Operar es continuo y cada acción cierra con su registro.

| Variante | Cuándo |
|---|---|
| **Rutina** | Toca un mantenimiento del calendario |
| **Incidente** | Algo falla en producción ahora |
| **Escritura en producción** | Hay que corregir o cargar datos reales |
| **Adopción** | Se recibe un sistema ajeno o con documentación vieja |
| **Pausa o baja** | Un sistema se congela o se apaga |

## Runbook y calendario

Todo sistema en producción tiene `docs/runbook.md` (plantilla: `assets/runbook.md`) y un calendario de mantenimiento (`assets/calendario-mantenimiento.md`). Las fechas del calendario van a un calendario real con recordatorios: un documento que nadie abre no avisa.

## Rutina
1. Abrir la tarea del calendario y seguir el procedimiento del runbook.
2. Registrar qué se hizo y qué se encontró, con fecha.
3. Si aparece algo para arreglar, abrir un issue: el arreglo es `gzsm:cambiar`.

## Incidente

### Triage primero
| Nivel | Criterio | Respuesta |
|---|---|---|
| P1 Crítico | Sistema caído o datos comprometidos | Inmediata; todo lo demás para |
| P2 Alto | Una función central falla para todos | Menos de 2 horas |
| P3 Medio | Falla para algunos usuarios | Menos de 24 horas |
| P4 Bajo | Cosmético o caso raro | No es incidente: va al backlog |

### Protocolo de seis pasos (no avanzar sin terminar el anterior)
1. **Contener.** ¿Se puede reducir el impacto sin tocar código? Reiniciar, revertir el último deploy, modo mantenimiento. Ganar tiempo es válido.
2. **Diagnosticar.** Reproducir con `/diagnosing-bugs` y leer los logs antes de suponer. Sin reproducción no hay arreglo.
3. **Causa raíz.** Cinco porqués: el primero casi nunca es la causa real. Obligatorio en P1 y P2.
4. **Arreglo mínimo.** Rama propia; exactamente lo necesario. No aprovechar la emergencia para refactorizar.
5. **Verificar.** Al menos un test que reproduce la falla y ahora pasa. CI en verde.
6. **Desplegar y monitorear.** Monitoreo activo 30 minutos y confirmación explícita antes de cerrar.

### Postmortem
Obligatorio en P1 y P2, dentro de las 24 horas, con `assets/postmortem.md` (`docs/postmortems/PM-NNN.md`). En P3 alcanza un registro breve en el issue o en el runbook. **Sin culpas:** se busca qué permitió el error, no quién lo cometió. Cada acción de prevención va a un issue con fecha.

### Ejemplo de cinco porqués
```
Síntoma: el stock de un producto quedó negativo después de una venta.
¿Por qué? La venta se procesó sin stock suficiente.
¿Por qué? La validación y el descuento no son atómicos.
¿Por qué? Son dos operaciones separadas.
¿Por qué? Se hizo así en el MVP por velocidad, sin pensar en concurrencia.
¿Por qué? No había un requisito de integridad transaccional.
Causa raíz: falta de transacción atómica en la venta.
Prevención: requisito escrito + test de concurrencia.
```

## Escritura en producción
Protocolo de cinco pasos en `references/escritura-produccion.md`. Sin excepciones.

## Adopción de un sistema ajeno
1. Inventario de solo lectura: qué corre, dónde, con qué datos, quién lo usa.
2. `estado.md` inicial y runbook mínimo **antes** del primer cambio.
3. Backup verificado propio.
4. Recién ahí, el primer cambio por `gzsm:cambiar`.

## Automatizaciones y workflows (n8n u otros)
- Exportar cada versión al repo, con un nombre que diga qué cambió ("v1.3 - agrega recordatorio").
- Nunca editar el workflow publicado sin una copia exportada.
- Si cambia un webhook o una URL de entrada, publicar en dos pasos: primero la versión nueva en paralelo, después el corte.
- Backup de la base que usa el workflow, igual que cualquier sistema.

## Pausa o baja
Exportar los datos, avisar a los usuarios con fecha, apagar servicios y credenciales, archivar el repo y dejar un `estado.md` final con el motivo y dónde quedaron los datos.

## Criterio de cierre
- [ ] Rutina: registro con fecha en el runbook
- [ ] Incidente: servicio restablecido, test de regresión, postmortem escrito y acciones en issues
- [ ] Escritura: verificación independiente hecha
- [ ] `estado.md` al día con `gzsm:sesion-proyecto`
