# Reglas de ritmo para trabajar con un agente en un sistema en producción

Doce reglas aprendidas manteniendo un sistema en producción con un agente de código. Cada una nació de un error real.

1. **Una conversación por slice o ticket.** Arranca con un kickoff escrito y cierra actualizando el estado. Una conversación larga mezcla contextos y el agente pierde el hilo.
2. **Slices de dos días como máximo, desplegables solos.** Si no se puede desplegar solo, no es un slice.
3. **Fase 0 de solo lectura antes de cualquier diff.** Leer el código a tocar y todo lo que escribe sobre los mismos datos. La mayoría de los bugs nuevos vienen de una escritura que nadie miró.
4. **Diff aprobado siempre.** Si el repo despliega a producción al hacer push, el agente trabaja en modo manual: nada de aceptar ediciones automáticamente.
5. **Un tema por commit. El test rojo se commitea.** Y solo vale si falla por el motivo correcto: clasificar cada falla antes de seguir.
6. **Las pruebas contra el mismo motor de base que producción corren antes del push.** Un test que pasa en SQLite puede fallar en Postgres.
7. **Prueba manual de la pantalla antes de documentar.** Los tests en verde no prueban lo que no cubren, sobre todo en el frontend.
8. **Ningún documento afirma un flujo que no se verificó.** Ni un docstring, ni un texto de ayuda, ni un CHANGE.
9. **CHANGELOG antes del push.** Si el deploy trae migración: todo cerrado en local y backup verificado.
10. **Git lo corre una persona.** En repos personales, el agente no escribe en git; en repos compartidos puede crear ramas y abrir PRs, nunca mergear. Reforzarlo con reglas de denegación en la configuración del agente. Nunca `git add .`: rutas explícitas.
11. **Comandos sin marcadores entre signos de menor y mayor.** Shells como zsh los interpretan como redirección y el comando hace otra cosa.
12. **Las credenciales de producción no viven en el entorno por defecto.** Van en un archivo aparte, con un nombre de variable distinto del que usa la aplicación en local; se cargan para la operación y se descargan después. Así un comando local nunca apunta a producción por error.
