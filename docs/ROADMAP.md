# Roadmap

Open work only; an item is `## RM<n> — title` with its state and owner under it. Written 2026-11-24 from the
8 open issues, PR #27 and `docs/opengenes-*.md`. Toolchain on this machine: `uv sync` done, `uv run pytest`
650 passed / 10 skipped (14 min); `dolt` is not on the PATH (`pixi global install dolt`); no pre-commit config
exists, so `CLAUDE.md` and `AGENTS.md` are kept identical by hand.

## RM5 — #16 validate the printable protein models

**State:** unattended
**Owner:** lead

`scripts/validate_stl.py` (2026-11-25) cross-checks the 75 report rows and 75 STL files against the database's PDB/UniProt ids. First run: 11 report rows have no gene and no gene uses their PDB id (5W21, 3HH2, 7S5H, 3F1P, 5F3B, 5UDZ, 8Y02, 9C5S, 5MEO, 5VAQ, 9QNG: orphan files, to delete or map; the maintainer's call, they are LFS-tracked); every STL file has a report row (the extra directory entries are not STLs); every model is reported not watertight (cartoon renders with many shells, expected, but a print check on one model with a slicer is still missing). Next: decide the orphans with the maintainer, then compare a few models with their PDB structure by eye (someone with a viewer).

## RM6 — OpenGenes: eight directionality defects and `bub1b_t23`

**State:** unattended
**Owner:** lead

Items B and C of `docs/opengenes-open-issues.md`. Rule: `gene_confidence` on existing genes is flagged, never overwritten. Read against `data/enhancement.db` on 2026-11-26: `bub1b_t23` is already fixed (its primary row now says human genetics "bounds the deficiency side only" and that the case rests on the mouse overexpression arm); `foxo3` and `klotho` knockout rows are both `positive=false` now, one convention; `aqp1`, `hsf1_pv`, `xrcc5_roughy`, `uhrf1_deer`, `lrrc10_cardiac`, `rgy_pyrococcus` cards already say in `short_description` that the loss-of-function result shows necessity, not benefit of extra copies. Left: read their `narrative`, `achievements` and `mechanism` for the same slip (`uhrf1_deer` and `lrrc10_cardiac` have no primary confidence row to check), and flag any that remain to the maintainer; no edits to existing genes, and `dolt` is not here anyway.

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
