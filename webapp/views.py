
from typing import Any
from flask import Flask, render_template, request, jsonify

from main import is_prime, solve

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/solver/'


@app.route('/')
def root():
    # type: () -> Any
    return render_template('index.html')


@app.route('/api/is_prime', methods=['POST'])
def api_is_prime():
    # type: () -> Any
    return is_prime(request)


@app.route('/api/solve', methods=['POST'])
def api_solve():
    # type: () -> Any
    return solve(request)
