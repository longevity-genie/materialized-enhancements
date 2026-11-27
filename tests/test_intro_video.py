"""Skippable intro clip (#19): rendered only when the clip file exists, and always with a skip control."""

from __future__ import annotations

from pathlib import Path

import pytest
import reflex as rx

from materialized_enhancements.pages import index


def test_no_clip_no_overlay(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(index, "_INTRO_VIDEO_DIR", tmp_path)
    assert type(index._intro_video_overlay()) is type(rx.fragment())


def test_clip_present_renders_a_skippable_player(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (tmp_path / "intro.mp4").write_bytes(b"not really a video")
    monkeypatch.setattr(index, "_INTRO_VIDEO_DIR", tmp_path)
    component = index._intro_video_overlay()
    assert type(component) is not type(rx.fragment())
    rendered = str(component.render())
    assert "/intro/intro.mp4" in rendered
    assert "Skip intro" in rendered and "Escape" in rendered
    assert "me_intro_seen" in rendered
