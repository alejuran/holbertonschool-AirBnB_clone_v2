#!/usr/bin/python3
"""
Before using Flask to display our HBNB data,
you will need to update some part of our engine:
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page: (inside the tag BODY)
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(error):
    """
    closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
