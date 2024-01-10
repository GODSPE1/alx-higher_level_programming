#!/usr/bin/python3
"""This Module defines a string-JSON function"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string object"""
    return json.loads(my_str)
