#!/usr/bin/env python3
"""
Flask app with Babel internationalization support.
Configures supported languages and default locale/timezone.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel.
    Defines supported languages, default locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
