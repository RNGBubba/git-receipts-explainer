# Git Receipts Explainer

## Offer

An original, silent Manim explainer showing how a commit, exact command, exit code, and artifact hash form a checkable Git receipt. The source is `git_receipts.py`; it contains all copy and visuals and uses no external media.

## Run

```bash
manim -pqh git_receipts.py GitReceiptExplainer
```

Manim is not installed in this worker environment, so the MP4 was not rendered here. The source is ready for a standard Manim installation. The scene is configured at 30 fps and is designed for approximately 30–45 seconds.

## Verification

```bash
python -m pytest -q test_git_receipts_scene.py
python -m py_compile git_receipts.py
```

The test suite checks the scene class, original explanatory copy, and short-video structure. No copyrighted music, lyrics, images, or footage are included.

## 30-day path

Publish the source as a free public example, then offer small custom auditability explainers for engineering teams at $75–$150 per original scene, with a human approving any commissioned copy before delivery.

## Human click

A human may need to install Manim and run the render command. Publishing to GitHub also requires the already-authenticated GitHub CLI session.

## Receipt

`receipts/` contains a DoneMeans receipt binding the verification command and its output artifact to the committed source SHA.

## GitHub

A new public repository URL is recorded here after publishing.
