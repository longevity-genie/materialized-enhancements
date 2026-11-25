# Roadmap

Open work only; an item is `## RM<n> — title` with its state and owner under it. Written 2026-11-24 from the
8 open issues, PR #27 and `docs/opengenes-*.md`. Toolchain on this machine: `uv sync` done, `uv run pytest`
650 passed / 10 skipped (14 min); `dolt` is not on the PATH (`pixi global install dolt`); no pre-commit config
exists, so `CLAUDE.md` and `AGENTS.md` are kept identical by hand.

## RM4 — #15 mobile: one-column layout

**State:** unattended
**Owner:** lead

The maintainer's own issue. UI: built, not viewed.

## RM5 — #16 validate the printable protein models

**State:** unattended
**Owner:** lead

Extend `tests/dump_stl_diagnostics.py` and `assets/stl/stl_report.csv` (watertight, difficulty). A batch job if heavy, never on the login node.

## RM6 — OpenGenes: eight directionality defects and `bub1b_t23`

**State:** unattended
**Owner:** lead

Items B and C of `docs/opengenes-open-issues.md`. Rule: `gene_confidence` on existing genes is flagged, never overwritten. Each read against the database first; the rulings are filed on the desk when each is read.

## RM7 — OpenGenes wave 4: 130 never-reviewed genes

**State:** unattended
**Owner:** lead

Needs `dolt` on the PATH and the brief's input artifacts, which live outside this repo and must be found or rebuilt.

## RM8 — #13 gene interaction scores

**State:** blocked: desk #86
**Owner:** lead

Desk #86: build now or park until the UI items land (default: park).

## RM9 — #17 custom builds (class presets)

**State:** unattended
**Owner:** lead

Decided by default (no cost either way). Build after RM2–RM4, presets as data in the database, no code table.

## RM10 — #19 intro video

**State:** unattended
**Owner:** lead

Lead builds the skippable player; the clip itself is made by the maintainer or a volunteer.

## RM11 — #20 UX review "think like a tester"

**State:** unattended
**Owner:** lead

The lead writes findings from the code; each becomes a plan item.

## RM12 — Where pages are looked at

**State:** blocked: desk #87
**Owner:** lead

Needs the maintainer. Desk #87: no page is shown on this server; visual items stay "built, not viewed" until a way of looking is named.
