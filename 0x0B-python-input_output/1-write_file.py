#!/usr/bin/python3
"""This module defines a text file read and return the number
of chRcters written
"""

def write_file(filename="", text=""):
    """Writes a string text file and returns the number of 
    characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
