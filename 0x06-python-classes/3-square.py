#!/usr/bin/python3
    
"""
This module defines a class called square.
"""


class Square:
    """
    This is class square that has a private attributes


    Attributes:
    size (int): The side size of the square
    
    """

    def __init__(self, size=0):
        """
        Initialize the object with the specified size
        Args:
        size (int): The side size of the square
        """
        
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
    """
    Calculates the area of a circle

    Returns:
        The area of a circle
    """
        area = self.__size * self.__size
        return area
