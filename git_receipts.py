"""Original Manim explainer: why a Git receipt makes a result auditable.

Render with:
    manim -pqh git_receipts.py GitReceiptExplainer

The scene uses only Manim primitives and original copy; no external media.
"""

from manim import (
    Arrow,
    BLUE,
    DARK_GRAY,
    GREEN,
    ORANGE,
    RED,
    WHITE,
    YELLOW,
    Code,
    Create,
    FadeIn,
    FadeOut,
    GrowArrow,
    Rectangle,
    Scene,
    Text,
    VGroup,
    Write,
    config,
)

config.frame_rate = 30


class GitReceiptExplainer(Scene):
    """A 30–60 second visual explanation of a receipt-backed change."""

    def construct(self) -> None:
        title = Text("Git receipts: proof, not promises", color=WHITE).scale(0.72)
        subtitle = Text("A small record that makes work reproducible", color=BLUE).scale(0.38)
        subtitle.next_to(title, direction=(0, -1, 0), buff=0.25)
        self.play(Write(title), FadeIn(subtitle), run_time=2)
        self.wait(1)

        commit = self._card("1. CHANGE", "commit\nCode SHA", YELLOW)
        command = self._card("2. RUN", "exact command\nexit code", ORANGE)
        artifact = self._card("3. SAVE", "artifact\nbytes + hash", GREEN)
        flow = VGroup(commit, command, artifact).arrange(direction=(1, 0, 0), buff=0.55)
        flow.scale(0.78).move_to((0, -0.25, 0))
        arrows = VGroup(
            Arrow(commit.get_right(), command.get_left(), buff=0.12, color=WHITE),
            Arrow(command.get_right(), artifact.get_left(), buff=0.12, color=WHITE),
        )
        self.play(FadeOut(title), FadeOut(subtitle), FadeIn(commit), run_time=1)
        self.play(FadeIn(command), FadeIn(artifact), GrowArrow(arrows[0]), run_time=2)
        self.play(GrowArrow(arrows[1]), run_time=1)
        self.wait(1)

        receipt_title = Text("receipt.json", color=GREEN).scale(0.55)
        receipt_title.to_edge((0, 1, 0), buff=0.55)
        receipt_lines = VGroup(
            Text('"code_sha": "a1b2c3d..."', color=YELLOW).scale(0.34),
            Text('"command": "pytest -q"', color=WHITE).scale(0.34),
            Text('"exit_code": 0', color=GREEN).scale(0.34),
            Text('"artifact": {"bytes": 1842}', color=ORANGE).scale(0.34),
            Text('"sha256": "verified"', color=BLUE).scale(0.34),
        ).arrange(direction=(0, -1, 0), aligned_edge=(-1, 0, 0), buff=0.14)
        receipt_lines.next_to(receipt_title, direction=(0, -1, 0), buff=0.35)
        panel = Rectangle(width=6.2, height=3.5, color=DARK_GRAY, fill_opacity=0.25)
        panel.move_to(receipt_lines.get_center())
        self.play(FadeOut(flow), FadeOut(arrows), FadeIn(panel), Write(receipt_title), run_time=2)
        for line in receipt_lines:
            self.play(Write(line), run_time=1)
        self.wait(1)

        verify = Text("Anyone can verify the artifact hash.", color=GREEN).scale(0.52)
        verify.next_to(panel, direction=(0, -1, 0), buff=0.45)
        check = Text("PASS", color=GREEN).scale(0.6)
        check.next_to(verify, direction=(1, 0, 0), buff=0.35)
        self.play(FadeIn(verify), FadeIn(check), run_time=2)
        self.wait(2)

        close = Text("A receipt turns a claim into a checkable result.", color=WHITE).scale(0.52)
        close.move_to((0, 0, 0))
        self.play(FadeOut(panel), FadeOut(receipt_title), FadeOut(receipt_lines), FadeOut(verify), FadeOut(check), FadeIn(close), run_time=2)
        self.wait(3)
        self.play(FadeOut(close), run_time=1)

    @staticmethod
    def _card(label: str, body: str, color) -> VGroup:
        box = Rectangle(width=2.35, height=1.55, color=color, fill_opacity=0.15)
        heading = Text(label, color=color).scale(0.28)
        content = Text(body, color=WHITE).scale(0.32)
        content.next_to(heading, direction=(0, -1, 0), buff=0.2)
        return VGroup(box, heading, content)
