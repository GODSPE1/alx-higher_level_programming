#!/usr/bin/python3
"""This module imports a class Rectangle with a subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class"""

    def __init__(self, size):
        """initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
