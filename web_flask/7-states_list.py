#!/usr/bin/python3
"""
Flask application listens port :5000
"""
from flask import Flask
from models import storage
from flask import render_template
from models import *

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
