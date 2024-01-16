#!/usr/bin/python3
"""
This is test case for the rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        representing testing for Base class
    """

    def test_initialization(self):
        ''' testing initialization of height and width'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        ''' testing initialization again to test id'''
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        ''' testing initialization including x and y'''
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)


if __name__ == '__main__':
    unittest main()
