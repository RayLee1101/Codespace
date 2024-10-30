import math
def Add_Sub(matrix_1, matrix_2, state): # 加法與減法
    matrix = []
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]): # 確定符合格
        for i in range(len(matrix_1)):
            _matrix = []
            for j in range(len(matrix_1[0])):
                if state == 1: # 判斷加或減
                    _matrix.append(matrix_1[i][j] + matrix_2[i][j])
                else:
                    _matrix.append(matrix_1[i][j] - matrix_2[i][j])
            matrix.append(_matrix)
        return matrix
    else:
        return "錯誤"

def Multiply(matrix_1, matrix_2):
    matrix = []
    if type(matrix_1) == int:# 判斷格式
        for i in range(len(matrix_2)):
            _matrix = []
            for j in range(len(matrix_2[0])):
                _matrix.append(matrix_1 * matrix_2[i][j])
            matrix.append(_matrix)
        return matrix
    elif len(matrix_1[0]) == len(matrix_2):   #判斷格式
        for i in range(len(matrix_1)):
            _matrix = []
            for j in range(len(matrix_2[0])):
                num = 0
                for k in range(len(matrix_2)):
                    num += matrix_1[i][k] * matrix_2[k][j]
                _matrix.append(num)
            matrix.append(_matrix)
        return matrix
    else:
        return "錯誤"

def Inverse(matrix):
    n = len(matrix)
    # 創建增廣矩陣
    if inverse_check(matrix) == False:
        return "error"
    aug_matrix = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]
    # 高斯消去法
    for i in range(n):
        # 將對角線元素變為1
        pivot = aug_matrix[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        for j in range(2 * n):
            aug_matrix[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = aug_matrix[k][i]
                for j in range(2 * n):
                    aug_matrix[k][j] -= factor * aug_matrix[i][j]
    # 提取反矩陣
    inverse_matrix = [row[n:] for row in aug_matrix]
    return inverse_matrix

def inverse_check(matrix):
    # 僅處理 2x2 和 3x3 矩陣的行列式
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3 and len(matrix[0]) == 3:
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    else:
        raise False

def Transform(matrix_a): #反轉
    matrix = []
    for i in range(len(matrix_a[0])):
        _matrix = []
        for j in range(len(matrix_a)):
            _matrix.append(matrix_a[j][i])
        matrix.append(_matrix)
    return matrix

def Diagonal(matrix):
    state = True
    if len(matrix) != len(matrix[0]):
        state = False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0 and i != j:
                state = False
    return state

def Symmetric(matrix):
    return matrix == Transform(matrix)

A = [[2, -2], [3, -5]] 
B = [[-2, 0], [0, 2]]
C = [[-1, 2, 0], [2, 0, 3]]
E = [[2, -1], [math.pi, math.log10(2)], [-2, 3]]
F = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Testing
print("a.")
print(Add_Sub(A, Multiply(3, B), 1))
print(Add_Sub(C, Multiply(B, Transform(E)), 0))
print(Transform(A))

print("b.")
M = Multiply(A, B)
N = Multiply(B, A)
print(M == N)

print("c.")
P = Multiply(Transform(C), Transform(B))
Q = Transform(Multiply(B, C))
print(P == Q)

print("d.")
A_inverse = Inverse(A)
F_inverse = Inverse(F)
print(A_inverse)
print(F_inverse)

print("e.")
print(Diagonal(A))
print(Diagonal(B))
print(Diagonal(F))
print(Diagonal(I))

print("f.")
print(Symmetric(A))
print(Symmetric(B))
print(Symmetric(F))
print(Symmetric(I))
