#!/usr/bin/python3
"""
Contains the class Geometryand subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class width width and height private attributes"""
    def __init__(self, width, height):
        """Insantiation of the class Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
