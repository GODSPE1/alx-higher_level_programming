#!/usr/bin/python3
"""
This module contains Rectangle class that implements Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class implements the Base class.
    Methods:
        __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the instance of the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for __width attribute
        Returns: the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter function for __height attribute
        Returns: the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for height
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter function for __x attribute
        Returns: the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for x
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter function for __y attribute
        Returns: the value of y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter function for y
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle object
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the # to stdout to represent the Rectangle instance
        """
        print_symbol = "#"

        for _ in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + print_symbol * self.width)

        print("#" * self.id, end="")

    def __str__(self):
        """
        Returns a string format of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Public method that assigns attributes

        Args:
            *args - list of no-keyworded arguments
            **kwargs - list of keyworded arguments
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {
            'id': getattr(self, "id"),
            'width': getattr(self, "width"),
            'height': getattr(self, "height"),
            'x': getattr(self, "x"),
            'y': getattr(self, "y")
        }
