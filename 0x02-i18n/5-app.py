#!/usr/bin/env python3
"""
Flask web application with a mocked user login system.

This application uses a mocked user table to simulate user login.
It displays a welcome message based on whether a user is logged in
or not, and handles locale and timezone information.
"""

from flask import Flask, render_template, request, g
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

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve a user based on the 'login_as' URL parameter.

    Returns:
        dict or None: The user dictionary if the user ID is valid,
                      otherwise None.
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    try:
        user_id = int(user_id)
    except ValueError:
        return None
    return users.get(user_id, None)


@app.before_request
def before_request():
    """
    Function to execute before each request.

    Sets the global variable g.user to the user retrieved
    by the get_user function, if any.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match language for the user's request.

    Returns:
        str: The locale that matches the user's request
             or the best match locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_locale():
    """
    Inject the get_locale function into the Jinja2 context.

    Returns:
        dict: A dictionary with the get_locale function
              available to templates.
    """
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """
    Render the index page.

    This route renders the 5-index.html template,
    which uses the get_locale function to display content
    in the appropriate language based on the user's preference.
    It also displays a message based on the login status.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
