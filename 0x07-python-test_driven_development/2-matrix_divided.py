def matrix_divided(matrix, div):
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    newlist = []
    if type(matrix) != list:
        raise TypeError(error1)
    elif type(matrix[0]) != list:
        raise TypeError(error1)
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        size = len(matrix[0])
        for i in range(len(matrix)):
            if type(matrix[i]) != list:
                raise TypeError(error1)
            elif len(matrix[i]) != size:
                raise TypeError(error2)
            newlist2 = []
            newlist.append(newlist2)
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                    raise TypeError(error1)
                newlist[i].append(round((matrix[i][j] / div), 2))
        return newlist
