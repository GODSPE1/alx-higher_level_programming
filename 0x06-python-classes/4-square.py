#!/usr/bin/python
    
'''A Square class'''


class Square:
    '''this is class square that has a private attributes'''

    '''constructor for square class'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
    
    @property
    def size(self):
        '''getter function for size'''
        return (self.__size)
    
    @size.setter
    def size(self, value):
        '''setter function for size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (self.__size < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area