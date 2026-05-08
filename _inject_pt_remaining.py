#!/usr/bin/env python3
"""Inject teacher (344) + student (288) pt-BR translations into the existing pt: block of i18n.js."""
from pathlib import Path

ns = {}
exec(open(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\_pt_teachers_dict.py", encoding="utf-8").read(), ns)
exec(open(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\_pt_students_dict.py", encoding="utf-8").read(), ns)
PT_TEACHERS = ns["PT_TEACHERS"]
PT_STUDENTS = ns["PT_STUDENTS"]

assert len(PT_TEACHERS) == 344, f"Expected 344 teacher entries, got {len(PT_TEACHERS)}"
assert len(PT_STUDENTS) == 288, f"Expected 288 student entries, got {len(PT_STUDENTS)}"
for i in range(344):
    assert f"cd_t_{i:03d}" in PT_TEACHERS, f"Missing cd_t_{i:03d}"
for i in range(288):
    assert f"cd_{i:03d}" in PT_STUDENTS, f"Missing cd_{i:03d}"

src_path = Path(r"C:\Users\larsg\OneDrive\Claude Code\01_website ctwp\assets\js\i18n.js")
src = src_path.read_text(encoding="utf-8")

# Find the closing of the pt: block.
# pt: was inserted before "};\n\nconst SUPPORTED_LANGS"
# Find "  }\n};\n\nconst SUPPORTED_LANGS" — that's the end of pt: { ... } and the translations const close
end_marker = "\n  }\n};\n\nconst SUPPORTED_LANGS"
if end_marker not in src:
    raise SystemExit("End marker not found")

# We want to insert the new lines BEFORE the "  }" that closes pt:
# Find position of end_marker, then go back to insert before "\n  }\n};"
pos = src.index(end_marker)
# pos points to the "\n" before "  }\n};\n\nconst SUPPORTED_LANGS"
# Build new lines (inject just before pos)
new_lines = []
for k in sorted(PT_STUDENTS.keys()):
    v = PT_STUDENTS[k].replace("\\", "\\\\").replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v}",')
for k in sorted(PT_TEACHERS.keys()):
    v = PT_TEACHERS[k].replace("\\", "\\\\").replace('"', '\\"')
    new_lines.append(f'    "{k}": "{v}",')
new_block = "\n".join(new_lines)

new_src = src[:pos] + "\n" + new_block + src[pos:]
src_path.write_text(new_src, encoding="utf-8")
print(f"Injected {len(PT_STUDENTS)} student + {len(PT_TEACHERS)} teacher = {len(PT_STUDENTS) + len(PT_TEACHERS)} pt-BR card translations")
