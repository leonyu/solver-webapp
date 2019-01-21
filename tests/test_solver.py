import unittest
from sympy import Symbol, Eq
from app.solver import solve_for_variable, convert_equation, convert_variable


class TestAppMethods(unittest.TestCase):
    def test_convert_variable(self):
        result = convert_variable(' ')
        self.assertIsNone(result)
        result = convert_variable(True)
        self.assertIsNone(result)
        abc = convert_variable('abc')
        self.assertIsInstance(abc, Symbol)
        self.assertEqual(str(abc), 'abc')

    def test_convert_equation_success(self):
        eq_test = convert_equation('a + b = c')
        self.assertIsInstance(eq_test, Eq)
        self.assertEqual(str(eq_test.lhs), 'a + b')
        self.assertEqual(str(eq_test.rhs), 'c')
        self.assertEqual(str(eq_test), 'Eq(a + b, c)')

    def test_convert_equation_failure(self):
        self.assertIsNone(convert_equation('a + b ='))
        self.assertIsNone(convert_equation('a = b = c'))
        self.assertIsNone(convert_equation('a == b'))
        self.assertIsNone(convert_equation('a b'))
        self.assertIsNone(convert_equation(''))
        self.assertIsNone(convert_equation(None))
        self.assertIsNone(convert_equation(True))

    def test_solve_for_variable_success(self):
        result = solve_for_variable(convert_variable(
            'a'), convert_equation('x + y * y = z / a'))
        self.assertEqual(result['solutions'], ['z/(x + y**2)'])

        result = solve_for_variable(convert_variable(
            'z'), convert_equation('x + y * y = z / a'))
        self.assertEqual(result['solutions'], ['a*(x + y**2)'])

        result = solve_for_variable(convert_variable(
            'a'), convert_equation('log(a) + b = c'))
        self.assertEqual(result['solutions'], ['exp(-b + c)'])

    def test_solve_for_variable_multiple_solutions(self):
        result = solve_for_variable(
            convert_variable('a'), convert_equation('x + y * y = z / a ** 2')
        )
        self.assertEqual(
            result['solutions'], ['-sqrt(z/(x + y**2))', 'sqrt(z/(x + y**2))']
        )

    def test_solve_for_variable_failure(self):
        result = solve_for_variable(convert_variable(
            'z'), convert_equation('cos(x) / tan(z) = z / a'))
        self.assertEqual(result['solutions'], [])

        result = solve_for_variable(convert_variable(
            'z'), convert_equation('a + b = c'))
        self.assertEqual(result['solutions'], [])

        result = solve_for_variable(convert_variable(
            'z'), convert_equation('a + b = c'))
        self.assertEqual(result['solutions'], [])

        result = solve_for_variable(convert_variable(
            'z'), convert_equation('a + b = c'))
        self.assertEqual(result['solutions'], [])

        result = solve_for_variable(convert_variable(
            '='), convert_equation('a + b = c'))
        self.assertEqual(result['solutions'], [])

        result = solve_for_variable(convert_variable(
            'log'), convert_equation('log(a) + b = c'))
        self.assertEqual(result['solutions'], [])


if __name__ == '__main__':
    unittest.main()
