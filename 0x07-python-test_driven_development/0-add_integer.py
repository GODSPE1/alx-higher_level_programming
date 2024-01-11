#!/usr/bin/python3
"""
This module supplies one function that
add the parameters
khlkljlkjlkh jkhk klihoinmbkho

"""


def add_integer(a, b=98):
    """
    This function adds two numbers

    Args:
        a: first number
        b:second number

    Raises:
        raise TypeError if a or b is not an 
        integer or float

    Returns:
        Returns an integer addition of two numbers
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
