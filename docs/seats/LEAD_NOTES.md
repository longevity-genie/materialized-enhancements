# Lead notes

State, not rules (rules: `LEAD.md` and the kit's role).

## 2026-11-24 first seating
- Plan: `docs/ROADMAP.md` (RM1-RM12); decisions: `docs/DECISIONS.md` (D1: site is https://enhancement.bio).
- Kept: `sync-dolthub.yml` (the data's own sync). No repo hooks or watchers to retire.
- `CLAUDE.md`/`AGENTS.md` identical (checked); no pre-commit config exists, keep them equal by hand.
- Toolchain: `uv sync` ok; pytest: 650 passed, 10 skipped in 14 min (InvalidMeshWarning from enhancement_geometry noted); `dolt` 2.7.7 installed in ~/.local/bin (release binary, 2026-11-26), push path untested; git-lfs 3.8.1 present.
- Avatar: cursor-agent absent here; asked `#agent-chat>avatars` for a seat to draw "lighthouse keeper at a glowing crystal prism".
- Duties acting (L139): milestones, upstream-index; not yet read/done.
- Nothing on local main unpushed except the docs commit below; nothing in a Dolt clone.

## Maintainer must do by hand
- Merge PR #27 after review (RM1); answer RM8-RM12.

## State at usage limit (2026-11-24)
- Pushed to origin/main: roadmap, D1, notes (53a8f72). Desk #86 (RM8) and #87 (RM12) filed.
- RM1 merged and pushed (ported hint, test passes; built, not viewed). Left: thank LauraR20 on PR #27 and close it as superseded (maintainer's call).
- Landed since: RM2 (#25), RM3 (#24), RM4 (#15), RM5 first pass (validator; orphan STLs and a by-eye check left), RM6 (all nine cards already fixed, read 2026-11-26). All UI items are built, not viewed. RM7 blocked on desk #93 (input files). Next: RM9-RM11. Duties milestones / upstream-index not yet done. Avatar still unset.
- RM10 player landed (2026-11-27): overlay shows only when `assets/intro/intro.mp4|webm` exists; the 20-30 s clip itself is the maintainer's or a volunteer's. RM9 code landed, waits on desk #95 (Dolt tables). RM13 and RM14 done.
- upstream-index duty: watcher declared in the (untracked) .blueprints.toml for reflex and enhancement-geometry (2026-11-27); the watchdog reads it only at start, so it is armed after the next `watchdog.py stop lead` and `/seats:seat lead`. Check `watchdog.py watchers lead` then.
- upstream-index armed (cmd fixed to run under py.sh; system python3 has no tomllib). Baseline: reflex 0.11.0 is out (2026-11-12) while pyproject pins reflex==0.9.8; no bump planned, it would need a browser check (RM12). enhancement-geometry 0.2.4 is current.
