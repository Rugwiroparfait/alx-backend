#!/usr/bin/env python3
"""
Flask web application with Flask-Babel for internationalization (i18n).
This application supports timezone selection via URL parameter and
determines the preferred timezone from the user's request or the URL.

It renders HTML content in the selected timezone and displays the current time.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError
from datetime import datetime

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
    Retrieve the user based on the 'login_as' URL parameter.

    Returns:
        dict or None: User dictionary if found, otherwise None.
    """
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Perform actions before handling each request,
    such as setting the user in `flask.g`.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match language for the user's request.

    This function first checks if a 'locale' parameter is present
    in the query string. If it is valid and supported, it returns that locale.
    Otherwise, it returns the locale from user settings or the best match
    locale based on the `Accept-Language` header from the request.

    Returns:
        str: The locale that matches the user's request
        or the best match locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Determine the best match timezone for the user's request.

    This function first checks if a 'timezone' parameter is present
    in the query string. If it is valid and supported,
    it returns that timezone.
    Otherwise, it returns the timezone from user settings or defaults to UTC.

    Returns:
        str: The timezone that matches the user's request
        or the default timezone.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


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

    This route renders the `index.html` template,
    which uses the `get_locale` and `get_timezone` functions
    to display content in the appropriate language and timezone
    based on the user's preference.

    Returns:
        str: The rendered HTML content for the index page.
    """
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=formatted_time)


if __name__ == '__main__':
    app.run(debug=True)
