#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        for j in row:
            new.append([[j ** 2 for j in row] for row in matrix])
            return (new)
