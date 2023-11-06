#!/usr/bin/python3
'''Starts a Flask web application
Displays:
        “Hello HBNB!” on route /
        “HBNB” on route /hbnb
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''home page display'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''hbnb page display'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
