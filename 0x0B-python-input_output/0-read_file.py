#!/usr/bin/python3
"""This module defines a text file read and print to the stdout """

def read_file(filename=""):
    """Reads a text fle and print to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
