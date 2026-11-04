---
name: implementar
description: Módulo Implementar de GZSM para dar de alta un cliente nuevo en un producto replicable que ya funciona (por ejemplo, un bot o un sistema que se instala por cliente). Crea la instancia desde una plantilla, mantiene los datos del cliente fuera del código y sigue un checklist de alta hasta dejar al cliente funcionando y registrado en el runbook. Usar cuando se suma un cliente a un producto existente, no cuando se construye uno nuevo.
---

# Implementar

> **Estado: beta.**

Un producto replicable crece por altas, no por proyectos. Si cada cliente exige código nuevo, el producto no es replicable todavía: eso es `gzsm:cambiar` sobre el producto, no Implementar.

## Recorrido

### E1 Checklist de alta
Copiar `assets/checklist-alta.md` para el cliente y completar los datos de entrada.

### E3 Configuración
- La instancia sale de la **plantilla del producto**, nunca de copiar la de otro cliente.
- **Datos del cliente fuera del código:** configuración y variables de entorno, no constantes en el repo.
- Pasos en paneles de terceros (cuentas de mensajería, pagos, dominios): `/wizard` arma el paso a paso para quien los tiene que hacer.
- Cuentas y servicios a nombre del cliente cuando corresponde.

### E4 Revisar
Pruebas del producto en verde con la configuración del cliente. Si el producto tiene un LLM adentro, sus evals en verde (`gzsm:con-ia`).

### E5 Entregar
Cliente usándolo en su flujo real, con una prueba guiada y registrada.

### E6 Cerrar
Cliente agregado al runbook del producto (contactos, configuración, particularidades) y `estado.md` al día.

## Criterio de cierre
- [ ] Checklist de alta completo
- [ ] Ningún dato del cliente dentro del código
- [ ] Pruebas y evals en verde con su configuración
- [ ] Cliente funcionando y registrado en el runbook
