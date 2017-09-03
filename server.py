#!/usr/bin/env python

import os
from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

# Jinja will raise an error instead of failing with any undefined variables:
app.jinja_env.undefined = StrictUndefined


@app.route("/", methods=["GET"])
def get_index():
    """Show index."""

    return render_template("index.html")


@app.route("/read-file.json", methods=["GET"])
def read_file():
    """Read contents of file."""
    with open('data/temp.txt', 'r') as file:
        value = file.read().strip()

    return value


if __name__ == "__main__":
    import os

    DEBUG = "DEBUG" in os.environ
    app.run(host="0.0.0.0", port=5000, debug=DEBUG)
