# Lead notes

State, not rules (rules: `LEAD.md` and the kit's role).

## 2026-11-24 first seating
- Plan: `docs/ROADMAP.md` (R1-R7, Q1-Q5); decisions: `docs/DECISIONS.md` (D1: site is https://enhancement.bio).
- Kept: `sync-dolthub.yml` (the data's own sync). No repo hooks or watchers to retire.
- `CLAUDE.md`/`AGENTS.md` identical (checked); no pre-commit config exists, keep them equal by hand.
- Toolchain: `uv sync` ok; pytest: 650 passed, 10 skipped in 14 min (InvalidMeshWarning from enhancement_geometry noted); `dolt` missing; git-lfs 3.8.1 present.
- Avatar: cursor-agent absent here; asked `#agent-chat>avatars` for a seat to draw "lighthouse keeper at a glowing crystal prism".
- Duties acting (L139): milestones, upstream-index; not yet read/done.
- Nothing on local main unpushed except the docs commit below; nothing in a Dolt clone.

## Maintainer must do by hand
- Merge PR #27 after review; answer Q1-Q5 in ROADMAP.
