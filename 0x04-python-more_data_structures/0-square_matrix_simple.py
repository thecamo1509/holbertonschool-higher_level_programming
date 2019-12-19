#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in range(len(matrix)):
        newmatrixi = []
        for j in range(len(matrix[i])):
            newmatrixi.append((matrix[i][j]) ** 2)
        newmatrix.append(newmatrixi)
    return(newmatrix)
