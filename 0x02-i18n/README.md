# 0x02. i18n

## Overview
This project focuses on implementing internationalization (i18n) in a Flask application using Flask-Babel. It involves setting up language localization, parametric templates, user-based locale settings, and timezone handling.

## Tasks

### Task 0: Basic Flask App
- **Objective:** Set up a basic Flask app.
- **Files:**
  - `0-app.py`: Basic Flask app with a single route `/`.
  - `templates/0-index.html`: Outputs "Welcome to Holberton" as `<title>` and "Hello world" as `<h1>`.

### Task 1: Basic Babel Setup
- **Objective:** Set up Babel for Flask.
- **Instructions:**
  - Install Flask-Babel (`flask_babel==2.0.0`).
  - Instantiate Babel in the app.
  - Create a `Config` class with `LANGUAGES = ["en", "fr"]`.
  - Set default locale (`en`) and timezone (`UTC`).
- **Files:**
  - `1-app.py`
  - `templates/1-index.html`

### Task 2: Get Locale from Request
- **Objective:** Implement a `get_locale` function to select the best language based on the request.
- **Files:**
  - `2-app.py`
  - `templates/2-index.html`

### Task 3: Parametrize Templates
- **Objective:** Use the `_` or `gettext` function to parametrize templates.
- **Instructions:**
  - Create a `babel.cfg` file for translation extraction.
  - Use `pybabel` to initialize translations for English and French.
  - Provide translations for `home_title` and `home_header`.
- **Files:**
  - `3-app.py`
  - `babel.cfg`
  - `templates/3-index.html`
  - Translations: `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`

### Task 4: Force Locale with URL Parameter
- **Objective:** Allow forcing a locale using a URL parameter (`locale=fr`).
- **Instructions:** Update `get_locale` to check for the `locale` parameter.
- **Files:**
  - `4-app.py`
  - `templates/4-index.html`

### Task 5: Mock Logging In
- **Objective:** Simulate a user login system.
- **Instructions:**
  - Create a mock user table.
  - Use the `before_request` function to mock user login with a `login_as` URL parameter.
  - Display a login message if the user is logged in.
- **Files:**
  - `5-app.py`
  - `templates/5-index.html`

### Task 6: Use User Locale
- **Objective:** Modify `get_locale` to prioritize locale settings from user preferences, URL parameters, and request headers.
- **Files:**
  - `6-app.py`
  - `templates/6-index.html`

### Task 7: Infer Appropriate Time Zone
- **Objective:** Implement a `get_timezone` function to handle time zone localization.
- **Instructions:** 
  - Time zone should be set from URL parameters, user settings, or default to `UTC`.
  - Validate time zones using `pytz.timezone`.
- **Files:**
  - `7-app.py`
  - `templates/7-index.html`

## Requirements
- Python 3.7
- Flask, Flask-Babel, pytz
- Code style: `pycodestyle`