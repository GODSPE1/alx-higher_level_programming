#!/usr/bin/python3
"""This defines a module"""
class Rectangle:
    """
    This rectangle class
    """


    def __init__(self, width=0, height=0):
        """
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
            self.__height = height

    @property
    def width(self):
        """
        gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
         if type(height) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
 

    @property
    def height(self):
        """
        gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
         if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
