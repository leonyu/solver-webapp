import re
from sympy import symbols, Eq, sympify, solve
from six import string_types


def convert_variable(text):
    if not isinstance(text, string_types) or text.isspace():
        return None
    try:
        return symbols(text)
    except ValueError:
        return None


def convert_equation(text):
    if not isinstance(text, string_types) or text.isspace():
        return None
    line_split = re.split(r'=+', text)
    if len(line_split) != 2:
        # raise Exception('Line does not contain a valid equation')
        return None
    lhs = line_split[0].strip()
    rhs = line_split[1].strip()
    if not lhs or not rhs:
        # raise Exception('LHS and RHS of an equation must not be empty')
        return None
    return Eq(sympify(lhs), sympify(rhs))


def create_solution_json(equation, target, solution):
    equation_text = str(equation)
    variable_text = str(target)
    solution_list = list(map(str, solution))
    return {
        "equation": equation_text,
        "target": variable_text,
        "solutions": solution_list,
    }


def solve_for_variable(target, equation):
    try:
        solution = solve(equation, target)
    except NotImplementedError:
        return create_solution_json(equation, target, [])
    return create_solution_json(equation, target, solution)
