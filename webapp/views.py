
from typing import Any
from flask import Flask, render_template, request, jsonify # type: ignore

from .solver import solve_for_variable, convert_equation, convert_variable

app = Flask(__name__)


@app.route('/') # type: ignore
def root():
    # type: () -> Any
    return render_template('index.html')


@app.route('/api/solve', methods=['POST']) # type: ignore
def api_solve():
    # type: () -> Any
    target = convert_variable(request.form.get('target'))
    equation = convert_equation(request.form.get('equation'))
    if equation is None or target is None:
        return jsonify({
            'success': False,
            'message': 'Must provide valid equation and target variable'
        })

    result = solve_for_variable(target, equation)
    return jsonify(result)
