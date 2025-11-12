def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}{args} = {result}')
        return result
    return wrapper

@printer
def dot_product(vector1: list[int|float], vector2: list[int|float]) -> int|float:
    if len(vector1) != len(vector2):
        return 0
    dot_product = 0
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
    return dot_product

@printer
def len_vector(vector: list[int|float]) -> int|float:
    len_vector = 0
    for elem in vector:
        len_vector += elem ** 2
    return len_vector ** 0.5

@printer
def cosine(vector1: list[int|float], vector2: list[int|float]) -> int|float:
    return dot_product(vector1, vector2) / (len_vector(vector1) * len_vector(vector2))

@printer
def dot_product_2(matrix: list[list[int|float]], vector: list[int|float]) -> list[int|float]:
    if len(matrix[0]) != len(vector):
        return []
    result = []
    for i in range(len(matrix)):
        temp = 0
        for j in range(len(vector)):
            temp += matrix[i][j] * vector[j]
        result.append(temp)
    return result

@printer
def dot_product_3(matrix1: list[list[int|float]], matrix2: list[list[int|float]]) -> list[list[int|float]]:
    if len(matrix1[0]) != len(matrix2):
        return []
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2)):
            temp = 0
            for k in range(len(matrix1[0])):
                temp += matrix1[i][k] * matrix2[k][j]
            row.append(temp)
        result.append(row)
    return result


vector1 = [1, 2, 3, 4, 5]
vector2 = [1, 2, 3, 4, 5]
matrix1 = [
    [1, 2, 3],
    [3, 4, 5]
]
matrix2 = [
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]
vector3 = [1, 2, 3]
# dot_product(vector1, vector2)
# len_vector(vector1)
# cosine(vector1, vector2)
# dot_product_2(matrix1, vector3)
dot_product_3(matrix1, matrix2)
import numpy as np
print(np.array(matrix1) @ np.array(matrix2))
