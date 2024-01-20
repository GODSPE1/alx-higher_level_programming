#!/usr/bin/python3

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''represents a class used to test the base class'''

    def test_id(self):
        '''testing the id'''
        b2 = Base()
        self.assertEqual(b2.id, 2)

        '''testing the id'''
        b3 = Base()
        self.assertEqual(b3.id, 3)
        
    def test_instaces_with_unique_id(self):
        "testing id to return the number passed"
        b4 = Base(20)
        self.assertEqual(b4.id, 20)
        b5 = Base(5)
        self.assertEqual(b5.id, 5)

    def test_constructor(self):
        """ Tests constructor signature """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


    def test_for_private_variable(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_passed(self):
        self.assertEqual("yes", Base("yes").id)

    def test_constructor(self):
        """ Tests constructor signature """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        """ Tests constructor signature with 2 notself args """
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_json_string(self):
        """ Test to_json_string method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 1, 3, 4)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_dict1 = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        json_dict2 = [{"x": 3, "width": 11, "id": 1, "height": 1, "y": 4}]
        json_string = Base.to_json_string([dict1, dict2])
        self.assertNotEqual(dict1, json_dict1)
        self.assertNotEqual(dict2, json_dict2)
        self.assertEqual(type(dict1), dict)
        self.assertEqual(type(json_string), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        self.assertTrue(type(json_string), str)
        d = json.loads(json_string)
        self.assertEqual(d, [dict1, dict2])

    def test_from_json_string(self):
        """ Test from_json_string method """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])
        list_input = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        list_output2 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertEqual(list_output, list_output2)
        self.assertTrue(type(list_output), list)

    def test_save_to_file_1(self):
        """ Test save_to_file_method with empty_file """
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_save_to_file_4(self):
        """ Test save_to_file method """
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 0)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except Exception:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)


    def test_create(self):
        """ Test create method """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)



if __name__ == '__main__':
    unittest.main()
