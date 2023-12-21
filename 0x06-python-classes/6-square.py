#!/usr/bin/python3    
"""Defiines a class square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square
        Args:
            size: (int) size of a side of the square
            position (tuple): the cordinates of the square
        """
        self.size = size
        self.position = position

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

        @property
        def position(self):
            """Get or set the position of the square"""
            return self.__position
        
        @position.setter
        def position(self, value):
            if type(value) is tuple and len(value) is 2 and  \
                type(value[0]) is int  and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError('position must be a tuple of 2 positive integers')
            
        def area(self):
            """Returns the current square area"""
            return self.__size ** 2
        
        def my_print(self):
            """prints the square"""
            if self.__size > 0:
                for y in range(self.__postion[1]):
                    print()
                for x in range(self.__size):
                    print(' ' * self.__postion[0], end='')
                    print('#' * self.__size)
            else:
                print()
