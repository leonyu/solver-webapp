
import os
from typing import List, Dict
from sympy import symbols, Eq, sympify, Symbol, solve
from flask import Flask, url_for, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.urandom(16)


def convert_variable(input: str) -> Symbol:
    if not input or input.isspace():
        return None
    try:
        return symbols(input)
    except:
        return None

def convert_equation(input: str) -> Eq:
    if not input or input.isspace():
        return None
    lineSplit = input.split('=')
    if len(lineSplit) != 2:
        return None # raise Exception('Line does not contain a valid equation')
    lhs = lineSplit[0].strip()
    rhs = lineSplit[1].strip()
    if not lhs or not rhs:
        return None # raise Exception('LHS and RHS of an equation must not be empty')
    return Eq(sympify(lhs), sympify(rhs))

def create_solution_json(equation: Eq, target: Symbol, solution: list) -> Dict:
    print(type(solution))
    equation_text = str(equation)
    variable_text = str(target)
    solution_list = list(map(lambda s: str(s), solution))
    if len(solution_list) == 0:
        message = 'No solutions'
    elif len(solution_list) > 1:
        message = 'There are multiple solutions'
    else:
        message = 'OK'
    return {
        "equation": equation_text,
        "target": variable_text,
        "success": len(solution_list) == 1,
        "solution": solution_list,
        "message": message,
    }

def solve_for_variable(target: Symbol, equation: Eq) -> Dict:
    try:
        solution = solve(equation, target)
    except NotImplementedError:
        return create_solution_json(equation, target, [])
    return create_solution_json(equation, target, solution)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def api_solve():
    target = convert_variable(request.form.get('target'))
    equation = convert_equation(request.form.get('equation'))
    if equation is None or target is None:
        return jsonify({ 'success': False, 'message': 'Must provide valid equation and target variable' })

    result = solve_for_variable(target, equation)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
