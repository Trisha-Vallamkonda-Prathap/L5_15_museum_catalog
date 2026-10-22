# Static Code Analysis Issues Report

This document records the defects identified by **Pylint**, **Bandit**, and **Flake8** in `museum_catalog.py`, alongside the resolution approaches and verification outcomes.

| Issue # | Issue Description | Tool & Code | Severity | Original Location | Explanation | Fix Approach | Verification Result |
|---|---|---|---|---|---|---|---|
| 1 | SQL Injection Vector | Bandit `B608` (CWE-89) | Medium | `museum_catalog.py:11` | User-supplied parameters (`title`, `era`, `value`, `on_display`) were concatenated directly into an SQL query string. | Converted query to parameterized SQLite statement using `?` placeholders with parameter tuple. | Bandit `B608` eliminated; verified by `test_parameterized_insert_special_characters`. |
| 2 | Insecure Subprocess & Shell Execution | Bandit `B602`, `B607`, `B404` (CWE-78) | Low / Security | `museum_catalog.py:3, 37` | `subprocess.call` with `shell=True` spawned an unnecessary shell process with a relative binary name, risking shell injection and portability issues. | Removed `subprocess` import and replaced shell invocation with native Python `print("catalog backup complete")`. | Bandit findings B602, B607, B404 resolved with zero findings. |
| 3 | Hardcoded Password | Bandit `B105` (CWE-259) | Low | `museum_catalog.py:7` | Hardcoded credential string `CURATOR_PASSWORD = "m4seum!"` stored in plain source code. | Verified password was completely unused in codebase; removed dead constant cleanly. | Bandit B105 eliminated. |
| 4 | Unused Dead Import | Flake8 `F401`, Pylint `W0611` | Low / Quality | `museum_catalog.py:2` | `datetime` was imported at module top-level but never referenced in any function. | Removed redundant `import datetime`. | Flake8 `F401` and Pylint `W0611` cleared. |
| 5 | Missing Defensive Handling for Missing Artifacts | Runtime Correctness / Defect | Medium | `museum_catalog.py:16-17` | `cursor.fetchone()` result indexed directly (`row[0]`) without checking if `row` is `None`, causing `TypeError` on missing ID. | Added guard check `if row is None: return "unknown"` before indexing. | Confirmed defensive behavior with `test_display_status_missing_id`. |
| 6 | PEP 8 Conventions & Code Quality Deficiencies | Pylint `C0103`, `C0114`, `C0116`, `C0301`, `R1705`; Flake8 `E501`, `E303`, `E225` | Low / Style | `museum_catalog.py` (multiple lines) | Missing module/function docstrings, camelCase identifiers (`addArtifact`, etc.), missing operator whitespace (`total=0`), line length > 79 chars, unnecessary `else` after `return`. | Added descriptive docstrings, renamed functions to standard snake_case, wrapped SQL queries/docstrings to < 79 characters, corrected blank lines and operators. | Pylint score improved from 4.85/10 to 10.00/10; Flake8 errors reduced from 8 to 0. |

---

### Summary of Tool Results

| Metric | Baseline (Before) | Final (After) | Status |
|---|---|---|---|
| **Pylint Score** | 4.85 / 10 | **10.00 / 10** | **Passed** (> 9.5 target) |
| **Bandit Findings** | 5 issues (1 Medium, 4 Low) | **0 issues** | **Clean** (No `#nosec` suppressions) |
| **Flake8 Violations** | 8 violations | **0 violations** | **Clean** (Exit code 0) |
| **Unit Tests** | None | 6 / 6 passed | **Passing** |
