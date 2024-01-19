#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''represents a class used to test the base class'''

    def test_id(self):
        '''testing the id'''
        b1 = Base()
        self.assertEqual(b1.id, 1)

        '''testing the id'''
        b2 = Base()
        self.assertEqual(b2.id, 2)

        '''testing the id'''
        b3 = Base()
        self.assertEqual(b3.id, 3)
        
        "testing id to return the number passed"
        b4 = Base(20)
        self.assertEqual(b4.id, 20)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)


if __name__ == '__main__':
    unittest.main()
