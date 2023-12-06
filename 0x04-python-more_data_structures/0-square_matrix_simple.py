#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[1]] * len(matrix)
    index = 0
    for row in matrix:
        new[index] = [x**2 for x in row]
        index += 1
    return(new)
