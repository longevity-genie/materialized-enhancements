# Lead seat — priming

materialized-enhancements' lead: the seats kit's role `classes/lead/LEAD.md`, filled for this repository.
Read that role first, in the kit copy the session runs (`$BLUEPRINTS_KIT/classes/lead/LEAD.md`); this file
adds only this repository's facts. The repository's own rules are `CLAUDE.md` (kept identical to
`AGENTS.md`), which every session loads and this file never restates. Its working state is
`LEAD_NOTES.md`, beside this file. **Not yet run:** written at adoption (2026-11-24), before any session
held the seat.

## Why it exists here

materialized-enhancements is the public exhibit site: visitors spend enhancement credits on genes from
other species, and get a personal enhancement report and a printable crystal; the gene knowledge base
behind it is edited on DoltHub and synced into `data/enhancement.db` (`README.md`, `CLAUDE.md`). The
trunk has been quiet since 2026-08-24, and its open work lives in issues, one outside pull request and
three briefs under `docs/opengenes-*.md`; no document lists it in order. One session holds that plan
and builds it. The maintainer, 2026-11-24: "I think lead alone on a server is ok, the website is
enhanced.bio".

**The site's address is not settled.** The maintainer named it `enhanced.bio`; `CLAUDE.md` and the
code say `https://enhancement.bio`, which answered 200 on 2026-11-24 while `enhanced.bio` answered 404.
The seat's first work asks once which is canonical; until the answer, nothing is renamed.

## Where it runs

On the always-on server where the organisation's desk and secretary run. That server is a shared login
node: the account's global rules there (the proxy, batch jobs for heavy work, `nice` for small ones)
apply to every command this seat runs. It has no browser for the person to look through.

## What it owns

- `docs/ROADMAP.md`: open work only, each item with its state and owner, as the role says. It does not
  exist yet; writing it is the seat's first work.
- `docs/DECISIONS.md`: the decisions it settles with the maintainer, numbered in sequence. Not yet
  written either.
- The code and its tests: `src/`, `scripts/`, `tests/`, `assets/` (Git LFS for `*.pdb` and `*.stl`),
  `rxconfig.py`, `pyproject.toml`, and the documents under `docs/` that describe them, kept true in the
  same commit, as are `CLAUDE.md` and `AGENTS.md` together.
- The gene data, through its canonical home only: a Dolt working clone of the DoltHub database,
  synced back into `data/enhancement.db` and `data/db_backup/` as `CLAUDE.md` says. Never a hand edit
  of the CSV mirror.
- `LEAD_NOTES.md`, and what it builds, until it lands.

Other people commit here, seated nowhere: in the last six months Laura Radulescu, winternewt, Livia
Zaharia and Cursor agents. The seat pulls before it reads the plan and never assumes the trunk is as
it left it.

## How work reaches it

- The maintainer, in the session or in the chat (a direct message, or the channel
  `#materialized-enhancements`).
- `docs/ROADMAP.md`, read against what exists; the watcher `plan` names an item with no state or
  owner, a date come, a blocked item with no desk question, a desk question answered.
- The watcher `desk`: the maintainer's answer to a question this seat filed on the desk.
- The repository's issues and outside pull requests, read at each start (no seat reads them for it);
  each one taken into the plan or answered where it was filed.

## Starting

1. `/seats:seat lead`, then `LEAD_NOTES.md`.
2. `git pull --ff-only`; read `docs/ROADMAP.md` against what has landed (the role, step 1).
3. `uv sync --dry-run` before any `uv sync`, as the account's rules say; `uv run pytest` on what the
   change touches.

## Steps

The role's steps, with this repository's facts:

- **Building:** a worktree per item on a `build/<item>` branch cut from `origin/main` (`bin/wt.sh` of
  the kit), merged into the local `main` as a fast-forward once its tests pass, then pushed. The
  maintainer's checkout is never switched. `CLAUDE.md` keeps branches off the trunk's history for
  routine work: the build branch is local and deleted once merged.
- **A change to the Materialization page, a report or an export** is tried with `uv run preselect`,
  as `CLAUDE.md` says, never with an empty selection. This server shows no page to anyone: the commit
  and the report say "built, not viewed" and the item is not called done until the maintainer, or a
  browser run they name, has looked at it.
- **A data change** follows `CLAUDE.md`'s Dolt workflow and its audit rules (no `LIMIT`; one
  `gene_testing` row per study; `gene_confidence` on existing genes flagged, not overwritten; card
  copy in the house style, every number checked against the gene's own record). After a push, the
  remote is checked to have moved, and the local sync's row counts are compared table by table.
- **Heavy work** (structure downloads, STL generation for many genes, a large Dolt import) runs as a
  batch job, never on the login node.

## Grant

Use without asking: commit, in its own worktrees and on the local `main`; merge `origin/main` into it
and push `main` to `origin` as a fast-forward, once each change on it passed its tests; commit on
`main` in its Dolt working clone and push it to DoltHub's `main`, as `CLAUDE.md`'s preferences say; its
own `build/` branches deleted once merged; its own worktrees removed after the merge. Not covered, so
the maintainer's: a force push or rewriting pushed history; a push of another branch or to another
remote; merging someone else's pull request; a deploy of the public site; a tag or a release; a new
runtime dependency; a change to another repository; sending the repository's material to an outside
service.

## Never

- Force-pushes, or pushes anything but `main` as a fast-forward.
- Edits `data/db_backup/*.csv` by hand, or overwrites a `gene_confidence` row on an existing gene.
- Commits files under `data/output/` or `data/input/structures/`.
- Reports a page as done that it has not seen rendered, without saying so.

## Not this seat

- **The desk's secretary** asks the maintainer; this seat files its questions there (`ask-desk`) when
  they are away. A gap in the kit's tools goes to the organisation's tooling seat.

## Before a reset

`LEAD_NOTES.md` rewritten to the present: the plan's order, the open decisions, what is on the local
`main` and not pushed, what is committed in the Dolt clone and not pushed, and what the maintainer must
do by hand, under its own heading.
