#!/usr/bin/python3
'''Starts a Flask web application
Displays:
        “Hello HBNB!” on route /
        “HBNB” on route /hbnb
        'C <text>' on route /c/<text>
'''
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''home page display'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''hbnb page display'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''C page display'''
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
