#!/usr/bin/python3
"""
This is a Geometry class
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
