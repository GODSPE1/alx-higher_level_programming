#!/usr/bin/python3
""" function to find the peak of list of integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    highest = list_of_integers[0]
    for item in list_of_integers:
        if item > highest:
            highest = item

    return highest

if __name__ == '__main__':
    pass
