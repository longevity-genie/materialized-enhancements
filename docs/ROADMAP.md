# Roadmap

Open work only. Each item has a state and an owner (`lead` unless noted). States: `unattended` (decided, built
when nothing blocks), `urgent`, `blocked: desk #N`, `waits until <date>`, `needs decision` (goes to the
maintainer as one batch with a default). Written 2026-11-24 from the 8 open issues, PR #27 and `docs/opengenes-*.md`.

## Decided, to build

| # | item | state | notes |
|---|---|---|---|
| R1 | PR #27 "Hint for fast removal" (LauraR20, 2026-07-13) | review: lead; merge: maintainer | 34+18 lines in `pages/index.py`, `state.py`; review, then ask the maintainer to merge |
| R2 | #25 fold a category back up | unattended | a collapse button on an open category; UI, built not viewed |
| R3 | #24 icons still active during the intro tutorial | unattended | UI, built not viewed |
| R4 | #15 mobile: one-column layout | unattended | the maintainer's own issue; UI, built not viewed |
| R5 | #16 validate the 3D-printable protein models | unattended | extend `tests/dump_stl_diagnostics.py` and `assets/stl/stl_report.csv` (watertight, difficulty); batch job if heavy |
| R6 | OpenGenes: ruling items B and C of `opengenes-open-issues.md` (8 pre-existing directionality defects, `bub1b_t23`) | needs decision | rule: flag, never edit `gene_confidence` on existing genes; read each against the database first |
| R7 | OpenGenes wave 4: 130 never-reviewed genes | blocked: dolt not on PATH; artifacts named in the brief are outside this repo | brief's inputs (`{{artifact:...}}`) must be found or rebuilt first |

## For the maintainer, one batch, each with the lead's default

| # | item | default |
|---|---|---|
| Q1 | #13 gene interaction scores (stamina +5, charisma −4) | no: it changes the budget and sculpture model; park until the game design is settled |
| Q2 | #17 custom builds (class presets) | yes, after R2–R4: presets as data in the database, no code table |
| Q3 | #19 intro video (AI-generated, skippable) | maintainer or a volunteer makes the clip; lead builds the skippable player |
| Q4 | #20 UX review "think like a tester" | lead writes a list of findings from the code; each goes to the plan on the maintainer's pick |
| Q5 | where pages are looked at | none on this server: visual items stay "built, not viewed" until a browser run is named |

## Toolchain facts

- `uv sync` done on this machine (2026-11-24); `uv run pytest` was started, result recorded in `LEAD_NOTES.md`.
- `dolt` is not on the PATH (`pixi global install dolt` would add it); no Dolt push has been tried.
- No `.pre-commit-config.yaml` exists although `CLAUDE.md` names a hook: `CLAUDE.md` and `AGENTS.md` are kept identical by hand.
