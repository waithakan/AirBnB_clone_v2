#!/usr/bin/python3
'''Starts a Flask web application
Displays:
        “Hello HBNB!” on route /
        “HBNB” on route /hbnb
        'C <text>' on route /c/<text>
        'Python <text>' on route /python/(<text>)
        '<n> is a number' on route /number/<n>
        'Number: <n>' on route /number_template/<n>
        'Number: <n> is even|odd' on route /number_odd_or_even/<n>
'''
from flask import Flask, escape, render_template

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


@app.route('/python/', strict_slashes=False,
           defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    '''python page display'''
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''numbers page display'''
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''number page that return rendered template'''
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numer_even_or_odd(n):
    """number page that return redered template
       that indicate if number is even or odd
    """
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
