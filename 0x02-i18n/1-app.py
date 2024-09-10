#!/usr/bin/env python3
"""
Flask app with Babel setup for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app.
    Sets available languages and default settings.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)


@app.route('/')
def index():
    """
    Route for the home page.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
