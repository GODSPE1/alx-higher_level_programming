#!/usr/bin/python3
"""Unittest cases for Square class"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle  # Import the Rectangle class


class SquareTest(unittest.TestCase):
    """
    Test for the Square class
    """
    def setUp(self):
        """sets up the fixtures"""
        self.se = Square(4)
        self.sq = Square(1, 5, 4)
        self.sh = Square(6, 2, 2, 10)

    def tearDown(self):
        """resets the id counter to get new id on Base class"""
        Base._Base__nb_objects = 0

    def test_subclass_relationship(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_class_relationship(self):
        self.assertTrue(isinstance(self.se, Square))

    def test_for_id(self):
        """test for id"""
        self.assertEqual(self.se.id, 1)
        self.assertEqual(self.sq.id, 2)
        self.assertEqual(self.sh.id, 10)

    def test_type_error(self):
        """test for TypeError"""
        with self.assertRaises(TypeError):
            s1 = Square("1")
            s2 = Square(5.5)
            s3 = Square()
            s4 = Square(complex(5))
            s5 = Square(True)
            s6 = Square(True, 2, 3)
            s7 = Square({1,2,3}, 2)
            s8 = Square((1, 2 ,3), 5)
            s9 = Square([1, 2, 5])
            s7 = Square(1,{1,2,3})
            s8 = Square(2, (1, 2 ,3))
            s9 = Square(5, [1, 2, 5])
            s10 = Square(1, "invalid")
            s4 = Square(complex(5))
            s5 = Square(range(5))
            s17 = Square(1, {1,2,3}, 2)
            s18 = Square(1, (1, 2 ,3), 5)
            s19 = Square(1, [1, 2, 5], 1)
            s27 = Square(1, {1,2,3}, 4)
            s28 = Square(2, (1, 2 ,3), 5)
            s29 = Square(5, [1, 2, 5])
            s30 = Square(1, "invalid", 5)
            s33 = Square(6, None, 4)
            s33 = Square(6, None)
            self.sh.x = "5"
            self.sh.y = "yes"
            self.sh.width = "2"
            self.sh.height = "3"
            self.sh.size = "1"
            self.sh.size = "0"

    def test_type_error(self):
        """test for ValueError"""
        with self.assertRaises(ValueError):
            s1 = Square(0)
            s2 = Square(-3)
            s3 = Square(0, 1)
            s4 = Square(-1, 4)
            self.sh.x = -9
            self.sh.y = -9
            self.sh.size = -1
            self.sh.size = 0

    def test_size(self):
        """Test size"""
        self.assertEqual(self.sq.size, 1)

    def test_x(self):
        """Test x"""
        self.assertEqual(self.sq.x, 5)

    def test_y(self):
        """Test y"""
        self.assertEqual(self.sq.y, 4)

    def test_negative_size(self):
        """Test negative size"""
        with self.assertRaises(ValueError, msg="size must be > 0"):
            ins = Square(-1)

    def test_Setter_for_size(self):
        with self.assertRaises(TypeError, msg="must be an integer"):
            ins = Square("hello")


if __name__ == "__main__":
    unitest.main()
