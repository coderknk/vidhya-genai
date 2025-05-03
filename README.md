# Analytics Vidhya GenAI Pinnacle - Automated Test Suite

This repository contains the automated test suite for the Analytics Vidhya GenAI Pinnacle Program webpage.

## Project Structure

- `pages/`  
  Contains Page Object Model classes for the GenAI Pinnacle page (locators and actions).

- `tests/frontend/`  
  Playwright (or Selenium) test scripts for frontend UI testing (pytest tests using page objects).

- `tests/backend/`  
  pytest scripts using `requests` to test API/HTTP endpoints (status codes and content).

- `requirements.txt`  
  Lists Python dependencies (e.g. `playwright`, `pytest`, `requests`).

- `README.md`  
  This documentation file.

## Installation

1. **Python Environment:** Ensure Python 3.8+ is installed.

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
