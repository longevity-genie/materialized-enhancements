"""Cross-check the printable protein STLs against the report and the gene database (issue #16).

Cheap checks, no mesh loading: every STL file has a report row, every report row has a file, each
row's gene and PDB/UniProt ids match ``gene_properties`` in ``data/enhancement.db``, and the
printability numbers in ``stl_report.csv`` stay inside limits. It validates the *records*; whether a
printed model really shows the right fold still needs a person (or the AlphaFold/RCSB structure) to
compare it with the structure.

Run:  uv run python scripts/validate_stl.py            # print findings, write the CSV
      uv run python scripts/validate_stl.py --strict   # exit 1 when any finding remains
"""

import csv
import logging
import sqlite3
from pathlib import Path

import typer

REPO = Path(__file__).resolve().parents[1]
STL_DIR = REPO / "assets" / "stl"
REPORT = STL_DIR / "stl_report.csv"
DB = REPO / "data" / "enhancement.db"
OUT = REPO / "data" / "output" / "stl_validation.csv"

MAX_PRINT_MM = 180.0
MAX_TINY_SHELLS = 20
MAX_ASPECT = 6.0

logger = logging.getLogger("validate_stl")
app = typer.Typer(add_completion=False, help=__doc__)


def load_db_properties(db: Path) -> dict[str, dict[str, str]]:
    """gene_id -> its protein ids from gene_properties."""
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT gene_id, gene, protein_id, pdb_id FROM gene_properties").fetchall()
    conn.close()
    return {r["gene_id"]: {k: (r[k] or "") for k in ("gene", "protein_id", "pdb_id")} for r in rows}


def validate(report: Path, stl_dir: Path, props: dict[str, dict[str, str]]) -> list[tuple[str, str, str]]:
    """Findings as (file or gene_id, check, detail)."""
    findings: list[tuple[str, str, str]] = []
    with report.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    files = {p.name for p in stl_dir.glob("*.stl")}
    listed = {r["file"] for r in rows}
    for name in sorted(files - listed):
        findings.append((name, "file_without_report_row", "STL exists, no row in stl_report.csv"))
    for name in sorted(listed - files):
        findings.append((name, "report_row_without_file", "row in stl_report.csv, no STL file"))
    seen_genes: dict[str, str] = {}
    for r in rows:
        name, gene_id = r["file"], r["gene_id"]
        if not gene_id:
            findings.append((name, "row_without_gene", "empty gene_id/gene/category in the report row"))
            continue
        if gene_id in seen_genes:
            findings.append((name, "gene_has_two_files", f"{gene_id} also has {seen_genes[gene_id]}"))
        seen_genes[gene_id] = name
        db = props.get(gene_id)
        if db is None:
            findings.append((name, "gene_not_in_db", f"{gene_id} has no gene_properties row"))
            continue
        if r["structure_source"] == "rcsb" and db["pdb_id"] and r["pdb_id"] != db["pdb_id"]:
            findings.append((name, "pdb_mismatch", f"report {r['pdb_id']} vs database {db['pdb_id']}"))
        if db["protein_id"] and r["protein_id"] and r["protein_id"] != db["protein_id"]:
            findings.append((name, "protein_id_mismatch", f"report {r['protein_id']} vs database {db['protein_id']}"))
        if r["max_dim_mm"] and float(r["max_dim_mm"]) > MAX_PRINT_MM + 0.5:
            findings.append((name, "too_large", f"max dimension {r['max_dim_mm']} mm > {MAX_PRINT_MM:.0f}"))
        if int(r["tiny_shells"] or 0) > MAX_TINY_SHELLS:
            findings.append((name, "many_tiny_shells", f"{r['tiny_shells']} shells under 20 faces"))
        if r["aspect_ratio"] and float(r["aspect_ratio"]) > MAX_ASPECT:
            findings.append((name, "extreme_aspect_ratio", f"aspect ratio {r['aspect_ratio']}"))
        if r["watertight"].lower() != "true":
            findings.append((name, "not_watertight", f"{r['shells']} shells, difficulty {r['difficulty']}"))
    return findings


@app.command()
def main(
    report: Path = typer.Option(REPORT, help="stl_report.csv"),
    stl_dir: Path = typer.Option(STL_DIR, help="Folder with the STL files"),
    db: Path = typer.Option(DB, help="SQLite gene database"),
    out: Path = typer.Option(OUT, help="Where to write the findings CSV"),
    strict: bool = typer.Option(False, help="Exit 1 when any finding remains"),
) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    findings = validate(report, stl_dir, load_db_properties(db))
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["subject", "check", "detail"])
        writer.writerows(findings)
    counts: dict[str, int] = {}
    for _, check, _ in findings:
        counts[check] = counts.get(check, 0) + 1
    for check, n in sorted(counts.items()):
        logger.info("%5d  %s", n, check)
    logger.info("%d findings -> %s", len(findings), out)
    if strict and findings:
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
