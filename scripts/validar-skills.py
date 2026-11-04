#!/usr/bin/env python3
"""Valida el plugin GZSM antes de publicarlo.

- Frontmatter de cada SKILL.md según la especificación de Agent Skills y las reglas de claude.ai.
- Referencias a archivos de la propia skill y a otras skills (gzsm:nombre).
- Plantillas con el mismo nombre en varias skills: tienen que ser idénticas.
- Enlaces relativos de los README y de docs/.
- Versión coherente entre plugin.json, marketplace.json y CHANGELOG.md.

Uso: python3 scripts/validar-skills.py   (desde la raíz del repo)
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "gzsm"
errors, warnings = [], []

skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
names = {p.parent.name for p in skills}
if not skills:
    sys.exit("No se encontró ningún SKILL.md")

for path in skills:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{rel}: falta el frontmatter")
        continue
    fields = dict(re.findall(r"^(\w+):[ \t]*(.*)$", m.group(1), re.M))
    name, desc = fields.get("name", "").strip(), fields.get("description", "").strip()
    if desc in {">", "|", ">-", "|-", ">+", "|+"}:
        errors.append(f"{rel}: description en varias líneas; escribirla en una sola línea")
        desc = ""
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(f"{rel}: name inválido ({name!r}): minúsculas, números y guiones, hasta 64")
    if re.search(r"claude|anthropic", name):
        errors.append(f"{rel}: name no puede contener 'claude' ni 'anthropic'")
    if name != path.parent.name:
        errors.append(f"{rel}: name {name!r} no coincide con la carpeta {path.parent.name!r}")
    if not desc:
        errors.append(f"{rel}: falta description")
    if len(desc) > 1024:
        errors.append(f"{rel}: description de {len(desc)} caracteres (máximo 1024)")
    if re.search(r"[<>]", desc):
        errors.append(f"{rel}: description contiene < o > (claude.ai lo rechaza como etiqueta XML)")
    if len(text.splitlines()) > 500:
        warnings.append(f"{rel}: más de 500 líneas; conviene mover detalle a references/")
    for ref in re.findall(r"`((?:assets|references|scripts)/[^`\s]+)`", text):
        if not (path.parent / ref).exists():
            errors.append(f"{rel}: referencia a {ref}, que no existe")
    for other in re.findall(r"`gzsm:([a-z0-9-]+)`", text):
        if other not in names:
            errors.append(f"{rel}: referencia a la skill gzsm:{other}, que no existe")

# Plantillas compartidas: mismo nombre de archivo, mismo contenido.
by_name = defaultdict(list)
for f in (PLUGIN / "skills").glob("*/assets/*"):
    by_name[f.name].append(f)
for fname, files in by_name.items():
    contents = {f.read_text(encoding="utf-8") for f in files}
    if len(files) > 1 and len(contents) > 1:
        errors.append(f"assets/{fname} difiere entre: " + ", ".join(str(f.parent.parent.name) for f in files))

# Enlaces relativos en la documentación.
docs = [*ROOT.glob("*.md"), *(ROOT / "docs").glob("*.md"), PLUGIN / "README.md"]
for doc in docs:
    if not doc.exists():
        continue
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", doc.read_text(encoding="utf-8")):
        if re.match(r"[a-z]+:", target):
            continue
        if not (doc.parent / target).exists():
            errors.append(f"{doc.relative_to(ROOT)}: enlace roto a {target}")

# Versión coherente.
pv = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())["version"]
mk = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
mv = next((p.get("version") for p in mk["plugins"] if p["name"] == "gzsm"), None)
cl = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
if mv and mv != pv:
    errors.append(f"versión distinta: plugin.json {pv}, marketplace.json {mv}")
if not cl or cl.group(1) != pv:
    errors.append(f"CHANGELOG.md no empieza con la versión {pv}")

for w in warnings:
    print("AVISO", w)
for e in errors:
    print("ERROR", e)
print(f"{len(skills)} skills revisadas · {len(errors)} errores · {len(warnings)} avisos")
sys.exit(1 if errors else 0)
