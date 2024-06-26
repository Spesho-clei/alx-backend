#!/usr/bin/env python 3
"""Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/')
def index():
    """home/index page"""

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
