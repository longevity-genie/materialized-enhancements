# Roadmap

Open work only; an item is `## RM<n> — title` with its state and owner under it. Written 2026-11-24 from the
8 open issues, PR #27 and `docs/opengenes-*.md`. Toolchain on this machine: `uv sync` done, `uv run pytest`
650 passed / 10 skipped (14 min); `dolt` 2.7.7 in `~/.local/bin` (release binary; conda-forge has none); no pre-commit config
exists, so `CLAUDE.md` and `AGENTS.md` are kept identical by hand.

## RM5 — #16 validate the printable protein models

**State:** unattended
**Owner:** lead

`scripts/validate_stl.py` (2026-11-25) cross-checks the 75 report rows and 75 STL files against the database's PDB/UniProt ids. First run: 11 report rows have no gene and no gene uses their PDB id (5W21, 3HH2, 7S5H, 3F1P, 5F3B, 5UDZ, 8Y02, 9C5S, 5MEO, 5VAQ, 9QNG: orphan files, to delete or map; the maintainer's call, they are LFS-tracked); every STL file has a report row (the extra directory entries are not STLs); every model is reported not watertight (cartoon renders with many shells, expected, but a print check on one model with a slicer is still missing). Next: decide the orphans with the maintainer, then compare a few models with their PDB structure by eye (someone with a viewer).

## RM7 — OpenGenes wave 4: 130 never-reviewed genes

**State:** blocked: desk #93
**Owner:** lead

The brief's 8 input artifacts live in the maintainer's science session (not on this server), (`dolt` 2.7.7 is installed in `~/.local/bin` from the release binary, 2026-11-26). Desk #93: the maintainer supplies the files, or the wave is parked (default: parked).

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

## RM12 — Where pages are looked at

**State:** blocked: desk #87
**Owner:** lead

Needs the maintainer. Desk #87: no page is shown on this server; visual items stay "built, not viewed" until a way of looking is named.
