## GZSM
- Metodología: GZSM. Antes de arrancar algo nuevo, elegir el módulo con la skill `gzsm`.
- Toda spec, también la que publica `/to-spec`, lleva requisitos en EARS y la sección "Comportamiento no deseado": SI [situación no deseada], ENTONCES el sistema [respuesta].
- `/implement` no commitea: termina mostrando el diff y el mensaje de commit propuesto.
- Los ADRs van en `docs/adr/0001-slug.md` (o donde el repo ya los tenga) y llevan señal de cambio.
- Toda sesión cierra actualizando `docs/estado.md` (skill `sesion-proyecto`).
- Enlaces entre documentos del repo: Markdown relativo (`[estado](docs/estado.md)`), nunca `[[ ]]`, que en GitHub se ve roto. Rutas fuera del repo y comandos, entre backticks.
- En repos personales, el agente no corre comandos de git que escriban. En repos compartidos puede crear ramas y abrir PRs, nunca mergear ni pushear a la rama principal. Nunca `git add .`.
