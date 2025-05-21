#!/usr/bin/env python3
"""
Basic Flask app module.
Defines a single route that renders a welcome page.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
