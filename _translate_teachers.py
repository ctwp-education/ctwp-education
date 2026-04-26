#!/usr/bin/env python3
"""
Splice teacher EN i18n keys into assets/js/i18n.js, plus per-class handlers
for the new teacher grade-badges (gb-prek/primary/secondary/higher/sen).

EN block: insert after the last cd_uni_NNN line.
gb-* handlers: insert just after the existing uni gb-* handler block, with
a path-aware tweak so .gb-all renders 'teachers.grade.all' on teachers.html
and 'uni.grade.all' on university.html.

German: not yet — keys will fall back to EN until we run the German pass.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
I18N = ROOT / "assets" / "js" / "i18n.js"
KEYS = json.loads((ROOT / "_teachers_i18n_keys.json").read_text(encoding="utf-8"))

src = I18N.read_text(encoding="utf-8")

# ---------- 1. Build the EN block to splice ----------
def fmt(k, v):
    return f"    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},\n"

# Group keys for readability
chrome_keys = [k for k in KEYS if not k.startswith("cd_t_")]
card_keys   = [k for k in KEYS if k.startswith("cd_t_")]

en_block_parts = ["\n    /* ─────────────── Teachers page (16 clusters × 12 cards) ─────────────── */\n"]
for k in chrome_keys:
    en_block_parts.append(fmt(k, KEYS[k]))
en_block_parts.append("    /* Teacher card descriptions (192 cards) */\n")
for k in card_keys:
    en_block_parts.append(fmt(k, KEYS[k]))
en_block = "".join(en_block_parts)

# ---------- 2. Splice EN block ----------
EN_ANCHOR = "    'cd_uni_143': \"Free courses on the UN Sustainable Development Goals — climate, equality, poverty and governance, taught by UN agencies and partners.\",\n"
if EN_ANCHOR not in src:
    raise SystemExit("EN anchor not found — has cd_uni_143 changed?")

# Idempotency: if already inserted, refresh the block instead of duplicating
START_MARK = "    /* ─────────────── Teachers page (16 clusters × 12 cards) ─────────────── */"
if START_MARK in src:
    # Replace existing block (between START_MARK and the closing `},` of the en block)
    pre, _, rest = src.partition(START_MARK)
    # rest currently starts with the previous block + then the rest of file.
    # The en block always ends just before `  },\n  de: {`
    end_marker = "  },\n  de: {"
    _, _, after = rest.partition(end_marker)
    src = pre + en_block.lstrip() + end_marker + after
    print("Refreshed existing teacher EN block.")
else:
    src = src.replace(EN_ANCHOR, EN_ANCHOR + en_block, 1)
    print(f"Inserted teacher EN block ({len(card_keys) + len(chrome_keys)} keys).")

# ---------- 3. Add gb-* class handlers (idempotent) ----------
HANDLER_ANCHOR = "  document.querySelectorAll('.grade-badge.gb-switcher').forEach(el => { el.textContent = t('uni.grade.switcher'); });"
NEW_HANDLERS = """
  /* Teachers page audience badges (page-aware so gb-all picks the right label) */
  var _isTeachersPg = location.pathname.endsWith('teachers.html');
  var _allKey = _isTeachersPg ? 'teachers.grade.all' : 'uni.grade.all';
  document.querySelectorAll('.grade-badge.gb-all').forEach(el => { el.textContent = t(_allKey); });
  document.querySelectorAll('.grade-badge.gb-prek').forEach(el => { el.textContent = t('teachers.grade.prek'); });
  document.querySelectorAll('.grade-badge.gb-primary').forEach(el => { el.textContent = t('teachers.grade.primary'); });
  document.querySelectorAll('.grade-badge.gb-secondary').forEach(el => { el.textContent = t('teachers.grade.secondary'); });
  document.querySelectorAll('.grade-badge.gb-higher').forEach(el => { el.textContent = t('teachers.grade.higher'); });
  document.querySelectorAll('.grade-badge.gb-sen').forEach(el => { el.textContent = t('teachers.grade.sen'); });"""

# Also remove the previous, narrower gb-all handler (it would conflict with our page-aware one).
OLD_GB_ALL = "  document.querySelectorAll('.grade-badge.gb-all').forEach(el => { el.textContent = t('uni.grade.all'); });\n"
if OLD_GB_ALL in src:
    src = src.replace(OLD_GB_ALL, "")

if "Teachers page audience badges" not in src:
    if HANDLER_ANCHOR not in src:
        raise SystemExit("Handler anchor not found — has gb-switcher line changed?")
    src = src.replace(HANDLER_ANCHOR, HANDLER_ANCHOR + NEW_HANDLERS, 1)
    print("Inserted teacher gb-* handlers (page-aware gb-all).")
else:
    print("Teacher gb-* handlers already present — skipped.")

I18N.write_text(src, encoding="utf-8")
print(f"Wrote {I18N} ({len(src):,} bytes)")
