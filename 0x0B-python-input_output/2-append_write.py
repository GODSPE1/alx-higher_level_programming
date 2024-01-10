#!/usr/bin/python3
"""This module defines a text file read appending"""

def append_write(filename="", text=""):
    """
    Appends a string to text file and returns the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
