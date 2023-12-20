#!/usr/bin/python3
    
"""
A Square class
"""


class Square:
    '''This is class square that has a private attributes'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
