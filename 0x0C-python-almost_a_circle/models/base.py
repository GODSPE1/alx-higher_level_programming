#!/usr/bin/python3
"""
this module defines the base class for the project
"""
import json
from models.Rectangle import Rectangle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == []:
            return ("[]")
        else:
            json_string = json.dumps(list_dictionaries, indent=4)
        return (json_string)
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            return([])
        else:
            with open("Base.json", a) as fp:
                return (fp)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or []:
            return ([])
        else:
            list_of_json = [{i: json_string[i]} for i in json_string]
            json_string_array = json.dumps(list_of_json)
            return (json_string_array)

    @classmethod
    def create(cls, **dictionary):
        super.__init__(width, height, size)
    dummy = Rectangle()
    update(self, **dictionary)
