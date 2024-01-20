#!/usr/bin/python3
"""
This module defines the base class for the project
"""
import json


class Base:
    """Base class of other classes with attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries, indent=4)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            return []
        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            with open("Base.json", "w") as fp:
                 json.dump([obj.to_dictionary() for obj in list_objs], fp)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        else:
            list_of_json = json.loads(json_string)
            return list_of_json

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

