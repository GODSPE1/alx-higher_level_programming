#!/usr/bin/python3
    
"""
A Square class
"""


class Square:
    """
    This is class square that has a private attributes

    - size: The side size of a square
    """

    
    def __init__(self, size=0):
        """
        Initializes the object with the specified size.

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
    

    def area(self):
        """
        Computes the area of a square
        
        Returns:
        the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        gets the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the private attribute

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
    def __eq__(self, other):
        """
        Compares two square objects for equality based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()
    def __ne__(self, other):
        """
        Compares two square objects for inequality based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()
    def __lt__(self, other):
        """
        Compares two square objects to check if one is less than the other based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()
    def __le__(self, other):
        """
        Compares two square objects to check if one is less than or equal to the other based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()
    def __gt__(self, other):
        """
        Compares two square objects to check if one is greater than the other based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()
    def __ge__(self, other):
        """
        Compares two square objects to check if one is greater than or equal to the other based on their area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
    def __str__(self):
        """
        Returns a string representation of the square object.
        """
        return f"Square with size {self.__size}"
    def __repr__(self):
        """
        Returns a string representation of the square object for debugging.
        """
        return f"Square({self.__size})"
    def __del__(self):
        """
        Prints a message when the square object is deleted.
        """
        print("Bye square...")
    def __hash__(self):
        """
        Returns a hash value for the square object based on its area.
        """
        return hash(self.area())
    def __bool__(self):
        """
        Returns True if the square has a non-zero area, otherwise False.
        """
        return self.area() != 0
    def __copy__(self):
        """
        Returns a shallow copy of the square object.
        """
        return Square(self.__size)
    def __deepcopy__(self, memo):
        """
        Returns a deep copy of the square object.
        """
        from copy import deepcopy
        return Square(deepcopy(self.__size, memo))
    def __format__(self, format_spec):
        """
        Formats the square object based on the specified format specification.
        """
        return f"Square with size {self.__size:{format_spec}}"
    def __sizeof__(self):
        """
        Returns the size of the square object in bytes.
        """
        return super().__sizeof__() + self.__size.__sizeof__()
    def __next__(self):
        """
        Returns the next square object in the sequence.
        """
        return Square(self.__size + 1)
    def __reversed__(self):
        """
        Returns a reversed iterator for the square object.
        """
        return iter(range(self.__size, 0, -1))
    def __contains__(self, item):
        """
        Checks if the square object contains a specific item.
        """
        return item in range(self.__size)
    def __iter__(self):
        """
        Returns an iterator for the square object.
        """
        return iter(range(self.__size))
    def __reversed__(self):
        """
        Returns a reversed iterator for the square object.
        """
        return iter(range(self.__size, 0, -1))
    def __call__(self, *args, **kwargs):
        """
        Calls the square object as a function.
        """
        return Square(*args, **kwargs)
    def __enter__(self):
        """
        Enters a context manager for the square object.
        """
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exits a context manager for the square object.
        """
        pass
    def __getattr__(self, name):
        """
        Gets an attribute of the square object.
        """
        if name == 'size':
            return self.__size
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    def __setattr__(self, name, value):
        """
        Sets an attribute of the square object.
        """
        if name == 'size':
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            if (value < 0):
                raise ValueError('size must be >= 0')
        super().__setattr__(name, value)
    def __delattr__(self, name):
        """
        Deletes an attribute of the square object.
        """
        if name == 'size':
            raise AttributeError("can't delete size")
        super().__delattr__(name)
    def __dir__(self):
        """
        Returns a list of attributes and methods of the square object.
        """
        return super().__dir__() + ['size', 'area']
    def __sizeof__(self):
        """
        Returns the size of the square object in bytes.
        """
        return super().__sizeof__() + self.__size.__sizeof__()