#!/usr/bin/python3
"""
flask application that can initiate the route /

"""

from markupsafe import escape
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route(
    '/python/',
    defaults={'text': 'is_cool'},
    strict_slashes=False
    )
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route("/number_template/<int:num>", strict_slashes=False)
def number_template(num):
    return render_template('5-number.html', nums=num)


@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def number_odd_or_even(num):
    return render_template('6-number_odd_or_even.html', nums=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
