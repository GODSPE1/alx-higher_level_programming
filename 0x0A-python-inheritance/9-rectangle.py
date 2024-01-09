#!/usr/bin/python3
"""
Contains the class Geometry and subclass Rectangle
"""


class BaseGeometry:
    """
    This ia a class with public attribut area
    """

    def area(self):
        """This ia a public instace method 
        with Exception('area() is not implemented')
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates the value"""
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """The Rectangle class width width and height private attributes"""
    def __init__(self, width, height):
        """Insantiation of the class Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

