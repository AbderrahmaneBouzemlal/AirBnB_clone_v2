#!/usr/bin/python3
"""
flask application that can initiate the route /

"""

from markupsafe import escape
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
states = list(storage.all(State).values())


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''The states_list page.'''
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', States=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
