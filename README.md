# QA Automation Framework

A Playwright + Python test automation framework built with Page Object Model (POM) architecture.

## Tech Stack
- Python 3.12
- Playwright
- pytest
- pytest-html

## Project Structure

| File/Folder | Description |
|---|---|
| `config/environments.py` | Environment config and URLs |
| `pages/login_page.py` | Page Object Models |
| `tests/test_login.py` | Test suites |
| `utils/helpers.py` | Reusable helper functions |
| `base_test.py` | Base test class |
| `conftest.py` | pytest fixtures |
| `requirements.txt` | Dependencies |
| `reports/` | Generated HTML reports |

## Setup
1. Clone the repo

2. Create a virtual environment:
```
bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
bash
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

Run all tests:
```
bash
pytest -v
```

Run with HTML report:
```
bash
pytest -v --html=reports/report.html --self-contained-html
```

Run against a specific environment:
```
bash
pytest --env staging -v
```

## Test Coverage
- Valid login
- Invalid password
- Empty username
- Locked out user
