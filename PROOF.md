# verisci: Proof Manifest

Every technical and research claim in this repository maps directly to a reproducible script, a ground-truth metric, or a verified test.

| Claim / Research Milestone | Artifact Link | Direct Verification Command | Status |
| :--- | :--- | :--- | :--- |
| **P1: Benchmark Harness Core** | `src/verisci/harness.py` | `uv run pytest` | 🟢 Active |
| **Dual-Pass CI Pipeline** | `.github/workflows/ci.yml` | `pytest tests/test_dual_pass.py` | 🟡 Pending |
| **JOSS 6-Month Clock Anchor** | GitHub Repository First Commit | `git log --reverse --oneline` | 🟢 Verified |
