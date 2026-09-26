# SauceDemo QA Automation Framework

[![Automation Tests](https://github.com/MedinaAle20/saucedemo-qa-automation-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/MedinaAle20/saucedemo-qa-automation-framework/actions/workflows/tests.yml)

## Overview

Python QA automation project covering critical UI flows in [SauceDemo](https://www.saucedemo.com/) and basic API contract checks against [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

The framework keeps Selenium interactions inside page objects, separates UI and API suites, loads test data from JSON and runs in headless mode through GitHub Actions.

## Stack

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- GitHub Actions
- Page Object Model

## Architecture

```text
tests/ui/ ──→ pages/ ──→ Selenium WebDriver ──→ SauceDemo
tests/api/ ─→ Requests ───────────────────────→ JSONPlaceholder
                  ↑
             data/users.json

conftest.py ─→ fixtures, browser lifecycle, logs and failure screenshots
```

```text
.
├── .github/workflows/tests.yml
├── conftest.py
├── data/users.json
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
├── tests/
│   ├── api/test_jsonplaceholder_api.py
│   └── ui/test_saucedemo_ui.py
├── utils/helpers.py
└── requirements.txt
```

## Automated coverage

### UI

- Successful login
- Invalid and locked-user login responses
- Product catalog names, count and price format
- Adding selected products to the cart
- End-to-end checkout
- Side-menu options and logout

### API

- `GET /users`: status and response shape
- `POST /users`: status and returned payload
- `DELETE /users/1`: status contract

The API suite validates the public JSONPlaceholder service; it is intentionally separate from SauceDemo because SauceDemo does not expose a public test API for these checks.

## Running the tests

Create and activate a virtual environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run a specific suite:

```bash
pytest tests/ui --headless
pytest tests/api
```

Generate a local HTML report:

```bash
pytest --headless --html=reports/reporte.html --self-contained-html
```

Chrome must be available for the UI suite. Selenium Manager resolves the compatible driver.

## CI

The workflow in [`.github/workflows/tests.yml`](./.github/workflows/tests.yml) runs on pushes and pull requests targeting `master` or `main`.

It:

1. installs Python 3.12 and the project dependencies;
2. executes all tests in headless mode;
3. generates a self-contained Pytest HTML report;
4. uploads the report as the `pytest-html-report` workflow artifact, even when a test fails.

## Evidence and generated artifacts

- HTML reports are generated locally or by CI and are not versioned.
- Execution logs are generated at `reports/logs/ejecucion.log` and are not versioned.
- UI failures create timestamped screenshots under `reports/screenshots/`.
- The CI run and its downloadable HTML artifact provide the reproducible execution record.

Generated reports and logs were removed from source control so GitHub language detection represents the Python codebase instead of temporary HTML output.

## Test data

[`data/users.json`](./data/users.json) contains the public SauceDemo demo credentials, invalid-user cases, checkout data and expected catalog products. It contains no private account credential.

## Design choices

- Page Object Model separates browser interactions from assertions.
- Explicit waits reduce timing-dependent UI failures.
- UI and API suites can run independently.
- Shared fixtures manage browser lifecycle and external test data.
- Failed UI tests capture screenshots without changing test outcomes.

