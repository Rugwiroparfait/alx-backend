#!/usr/bin/env python3
"""
This is a simple Flask web application that demonstrates
the use of Flask-Babel for internationalization (i18n).
It renders an HTML template in the user's preferred language
based on the `Accept-Language` header of their request.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Configuration class for setting application languages and timezone."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match language from the user's request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Adding get_locale to the Jinja2 context
@app.context_processor
def inject_locale():
    """ get locale definition"""
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """Render the index template."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
