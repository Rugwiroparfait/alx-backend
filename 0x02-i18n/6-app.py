#!/usr/bin/env python3
"""
Flask web application that uses Flask-Babel for internationalization (i18n).
This application supports language selection and user login emulation.
The locale priority order is URL parameters, user settings, request headers, and default locale.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configuration class for supported languages and time zones."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determine the best match language for the user's request.

    Returns:
        str: The locale that matches the URL parameters, user settings, request header, or the default locale.
    """
    # Check for 'locale' parameter in query string
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Check the request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.context_processor
def inject_locale():
    """Inject the get_locale function into the Jinja2 context."""
    return dict(get_locale=get_locale)

def get_user():
    """
    Retrieve a user based on the 'login_as' URL parameter.

    Returns:
        dict or None: The user dictionary if the user ID is valid, otherwise None.
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    user_id = int(user_id)
    return users.get(user_id, None)

@app.before_request
def before_request():
    """Set g.user to the user retrieved by get_user."""
    g.user = get_user()

@app.route('/')
def index():
    """Render the index page."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(debug=True)
