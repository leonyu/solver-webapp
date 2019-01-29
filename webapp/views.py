
from typing import Any
from flask import Flask, render_template, request, jsonify  # type: ignore

from utils.solver.solver import solve_for_variable, convert_equation, convert_variable
from utils.primality.fermat_primality import FermatPrimality

app = Flask(__name__)


@app.route('/')  # type: ignore
def root():
    # type: () -> Any
    return render_template('index.html')


@app.route('/api/is_prime', methods=['POST'])  # type: ignore
def api_is_prime():
    # type: () -> Any
    try:
        num = int(request.form.get('input'))
    except ValueError:
        pass

    if num is None:
        return jsonify({
            'success': False,
            'message': 'Must provide valid equation and target variable',
            'input': num
        })

    success, reason = FermatPrimality().is_prime(num)
    if success:
        solution = '{num} is a prime number'.format(num=num)
    else:
        solution = '{num} is NOT a prime number'.format(num=num)
    result = {
        'success': True,
        'input': num,
        'solutions': [solution],
        'message': reason,
    }
    return jsonify(result)


@app.route('/api/solve', methods=['POST'])  # type: ignore
def api_solve():
    # type: () -> Any
    equation = convert_equation(request.form.get('input'))
    target = convert_variable(request.form.get('target'))
    if equation is None or target is None:
        return jsonify({
            'success': False,
            'message': 'Must provide valid equation and target variable',
        })

    result = solve_for_variable(target, equation)
    return jsonify(result)
