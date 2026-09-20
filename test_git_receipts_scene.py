from __future__ import annotations

import ast
from pathlib import Path


SCENE_PATH = Path(__file__).with_name("git_receipts.py")


def test_scene_declares_an_original_receipt_explainer() -> None:
    source = SCENE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    assert "GitReceiptExplainer" in classes
    assert "from manim import" in source
    assert "Code SHA" in source
    assert "artifact hash" in source
    assert "git receipts" in source.lower()


def test_scene_is_configured_for_a_short_video() -> None:
    source = SCENE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    construct = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "construct"
    )
    assert len(construct.body) >= 5
    assert "config.frame_rate = 30" in source
    assert "run_time=2" in source or "run_time = 2" in source
