#!/usr/bin/python3
"""
new_matrix = matrix.copy()
return [[(x ** 2) for x in row] for row in new_matrix]

def square_matrix_simple(matrix=[]))
"""
def square(num):
    return num ** 2

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        newmatrix.append(list(map(i, square)))
    return newmatrix
