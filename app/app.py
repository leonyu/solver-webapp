
import os
from typing import List
from sympy import symbols, Eq, solve, sympify, Symbol
from flask import Flask, url_for, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.urandom(16)

def splitAndTrimLines(equationLines: str) -> List[str]:
    return map(lambda s: s.strip(), filter(lambda s: s and not s.isspace(), equationLines.splitlines()))

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def api_solve():
    if not request.form.get('equations') or not request.form.get('target'):
        return jsonify({ 'success': False, 'message': 'Must provide both equations and target' })

    try:
        target = symbols(request.form.get('target'))
    except Exception as error:
        return jsonify({ 'success': False, 'message': 'Unable to parse target variable', 'error': str(error) })
    if type(target) != Symbol and len(target) > 1:
        return jsonify({ 'success': False, 'message': 'Cannot target more than one variable' })
    equationText = splitAndTrimLines(request.form['equations'])
    try:
        equations = list(map(lambda eqStr: Eq(*map(sympify, eqStr.split('='))), equationText))
    except Exception as error:
        return jsonify({ 'success': False, 'message': 'Unable to parse equations', 'error': str(error) })

    solutions = solve(equations, target)
    if not solutions:
        return jsonify({ 'success': False, 'solutions': str(solutions), 'equations': list(map(lambda s: str(s), equations)), 'target': str(target) })
    elif target in solutions:
        return jsonify({ 'success': True, 'solutions': str(solutions[target]), 'equations': list(map(lambda s: str(s), equations)), 'target': str(target) })
    elif type(solutions) == list:
        return jsonify({ 'success': False, 'message': 'Multiple solutions or solutions with imaginary components', 'solutions': list(map(lambda s: str(s), solutions)), 'equations': list(map(lambda s: str(s), equations)), 'target': str(target) })
    else:
        return jsonify({ 'success': False, 'solutions': str(solutions), 'equations': list(map(lambda s: str(s), equations)), 'target': str(target) })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
