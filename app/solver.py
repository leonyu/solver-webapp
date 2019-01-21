from sympy import symbols, Eq, sympify, Symbol, solve

def convert_variable(input):
    if not input or input.isspace():
        return None
    try:
        return symbols(input)
    except:
        return None

def convert_equation(input):
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

def create_solution_json(equation, target, solution):
    equation_text = str(equation)
    variable_text = str(target)
    solution_list = list(map(lambda s: str(s), solution))
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
