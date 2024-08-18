#!/usr/bin/python3
'''
flask application
that can initiate cities by states
'''

from markupsafe import escape
from sqlalchemy.inspection import inspect
from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes storage on teardown"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    dictionary = {}
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    cities = list(storage.all(City).values())
    cities.sort(key=lambda x:x.name)
    return render_template('8-cities_by_states.html', states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

