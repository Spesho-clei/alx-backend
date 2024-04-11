#!/usr/bin/env python 3
"""Basic Flask App"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """home/index page"""

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
