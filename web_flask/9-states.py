#!/usr/bin/python3
'''
flask application
that can initiate cities by states
'''

from markupsafe import escape
from sqlalchemy.inspection import inspect
from os import getenv
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes storage on teardown"""
    storage.close()


@app.route(
    '/states',
    strict_slashes=False)
@app.route('/states/<stateId>', strict_slashes=False)
def states(stateId=None):
    states = list(storage.all(State).values())
    cities = list(storage.all(City).values())
    cities.sort(key=lambda x: x.name)
    states.sort(key=lambda x: x.name)

    if stateId is not None and stateId in states:
        stateId = f"State.{stateId}"
    elif stateId not in states:
        abort(404)

    return render_template(
        '9-states.html',
        states=states, cities=cities, stateId=stateId)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
