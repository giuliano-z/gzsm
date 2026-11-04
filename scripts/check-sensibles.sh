#!/usr/bin/env bash
# GZSM · pre-commit: rechaza el commit si una línea agregada o un nombre de archivo contiene
# un término de una lista de bloqueo. La lista vive FUERA del repo, para no publicar
# justamente lo que se quiere proteger.
# Formato de la lista: un término por línea; las que empiezan con # se ignoran; sin distinguir mayúsculas.
# Ruta: $GZSM_BLOCKLIST, o ~/.config/gzsm/blocklist.txt por defecto.
set -euo pipefail

LIST="${GZSM_BLOCKLIST:-$HOME/.config/gzsm/blocklist.txt}"
if [ ! -f "$LIST" ]; then
  echo "GZSM: no se encontró la lista de bloqueo en $LIST." >&2
  echo "Crearla o definir GZSM_BLOCKLIST. Sin lista no se puede verificar el commit." >&2
  exit 1
fi

patterns="$(tr -d '\r' < "$LIST" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | grep -v '^#' | grep -v '^$' || true)"
[ -z "$patterns" ] && exit 0

status=0

# 1. Nombres de archivo nuevos o modificados.
names="$(git diff --cached --name-only --diff-filter=ACMR || true)"
if [ -n "$names" ]; then
  bad_names="$(printf '%s\n' "$names" | grep -i -F -f <(printf '%s\n' "$patterns") || true)"
  if [ -n "$bad_names" ]; then
    echo "GZSM: nombres de archivo con términos bloqueados:" >&2
    printf '%s\n' "$bad_names" | sed 's/^/  /' >&2
    status=1
  fi
fi

# 2. Líneas agregadas: se compara solo el contenido y se informa archivo y línea.
hits="$(git diff --cached --no-color --no-ext-diff -U0 --diff-filter=ACMR | awk '
  NR == FNR { if ($0 != "") pats[++n] = tolower($0); next }
  /^\+\+\+ (b\/|\/dev\/null)/ { file = substr($0, 7); next }
  /^@@/ { split($3, a, ","); line = substr(a[1], 2) + 0; next }
  /^\+/ {
    text = substr($0, 2); low = tolower(text)
    for (i = 1; i <= n; i++) if (index(low, pats[i])) { print "  " file ":" line ": " substr(text, 1, 160); break }
    line++
  }
' <(printf '%s\n' "$patterns") -)"
if [ -n "$hits" ]; then
  echo "GZSM: líneas con términos bloqueados:" >&2
  printf '%s\n' "$hits" >&2
  status=1
fi

if [ "$status" -ne 0 ]; then
  echo "Quitarlos antes de commitear. Si es un falso positivo, ajustar la lista." >&2
fi
exit "$status"
