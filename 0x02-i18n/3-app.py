#!/usr/bin/env python3
"""
Flask web application that uses Flask-Babel for internationalization (i18n).
It detects the user's preferred language from the request and serves the
HTML content in the corresponding language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    """Configuration class for supported languages and time zones."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match language from the user's request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_locale():
    """Inject the get_locale function into the Jinja2 context."""
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
