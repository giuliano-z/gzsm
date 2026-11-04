# Checklist de deploy

## Antes
- [ ] Tests del cambio en verde; ningún test anterior roto
- [ ] CI en verde en la rama
- [ ] Pruebas contra el mismo motor de base que producción
- [ ] Migraciones revisadas línea por línea
- [ ] Backup de producción hecho **y verificado** (se puede restaurar)
- [ ] Variables de entorno nuevas cargadas en producción
- [ ] CHANGELOG y versión actualizados
- [ ] Plan de vuelta atrás escrito en el CHANGE

## Seguridad (OWASP, versión corta)
- [ ] Toda entrada nueva está validada del lado del servidor
- [ ] Los permisos nuevos se verificaron con un usuario sin permisos
- [ ] Ningún secreto en el repo ni en los logs
- [ ] Dependencias nuevas sin vulnerabilidades conocidas

## Después
- [ ] Monitoreo activo de logs y errores durante 30 minutos
- [ ] Validación con el usuario agendada
