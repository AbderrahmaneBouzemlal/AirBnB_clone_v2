#!/usr/bin/python3
"""
Flask web application
"""

from markupsafe import escape
from sqlalchemy.inspection import inspect
from os import getenv
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes storage on teardown"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)