#!/usr/bin/env bash
# GZSM · pre-commit: rechaza el commit si cambió código y no cambió docs/estado.md.
# Uso: copiar o enlazar como .git/hooks/pre-commit en un repo que use GZSM.
# Omitirlo una vez (por ejemplo, un commit solo de formato): GZSM_SKIP_ESTADO=1 git commit ...
set -euo pipefail

ESTADO="${GZSM_ESTADO:-docs/estado.md}"
[ "${GZSM_SKIP_ESTADO:-0}" = "1" ] && exit 0

staged="$(git diff --cached --name-only --diff-filter=ACMRD)"
[ -z "$staged" ] && exit 0

# Cambios que no son documentación ni configuración del repo.
code_changes="$(printf '%s\n' "$staged" | grep -Ev '\.(md|txt)$|^docs/|^\.github/' || true)"
[ -z "$code_changes" ] && exit 0

if ! printf '%s\n' "$staged" | grep -qxF "$ESTADO"; then
  echo "GZSM: cambió código y no cambió $ESTADO." >&2
  echo "Cerrar la sesión (skill sesion-proyecto) y agregar $ESTADO al commit," >&2
  echo "u omitir este chequeo una vez con GZSM_SKIP_ESTADO=1." >&2
  exit 1
fi
