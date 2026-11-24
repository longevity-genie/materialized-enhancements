# Roadmap

Open work only; an item is `## RM<n> — title` with its state and owner under it. Written 2026-11-24 from the
8 open issues, PR #27 and `docs/opengenes-*.md`. Toolchain on this machine: `uv sync` done, `uv run pytest`
650 passed / 10 skipped (14 min); `dolt` is not on the PATH (`pixi global install dolt`); no pre-commit config
exists, so `CLAUDE.md` and `AGENTS.md` are kept identical by hand.

## RM1 — Review PR #27 "Hint for fast removal"

**State:** unattended

**Owner:** lead (the merge is the maintainer's)

LauraR20, 2026-07-13: a right-click hint under the text box (`pages/index.py`, `state.py`). Review it, then ask the maintainer to merge.

## RM2 — #25 fold a category back up

**State:** unattended

**Owner:** lead

A collapse button on an open category so a long gene list need not be scrolled back. UI: built, not viewed.

## RM3 — #24 icons still active during the intro tutorial

**State:** unattended

**Owner:** lead

UI: built, not viewed.

## RM4 — #15 mobile: one-column layout

**State:** unattended

**Owner:** lead

The maintainer's own issue. UI: built, not viewed.

## RM5 — #16 validate the printable protein models

**State:** unattended

**Owner:** lead

Extend `tests/dump_stl_diagnostics.py` and `assets/stl/stl_report.csv` (watertight, difficulty). A batch job if heavy, never on the login node.

## RM6 — OpenGenes: eight directionality defects and `bub1b_t23`

**State:** queued

**Owner:** lead

Items B and C of `docs/opengenes-open-issues.md`. Rule: `gene_confidence` on existing genes is flagged, never overwritten. Each read against the database first; the rulings go to the maintainer in one batch with RM8–RM12.

## RM7 — OpenGenes wave 4: 130 never-reviewed genes

**State:** queued

**Owner:** lead

Needs `dolt` on the PATH and the brief's input artifacts, which live outside this repo and must be found or rebuilt.

## RM8 — #13 gene interaction scores

**State:** queued

**Owner:** lead

Needs the maintainer. Default: no for now; it changes the budget and sculpture model.

## RM9 — #17 custom builds (class presets)

**State:** queued

**Owner:** lead

Needs the maintainer. Default: yes after RM2–RM4, presets as data in the database, no code table.

## RM10 — #19 intro video

**State:** queued

**Owner:** lead

Needs the maintainer. Default: the maintainer or a volunteer makes the clip; the lead builds the skippable player.

## RM11 — #20 UX review "think like a tester"

**State:** queued

**Owner:** lead

Needs the maintainer. Default: the lead writes findings from the code; each goes into the plan on the maintainer's pick.

## RM12 — Where pages are looked at

**State:** queued

**Owner:** lead

Needs the maintainer. No page is shown on this server: visual items stay "built, not viewed" until a browser run is named.
