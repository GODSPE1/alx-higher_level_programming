#!/usr/bin/python3
"""
    contains class square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that implements rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
            initialise Square (overides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            sets the value of the size
        """
        self.width = value
        self.height = value

        def update(self, *args, **kwargs):
            """
                Publc method that assigns attributes

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
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass

        def __str__(self):
            """
                Overloading str function
            """
            return "[{}] ({}) {}/{} {}".format(
                    type(self).__name__, self.id, self.x, self.y, self.width)

        def to_dictionary(self):
            """
                Returns the dictionary representation of a Rectangle
            """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
