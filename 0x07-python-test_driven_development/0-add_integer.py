#!/usr/bin/python3
"""
This module supplies one function that add the parameters
"""

    def add_integer(a, b=98):
        """
        This function adds two numbers

        Args:
            a (int): first number
            b (int):second number

        Raises:
            TypeError: if a or b is not an integer or float

        Returns:
            returns an integer addition of two numbers
        """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be a integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
