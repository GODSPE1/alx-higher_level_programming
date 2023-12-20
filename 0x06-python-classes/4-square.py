#!/usr/bin/python
    
'''A Square class'''


class Square:
    '''This is class square that has a private attributes'''


    def __init__(self, size=0):
        '''Initializes the square'''
        
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
    
    @property
    def size(self):
        """getter function for size
        Returns:
            The size of the square
        """
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """setter function for size
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (self.__size < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the area square
        Args:
            size (int): size of a side of a square
        Returns:
            None
        """
        area = self.__size * self.__size
        return (area)
