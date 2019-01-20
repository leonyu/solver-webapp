from sympy import Symbol, Eq
from app import solve_for_variable, convert_equation, convert_variable

def test_convert_variable():
    abc = convert_variable('abc')
    assert type(abc) == Symbol
    assert abc != None
    assert str(abc) == 'abc'

def test_convert_equation():
    eq = convert_equation('a + b = c')
    assert type(eq) == Eq
    assert str(eq.lhs) == 'a + b'
    assert str(eq.rhs) == 'c'
    assert str(eq) == 'Eq(a + b, c)'

    eq = convert_equation('a + b =')
    assert eq is None

    eq = convert_equation('')
    assert eq is None

def test_solve_for_variable():
    result = solve_for_variable(convert_variable('a'), convert_equation('x + y * y = z / a'))
    assert result['success']
    assert result['solution'] == ['z/(x + y**2)']
    assert result['message'] == 'OK'

    result = solve_for_variable(convert_variable('z'), convert_equation('x + y * y = z / a'))
    assert result['success']
    assert result['solution'] == ['a*(x + y**2)']
    assert result['message'] == 'OK'

    result = solve_for_variable(convert_variable('z'), convert_equation('cos(x) / tan(z) = z / a'))
    assert not result['success']
    assert result['solution'] == []
    assert result['message'] == 'No solutions'

    result = solve_for_variable(convert_variable('z'), convert_equation('a + b = c'))
    assert not result['success']
    assert result['solution'] == []
    assert result['message'] == 'No solutions'

    result = solve_for_variable(convert_variable('z'), convert_equation('a + b = c'))
    assert not result['success']
    assert result['solution'] == []
    assert result['message'] == 'No solutions'

    result = solve_for_variable(convert_variable('z'), convert_equation('a + b = c'))
    assert not result['success']
    assert result['solution'] == []
    assert result['message'] == 'No solutions'
