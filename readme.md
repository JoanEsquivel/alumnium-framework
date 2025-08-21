Alumnium baseline project

Overview

This is a minimal Python baseline to run browser automation with Alumnium. It uses:
- Selenium for driving the browser
- Alumnium for natural‑language actions and checks
- python‑dotenv to load environment variables from a .env file

Prerequisites

- Python 3.10+ installed (3.13 tested)
- Google Chrome installed (Selenium Manager will auto‑resolve the driver)

Quick start

1) Create and activate a virtual environment

macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```
pip install -r requirements.txt
```

Optional: Install Playwright browsers (some Alumnium features may use Playwright)
```
python -m playwright install chromium
```

3) Configure environment variables (.env)

Create a file named .env in the project root:
```
ALUMNIUM_MODEL=ollama
# Optionally, if you use external providers
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=...
# GOOGLE_API_KEY=...
```

Note: .env is already ignored by .gitignore.

4) Run the example
```
python test.py
```

What the example does

- Loads environment variables from .env
- Starts a Chrome browser
- Navigates to https://www.joanmedia.dev/
- Uses Alumnium to click on “conferences”, verifies a conference is listed, then prints the conferences list

Troubleshooting

- Chrome not found: Ensure Google Chrome is installed and on a supported version.
- Driver errors: Selenium 4.6+ uses Selenium Manager to fetch the correct driver automatically; update Selenium if needed.
- Environment variables not loading: Confirm the .env file is placed at the project root and that load_dotenv() is executed before usage.

Useful commands

- Upgrade pip: `python -m pip install --upgrade pip`
- Freeze current environment: `pip freeze > requirements.lock.txt`