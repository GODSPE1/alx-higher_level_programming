#!/usr/bin/python3
"""
this module defines the base class for the project
"""


class Base:
    """Base class of other classes with attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialises the instance of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
