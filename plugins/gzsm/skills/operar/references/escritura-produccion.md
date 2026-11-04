# Escritura en producción

Toda operación que modifica datos de producción sigue estos cinco pasos, sin excepciones.

1. **Diff aprobado.** El script se muestra completo y una persona lo aprueba.
2. **Prueba en seco por rollback real.** Se ejecutan las escrituras reales dentro de una transacción que se revierte al final. No es una simulación: si algo va a fallar en producción, falla también aquí.
3. **Guarda de identidad de la base.** El script verifica que está conectado a la base correcta (por ejemplo, conteos esperados) y aborta si no. Evita correr contra la base local, o contra producción creyendo que es local.
4. **Snapshot antes de escribir.** Un export de las filas que se van a tocar.
5. **Verificación independiente después.** Con una consulta distinta de la que escribió.

## Dónde viven los scripts
- En una carpeta de operaciones (`ops/`), nunca junto al código de la aplicación: un script olvidado entre el código termina en un deploy, o filtra datos del negocio.
- Se ejecutan como script puntual, no como un comando nuevo de la aplicación: si agregar un comando exige un deploy, el deploy ocurre en medio de la operación.

## Credenciales
La conexión a producción vive en un archivo aparte, con un nombre de variable distinto del que usa la aplicación en local. Se carga para la operación y se descarga al terminar.
