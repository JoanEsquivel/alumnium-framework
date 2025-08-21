# Alumnium Test Automation Framework

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Alumnium](https://img.shields.io/badge/alumnium-0.12.0-green.svg)](https://pypi.org/project/alumnium/)

A comprehensive test automation framework leveraging **Alumnium** for AI-powered browser testing with natural language commands. This project demonstrates how to write maintainable, readable tests using both Selenium and Playwright drivers.

## 🚀 Features

- **Natural Language Testing**: Write tests using plain English commands
- **Multi-Driver Support**: Compatible with both Selenium and Playwright
- **AI-Powered Assertions**: Intelligent verification using Alumnium's AI capabilities
- **Environment Configuration**: Flexible setup with environment variables
- **Cross-Platform**: Works on macOS, Linux, and Windows

## 📋 Prerequisites

- **Python 3.10+** (Python 3.13 tested and recommended)
- **Google Chrome** browser installed
- **Git** for cloning the repository

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd alumnium
```

### 2. Set Up Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers (Optional)

For Playwright-based tests, install the required browsers:

```bash
python -m playwright install chromium
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
ALUMNIUM_MODEL=ollama
# Optional: External AI providers
# OPENAI_API_KEY=sk-your-key-here
# ANTHROPIC_API_KEY=your-key-here
# GOOGLE_API_KEY=your-key-here
```

> **Note**: The `.env` file is automatically ignored by Git for security.

## 🎯 Usage

### Running Selenium Tests

Execute the Selenium-based test example:

```bash
python test_selenium.py
```

This test will:
- Navigate to https://www.joanmedia.dev/
- Click on the "conferences" section
- Verify conference listings
- Extract and display conference information

### Running Playwright Tests

Execute the Playwright-based test suite:

```bash
python -m unittest test_playwright.py
```

This test demonstrates:
- TodoMVC application testing
- Adding multiple todo items
- Bulk task completion
- State verification using natural language assertions

### Test Structure

#### Selenium Example (`test_selenium.py`)
```python
# Simple script demonstrating Alumnium with Selenium WebDriver
al = Alumni(driver)
al.do("click on 'conferences'")
al.check("conference list contain PyCon US 2025")
conferences = al.get('list of conferences')
```

#### Playwright Example (`test_playwright.py`)
```python
# Unit test structure with setUp and tearDown
class TestSearch(unittest.TestCase):
    def setUp(self):
        # Initialize Playwright and Alumnium
        
    def test_complete_all_todos(self):
        # Natural language test steps
        self.al.do("add 'buy some milk' to the todo list")
        self.al.check("task 'buy some milk' is completed")
```

## 📁 Project Structure

```
alumnium/
├── readme.md           # This documentation
├── requirements.txt    # Python dependencies
├── test_selenium.py    # Selenium WebDriver example
├── test_playwright.py  # Playwright test suite
└── .env               # Environment configuration (create this)
```

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `alumnium` | 0.12.0 | AI-powered test automation framework |
| `python-dotenv` | ≥1.0.1 | Environment variable management |

## 🐛 Troubleshooting

### Common Issues

**Chrome Browser Not Found**
- Ensure Google Chrome is installed and up to date
- Verify Chrome is in your system's PATH

**Driver Compatibility Issues**
- Selenium 4.6+ includes automatic driver management
- Update Selenium if experiencing driver-related errors:
  ```bash
  pip install --upgrade selenium
  ```

**Environment Variables Not Loading**
- Verify `.env` file exists in the project root
- Ensure `load_dotenv()` is called before using Alumnium
- Check for typos in environment variable names

**Playwright Installation Issues**
- Run `python -m playwright install --help` for installation options
- Ensure sufficient disk space for browser downloads

## 🚀 Advanced Usage

### Custom AI Models

Configure different AI providers in your `.env` file:

```env
# Use OpenAI
ALUMNIUM_MODEL=openai
OPENAI_API_KEY=your-openai-key

# Use Anthropic Claude
ALUMNIUM_MODEL=anthropic
ANTHROPIC_API_KEY=your-anthropic-key

# Use local Ollama (default)
ALUMNIUM_MODEL=ollama
```

### Extending Tests

Create additional test files following the established patterns:

1. Import required modules (`alumnium`, `selenium`/`playwright`, `dotenv`)
2. Load environment variables with `load_dotenv()`
3. Initialize your driver and Alumnium instance
4. Write tests using natural language commands

## 📚 Useful Commands

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Freeze current environment
pip freeze > requirements.lock.txt

# Run tests with verbose output
python -m unittest test_playwright.py -v

# Check Python version
python --version
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is provided as-is for educational and testing purposes.

---

For more information about Alumnium, visit the [official documentation](https://pypi.org/project/alumnium/).