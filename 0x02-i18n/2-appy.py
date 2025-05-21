#!/usr/bin/env python3
"""
Flask app with Babel for i18n.
Selects locale based on request headers.
"""

from flask import Flask, request, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration for Babel.
    Sets supported languages and default locale/timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Select the best matching language based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
