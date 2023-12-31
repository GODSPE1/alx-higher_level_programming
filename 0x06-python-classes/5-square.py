#!/usr/bin/python3
    
"""Defiines a class square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side square
    """
    def __init__(self, size=0):
        """Initialize the square
        Args:
            size: (int) size of a side of the square
        Returns:
            None

        """
        self.__size = size

    def area(self):
        """returns the area square
        Args:
            size (int): size of a side of a square
        Returns:
            The area of a square
        """
        area = self.__size * self.__size
        return (area)
    
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

        def my_print(self):
            """prints the square
            Returns:
                None
            """
            if self.__size == 0
            print()
            return
            for i in range(self.__size)
        print("".join(["#" for j in range(self.__)]))