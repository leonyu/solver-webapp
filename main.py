
from flask import jsonify, Request
from typing import List, Dict, Any

from utils.solver.solver import solve_for_variable, convert_equation, convert_variable
from utils.primality.fermat_primality import FermatPrimality

def is_prime(req):
    # type: (Request) -> Any
    try:
        num = int(str(req.values.get('input')))
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

def solve(req):
    # type: (Request) -> Any
    equation = convert_equation(str(req.values.get('input')))
    target = convert_variable(str(req.values.get('target')))
    if equation is None or target is None:
        return jsonify({
            'success': False,
            'message': 'Must provide valid equation and target variable',
        })

    result = solve_for_variable(target, equation)
    return jsonify(result)
