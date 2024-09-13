#!/usr/bin/env python3
"""
Flask web application that uses Flask-Babel for internationalization (i18n).
It detects the user's preferred language from the request and serves the
HTML content in the corresponding language based on the configured locales.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match language for the user's request.

    Uses the `Accept-Language` header from the request
    to select the most appropriate
    language from the supported languages list.

    Returns:
        str: The locale that matches the user's request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_locale():
    """
    Inject the `get_locale` function into the Jinja2 context.

    This allows templates to access the `get_locale` function
    to get the current locale.

    Returns:
        dict: A dictionary with the `get_locale` function
        available to templates.
    """
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """
    Render the index page.

    This route renders the `3-index.html` template, which uses
    the `get_locale` function
    to display content in the appropriate language based on the
    user's preference.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
