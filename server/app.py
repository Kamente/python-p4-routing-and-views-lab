#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return f'<h1>Printed String: {text}</h1>'


@app.route('/<int:count>')
def count(count):
    return f'<h1>Count here {count}</h1>'


@app.route('/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    return f'<h1>Your answer is {result}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
