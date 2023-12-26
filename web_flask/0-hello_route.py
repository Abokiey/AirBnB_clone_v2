#!/usr/bin/python3
""" minimal flask application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """string to print"""
    return "Hello HBNB!"


if __name__ == "__man__":
    app.run(host='0.0.0.0', port=5000)
