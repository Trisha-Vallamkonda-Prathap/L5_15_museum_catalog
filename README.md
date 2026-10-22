# Lab 5: Static Code Analysis — Museum Artifact Catalog

**Your file:** `museum_catalog.py`

Follow the lab handout for the full instructions.

## About the program

A catalog for a museum collection. It registers artifacts with their era and value, moves items onto display, totals the value of a collection by era and runs a backup notice.

The code works, but only just. It has quality, style and security problems of the kind Pylint, Flake8 and Bandit are built to find.

## What to do

1. **Run it first** and read the output carefully:
   ```bash
   python museum_catalog.py
   ```
   It runs a short demonstration and may create a small output file in the current folder, so run it from a folder you don't mind adding files to.

2. **Install the tools:**
   ```bash
   pip install pylint bandit flake8
   ```

3. **Run the analysis** and save the reports:
   ```bash
   pylint museum_catalog.py > pylint_report.txt
   bandit -r museum_catalog.py > bandit_report.txt
   flake8 museum_catalog.py > flake8_report.txt
   ```

4. **Document the issues** in `issues.md` using this table (at least 4 rows, high and medium severity first):

   | Issue | Type | Line(s) | Description | Fix Approach |
   |-------|------|---------|-------------|--------------|
   | ... | ... | ... | ... | ... |

5. **Fix the code.** Fix at least 4 of the issues you documented, then rerun all three tools to confirm they are gone. Repeat until you are satisfied. The program should still do its job when you are done.

## Deliverables

1. `museum_catalog.py`: cleaned version achieving 10.00/10 Pylint score, 0 Bandit issues, and 0 Flake8 violations.
2. `test_museum_catalog.py`: unit test suite covering functionality and security edge cases.
3. `issues.md`: completed issue documentation table with 6 documented issues.
4. `reports/before/`: original baseline reports (`pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt`, `original_output.txt`).
5. `reports/after/`: verified post-fix reports demonstrating 0 findings and 10.00/10 score.

## How to Run & Verify

1. **Run the program:**
   ```bash
   python museum_catalog.py
   ```
2. **Run the automated unit tests:**
   ```bash
   python -m unittest test_museum_catalog.py
   ```
3. **Run Static Code Analyzers:**
   ```bash
   python -m pylint museum_catalog.py
   python -m bandit -r museum_catalog.py
   python -m flake8 museum_catalog.py
   ```

