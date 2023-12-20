#!/usr/bin/python3
    
"""
This module defines a class called square.
"""


class Square:
    """
    This is class square 
    """
    

    def __init__(self, size=0):
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
        area = self.__size ** 2
        return area
