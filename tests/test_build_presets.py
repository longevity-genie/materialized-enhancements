"""Class presets / custom builds (#17): loaded from the database, applied through the compose state."""

from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from materialized_enhancements import gene_data
from materialized_enhancements.state import ComposeState

MIGRATION = Path(__file__).resolve().parents[1] / "data" / "dolt_migrations" / "001_build_presets.sql"


def _db_with_presets(tmp_path: Path) -> Path:
    db = tmp_path / "enhancement.db"
    shutil.copy(gene_data.DB_PATH, db)
    sql = MIGRATION.read_text().replace("INT NOT NULL", "INTEGER NOT NULL")
    conn = sqlite3.connect(db)
    conn.executescript(sql)
    conn.commit()
    conn.close()
    return db


def test_presets_load_from_the_migration_tables(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(gene_data, "DB_PATH", _db_with_presets(tmp_path))
    presets = gene_data._load_build_presets()
    assert [p["preset_id"] for p in presets] == ["guardian", "regenerator", "survivor"]
    assert all(g in gene_data.PLAYABLE_GENE_NAMES for p in presets for g in p["genes"])
    cost = {p["preset_id"]: sum(gene_data.GENE_PRICES[g] for g in p["genes"]) for p in presets}
    assert all(0 < c <= gene_data.DEFAULT_BUDGET for c in cost.values()), cost


def test_no_preset_tables_means_no_presets(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db = tmp_path / "plain.db"
    shutil.copy(gene_data.DB_PATH, db)
    conn = sqlite3.connect(db)
    conn.execute("DROP TABLE IF EXISTS build_preset_genes")
    conn.execute("DROP TABLE IF EXISTS build_presets")
    conn.commit()
    conn.close()
    monkeypatch.setattr(gene_data, "DB_PATH", db)
    assert gene_data._load_build_presets() == []


def test_apply_preset_replaces_the_loadout(monkeypatch: pytest.MonkeyPatch) -> None:
    gene = gene_data.GAME_GENE_LIBRARY[0]
    preset = {"preset_id": "p", "name": "P", "description": "", "genes": [gene["gene"]]}
    monkeypatch.setattr("materialized_enhancements.state.BUILD_PRESETS", [preset])
    state: Any = SimpleNamespace(
        included_genes=["old"], selected_categories=["old"], gene_library_open_category="x", recomputed=0
    )
    state._recompute_params = lambda: setattr(state, "recomputed", state.recomputed + 1)
    ComposeState.apply_preset.fn(state, "p")
    assert state.included_genes == [gene["gene"]]
    assert state.selected_categories == [gene["category"]]
    assert state.recomputed == 1
    ComposeState.apply_preset.fn(state, "missing")
    assert state.included_genes == [gene["gene"]]
