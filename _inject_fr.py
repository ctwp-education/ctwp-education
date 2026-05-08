#!/usr/bin/env python3
"""Build and inject the complete FR language block into i18n.js, then update SUPPORTED_LANGS."""
from pathlib import Path

base = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp")

# ── Load all French dicts ─────────────────────────────────────────────────────
ns = {}
exec((base / "_fr_structural.py").read_text(encoding="utf-8"), ns)
FR_STRUCTURAL = ns["FR_STRUCTURAL"]

ns = {}
exec((base / "_fr_students_dict.py").read_text(encoding="utf-8"), ns)
FR_STUDENTS = ns["FR_STUDENTS"]

ns = {}
exec((base / "_fr_uni_dict.py").read_text(encoding="utf-8"), ns)
FR_UNI = ns["FR_UNI"]

ns = {}
exec((base / "_fr_teachers_dict.py").read_text(encoding="utf-8"), ns)
FR_TEACHERS = ns["FR_TEACHERS"]

print(f"Loaded: {len(FR_STRUCTURAL)} structural, {len(FR_STUDENTS)} students, "
      f"{len(FR_UNI)} uni, {len(FR_TEACHERS)} teachers")

# ── Sanity checks ─────────────────────────────────────────────────────────────
assert len(FR_STUDENTS) == 300, f"Expected 300 students, got {len(FR_STUDENTS)}"
assert len(FR_UNI) == 144, f"Expected 144 uni, got {len(FR_UNI)}"
assert len(FR_TEACHERS) == 344, f"Expected 344 teachers, got {len(FR_TEACHERS)}"
for i in range(288):
    assert f"cd_{i:03d}" in FR_STUDENTS, f"Missing cd_{i:03d}"
for i in range(1, 13):
    assert f"cd_s{i:02d}" in FR_STUDENTS, f"Missing cd_s{i:02d}"
for i in range(144):
    assert f"cd_uni_{i:03d}" in FR_UNI, f"Missing cd_uni_{i:03d}"
for i in range(344):
    assert f"cd_t_{i:03d}" in FR_TEACHERS, f"Missing cd_t_{i:03d}"

# ── Build FR block lines ──────────────────────────────────────────────────────
def esc(v):
    return v.replace("\\", "\\\\").replace('"', '\\"')

lines = []
lines.append('  fr: {')
lines.append('    /* ─────────────── French translations (fr) — structural ─────────────── */')

# Structural keys (in insertion order)
for k, v in FR_STRUCTURAL.items():
    lines.append(f'    "{k}": "{esc(v)}",')

lines.append('    /* Resource card descriptions (288 K-12 + 12 sport) */')
for k in sorted(FR_STUDENTS.keys()):
    lines.append(f'    "{k}": "{esc(FR_STUDENTS[k])}",')

lines.append('    /* University card descriptions (144) */')
for k in sorted(FR_UNI.keys()):
    lines.append(f'    "{k}": "{esc(FR_UNI[k])}",')

lines.append('    /* Teacher card descriptions (344) */')
for k in sorted(FR_TEACHERS.keys()):
    lines.append(f'    "{k}": "{esc(FR_TEACHERS[k])}",')

lines.append('  }')

fr_block = "\n".join(lines)

# ── Inject into i18n.js ───────────────────────────────────────────────────────
src_path = base / "assets" / "js" / "i18n.js"
src = src_path.read_text(encoding="utf-8")

# The PT block ends with "  }\n};" — find the last occurrence of "  }\n};"
end_marker = "\n  }\n};"
pos = src.rfind(end_marker)
if pos == -1:
    raise SystemExit("Could not find end marker '  }\\n};' in i18n.js")

# Insert ",\n" + fr_block before the end_marker's "  }" line
# src[pos] = '\n', src[pos+1:pos+4] = '  }', src[pos+4:pos+6] = '\n};'
# We want: original_content + ",\n" + fr_block + "\n};"
new_src = src[:pos] + ",\n" + fr_block + src[pos + len("\n  }"):]

# ── Update SUPPORTED_LANGS ────────────────────────────────────────────────────
old_langs = "const SUPPORTED_LANGS = ['en', 'de', 'es', 'pt'];"
new_langs = "const SUPPORTED_LANGS = ['en', 'de', 'es', 'pt', 'fr'];"
if old_langs not in new_src:
    raise SystemExit(f"Could not find SUPPORTED_LANGS line in i18n.js")
new_src = new_src.replace(old_langs, new_langs)

src_path.write_text(new_src, encoding="utf-8")

total_cards = len(FR_STUDENTS) + len(FR_UNI) + len(FR_TEACHERS)
print(f"Done — injected FR block ({len(FR_STRUCTURAL)} structural + {total_cards} cards)")
print(f"Updated SUPPORTED_LANGS to include 'fr'")
