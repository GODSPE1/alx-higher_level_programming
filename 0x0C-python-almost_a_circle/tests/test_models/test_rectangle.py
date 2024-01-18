#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_isClass(self):
        r6 = Rectangle(10, 2)
        self.assertIsInstance(r6, Rectangle)

    def test_forSubclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_initialization(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_zero_instatiation(self):
        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(0, 12)

        error_msg = "width must be >= 0"
        self.assertEqual(str(e.exception), error_msg)

    def test_zero_instatiation(self):
        with self.assertRaises(ValueError) as e:
            r5 = Rectangle(12, 0)

        error_msg = "height must be > 0"
        self.assertEqual(str(e.exception), error_msg)

    def test_y_not_int(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r6 = Rectangle(10, 23, 3, "y")

    def test_x_not_int(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r7 = Rectangle(10, 23, "x", 6)


if __name__ == '__main__':
    unittest.main()
