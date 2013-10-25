poly-fun
========

A little polynomial function that itself returns a function that is able to solve the equation

    >>> poly_func = polynomial_function(2, 4, 3)  # 2 + 4x + 3x^2
    >>> poly_func(5)  # Solve the equation where x=5

To run the tests:

    >>> python tests.py

