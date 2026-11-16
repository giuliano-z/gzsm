# CHANGE-NNN — [nombre del cambio]

| Campo | Valor |
|---|---|
| Variante | Funcionalidad / Preventivo / Bug |
| Fecha | AAAA-MM-DD |
| Sistema y versión actual | [nombre] vX.Y.Z |
| Pedido por | [persona o rol] |
| Fecha límite | [fecha o "sin fecha"] |

*Relacionado: [estado](../estado.md) · [ADR-NNNN](../adr/NNNN-slug.md) · [PM-NNN](../postmortems/PM-NNN.md) (borrar los que no apliquen)*

## Qué y por qué
[Dos o tres oraciones en términos del negocio, no técnicos.]

## Análisis de impacto
| Pregunta | Respuesta |
|---|---|
| Qué toca directamente | |
| Qué depende de eso | |
| Tests en riesgo | |
| Datos en producción en riesgo | |
| Migraciones | Sí / No |

## Requisitos
Spec: [spec NNN](../../specs/NNN-nombre/spec.md) (o el test que reproduce el bug, entre backticks).

## Fuera de alcance
- [al menos un ítem]

## Plan de vuelta atrás
[Cómo revertir: versión anterior, migración inversa, restaurar backup.]

## Validación con el usuario
*Escrito antes de implementar.*

| Requisito | Qué prueba el usuario en el flujo real | Resultado |
|---|---|---|
| R1 | | |
| N1 | | |

Validó: [quién] · Fecha: AAAA-MM-DD

## Cierre
- [ ] Tests y CI en verde
- [ ] Checklist de deploy completo
- [ ] Validación con el usuario completa
- [ ] [CHANGELOG](../../CHANGELOG.md) con vX.Y.Z
- [ ] Enlazado desde `estado.md` (última sesión)
