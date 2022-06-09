#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        return ([[j ** 2 for j in row] for row in matrix])
