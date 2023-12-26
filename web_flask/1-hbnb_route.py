#!/usr/bin/python3
"""start web application with flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """text to display"""
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """text to display"""
    return ('HBNB')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
