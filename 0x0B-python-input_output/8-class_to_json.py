#!/usr/bin/python3
"""Moule that returns the dictionary description with a simple
data structure for aJSON serializationof an objec
"""


def class_to_json(obj):
    """Functio that returns the dictionary of an obj"""
    res ={}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
