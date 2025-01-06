import math
import copy

def eigenvalues(arr):
    # Check for zero matrix
    if arr == [[0, 0], [0, 0]]:
        return [0, 0]

    a = 1
    b = -(arr[0][0] + arr[1][1])
    c = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        raise ValueError("The matrix has complex eigenvalues, which this function does not handle.")

    lambda1 = (-b + math.sqrt(discriminant)) / (2 * a)
    lambda2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return [lambda1, lambda2]

def eigenvectors(arr, eigenvalue):
    # Check for zero matrix
    if arr == [[0, 0], [0, 0]]:
        return "Any non-zero vector"

    matrix = copy.deepcopy(arr)
    matrix[0][0] -= eigenvalue
    matrix[1][1] -= eigenvalue

    # Solve the equation (A - λI)x = 0
    if matrix[0][1] != 0:
        x1 = 1
        x2 = -matrix[0][0] / matrix[0][1]
    elif matrix[1][0] != 0:
        x1 = -matrix[1][1] / matrix[1][0]
        x2 = 1
    else:
        x1, x2 = 1, 0  # Default case if all elements are zero

    # Normalize the eigenvector
    norm = math.gcd(int(x1), int(x2)) if x1 != 0 and x2 != 0 else 1
    return [int(x1 / norm), int(x2 / norm)]

def main():
    matrices = [
        [[1, 6], [5, 2]],
        [[2, 3], [3, -6]],
        [[7, 2], [-4, 1]],
        [[1, 1], [-1, 1]],
        [[0, 0], [0, 0]]
    ]

    for matrix in matrices:
        print(f"Matrix: {matrix}")
        try:
            evalues = eigenvalues(matrix)
            print(f"Eigenvalues: {evalues}")

            for ev in evalues:
                evector = eigenvectors(matrix, ev)
                print(f"Eigenvalue: {ev}, Eigenvector: {evector}")

        except ValueError as e:
            print(f"Error: {e}")
main()