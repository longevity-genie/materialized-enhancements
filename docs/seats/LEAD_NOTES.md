# Lead notes

State, not rules (rules: `LEAD.md` and the kit's role).

## 2026-11-24 first seating
- Plan: `docs/ROADMAP.md` (RM1-RM12); decisions: `docs/DECISIONS.md` (D1: site is https://enhancement.bio).
- Kept: `sync-dolthub.yml` (the data's own sync). No repo hooks or watchers to retire.
- `CLAUDE.md`/`AGENTS.md` identical (checked); no pre-commit config exists, keep them equal by hand.
- Toolchain: `uv sync` ok; pytest: 650 passed, 10 skipped in 14 min (InvalidMeshWarning from enhancement_geometry noted); `dolt` missing; git-lfs 3.8.1 present.
- Avatar: cursor-agent absent here; asked `#agent-chat>avatars` for a seat to draw "lighthouse keeper at a glowing crystal prism".
- Duties acting (L139): milestones, upstream-index; not yet read/done.
- Nothing on local main unpushed except the docs commit below; nothing in a Dolt clone.

## Maintainer must do by hand
- Merge PR #27 after review (RM1); answer RM8-RM12.

## State at usage limit (2026-11-24)
- Pushed to origin/main: roadmap, D1, notes (53a8f72). Desk #86 (RM8) and #87 (RM12) filed.
- RM1 in progress: branch `build/rm1-remove-hint`, worktree `.worktrees/build-rm1-remove-hint`, one WIP commit (port of PR #27, hidden on touch). Imports fine; NOT tested, NOT merged. Next: a test in tests/test_ui_performance_state.py (hint fires once, only on the first gene), run `uv run pytest tests/test_ui_performance_state.py`, fast-forward into main, push, delete the branch and worktree, thank LauraR20 on the PR and close it as superseded (maintainer's call to close).
- Then RM2 (#25), RM3 (#24), RM4 (#15). Duties milestones / upstream-index not yet done. Avatar still unset.
