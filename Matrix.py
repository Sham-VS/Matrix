import math
import numpy as np


def construct_name(matrix):
    size = len(matrix)
    name = ""
    for i in range(size):
        for j in range(size):
            name += str(matrix[i][j]) + ","
    return name


def mat_printer(matrix, fsize):
    size = len(matrix)
    for i in range(size):
        print("|", end="")
        for j in range(size):
            print(f"{round(matrix[i][j], 3):> {fsize}}", end="")
        print("|")


def minor(matrix, n, m):
    size = len(matrix)
    sub_mat = []
    for i in range(size):
        if i == n:
            continue
        row = []
        for j in range(len(matrix[0])):
            if j == m:
                continue
            row.append(matrix[i][j])
        sub_mat.append(row)
    return sub_mat


def determinant(matrix, hash_map={}):
    name = construct_name(matrix)
    if name in hash_map:
        return hash_map[name]

    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(size):
        det += ((-1) ** i) * matrix[0][i] * determinant(minor(matrix, 0, i))

    hash_map[name] = det
    return det


def inverse(matrix):
    det = determinant(matrix)
    adj = adjugate(matrix)
    return [[adj[i][j] / det for j in range(len(matrix))] for i in range(len(matrix))]


def adjugate(matrix):
    size = len(matrix)
    adj = []
    for i in range(size):
        row = []
        for j in range(size):
            # Cofactor = (-1)^(i+j) * determinant(minor)
            cof = ((-1) ** (i + j)) * determinant(minor(matrix, j, i))
            # Notice (j, i) here instead of (i, j) → transpose done inline
            row.append(cof)
        adj.append(row)
    return adj


def inv_printer(inv, matrix):
    size = len(inv)
    det = determinant(matrix)
    a = int(math.ceil(abs((math.log10(abs(det))))))
    fsize = a * 2 + 3
    space = a + 9
    det_place = size // 2

    for i in range(size):
        if i == det_place:
            print(f"{'1 / ' + str(round(det, 3)):>{space}}", end="")

        else:
            print(" " * space, end="")
        print("|", end="")

        for j in range(size):
            print(f"{round(inv[i][j] * det, 3):> {fsize}}", end="")
        print("|")


n = int(input("Enter the order of the matrix: "))
print()
matrix = np.zeros((n, n), dtype=float)
max_value = float("-inf")
for i in range(n):
    for j in range(n):
        while True:
            try:
                x = float(input(f"Enter element [{i+1}][{j+1}] -> "))
            except ValueError:
                print("Invalid input")
                continue
            break

        x = int(x)
        if abs(x) > max_value:
            max_value = abs(x)
        matrix[i, j] = x

max_val_len = int(math.ceil(math.log10(abs(max_value)))) + 6
print("\nThe entered matrix is: \n")
mat_printer(matrix, max_val_len)

det = determinant(matrix)
print(f"\nDeterminant of the matrix is {det}")

adj_mat = adjugate(matrix)
print("\nThe adjugate (adjoint) matrix is:\n")
mat_printer(adj_mat, max_val_len + 5)
# print(adj_mat)

if det == 0:
    print("\nInverse doesn't exist\n")

else:
    inv_mat = inverse(matrix)
    print("\nThe inverse matrix is:\n")
    mat_printer(inv_mat, max_val_len + 2)
    # print(inv_mat)

    print("\nInverse matrix in divided form:\n")
    inv_printer(inv_mat, matrix)
