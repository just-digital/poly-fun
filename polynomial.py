"""
Module containing the polynomial_function.  Usage:

>>> poly_func = polynomial_function(2, 4, 3)  # 2 + 4x + 3x^2
>>> poly_func(5)  # Solve the equation where x=5
97
"""


def polynomial_function(*coeffs):
    """
    This function accepts a list of coefficients as args and returns a callable
    such that when passed the value for x, will solve the polynomial.
    """
    if not coeffs:
        raise TypeError("Please specify some coefficients")

    def func(x):
        total = 0
        for power, coeff in enumerate(func.coeffs):
            total += coeff * x ** power
        return total
    func.coeffs = coeffs
    return func

