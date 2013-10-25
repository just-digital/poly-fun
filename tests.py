"""
Tests that prove polynomial_function does what it should, and also that it's
interface won't regress when modified.
"""
import unittest
from polynomial import polynomial_function


class TestPolynomialFunction(unittest.TestCase):

    def test_interface_contract(self):
        # Make sure the function raises a TypeError when no coeffs are provided
        self.assertRaises(TypeError, polynomial_function)

        # The returned value must be callable
        poly_func = polynomial_function(2, 4, 3)
        self.assertTrue(callable(poly_func))

    def test_solves_equation(self):
        """
        Make sure the returned function solves the equation correctly.
        Solve 2 + 4x + 3x^2 where x is 5:
        2 * 5^0 = 2
        4 * 5^1 = 20
        3 * 5^2 = 75
        2 + 20 + 75 = 97
        """
        poly_func = polynomial_function(2, 4, 3)
        self.assertEqual(poly_func(5), 97)

        val = 100 * (5 ** 0)
        poly_func = polynomial_function(100)
        self.assertEqual(poly_func(5), 100)

        #2 + 3x
        val = (2 * (5 ** 0)) + (3 * (5 ** 1))
        poly_func = polynomial_function(2, 3)
        self.assertEqual(poly_func(5), val)

        #2 + 3x + 4x^2
        val = (2 * (5 ** 0)) + (3 * (5 ** 1)) + (4 * (5 ** 2))
        poly_func = polynomial_function(2, 3, 4)
        self.assertEqual(poly_func(5), val)

if __name__ == '__main__':
    unittest.main()

