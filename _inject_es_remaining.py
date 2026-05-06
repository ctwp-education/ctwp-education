#!/usr/bin/env python3
"""Inject teacher (344) + student (288) ES translations into i18n.js."""
from pathlib import Path

# Load both dicts
ns = {}
exec(open(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\_es_teachers_dict.py", encoding="utf-8").read(), ns)
exec(open(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\_es_students_dict.py", encoding="utf-8").read(), ns)
ES_TEACHERS = ns["ES_TEACHERS"]
ES_STUDENTS = ns["ES_STUDENTS"]

assert len(ES_TEACHERS) == 344, f"Expected 344 teacher entries, got {len(ES_TEACHERS)}"
assert len(ES_STUDENTS) == 288, f"Expected 288 student entries, got {len(ES_STUDENTS)}"

# All teacher keys cd_t_000 through cd_t_343
for i in range(344):
    k = f"cd_t_{i:03d}"
    assert k in ES_TEACHERS, f"Missing {k}"

# All student keys cd_000 through cd_287
for i in range(288):
    k = f"cd_{i:03d}"
    assert k in ES_STUDENTS, f"Missing {k}"

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
src = src_path.read_text(encoding="utf-8")

# Find ES block end
es_start = src.index("\n  es: {")
end_marker = "\n  }\n};"
es_end = src.index(end_marker, es_start)

# Build new lines
new_lines = []
# Add students first (cd_000 - cd_287), then teachers (cd_t_000 - cd_t_343)
for k in sorted(ES_STUDENTS.keys()):
    v = ES_STUDENTS[k]
    v_esc = v.replace("\\", "\\\\").replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v_esc}",')
for k in sorted(ES_TEACHERS.keys()):
    v = ES_TEACHERS[k]
    v_esc = v.replace("\\", "\\\\").replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v_esc}",')

new_block = "\n".join(new_lines)
new_src = src[:es_end] + "\n" + new_block + src[es_end:]
src_path.write_text(new_src, encoding="utf-8")
print(f"Injected {len(ES_STUDENTS)} student + {len(ES_TEACHERS)} teacher = {len(ES_STUDENTS) + len(ES_TEACHERS)} ES card translations")
