#!/usr/bin/python3
    
"""
A Square class
"""


class Square:
    """
    This is class square that has a private attributes

    - size: The side size of a square
    """

    
    def __init__(self, size=0):
        """
        Initializes the object with the specified size.

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
    

    def area(self):
        """
        Computes the area of a square
        
        Returns:
        the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        gets the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the private attribute

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
