import numpy as np

def input_matrix(name):
    matrix = []
    print(f"Enter the elements of {name} (3 rows, each with 3 integers):")
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        while len(row) != 3:
            print("Please enter exactly 3 integers.")
            row = list(map(int, input(f"Row {i+1} again: ").split()))
        matrix.append(row)
    return np.array(matrix)
 
matrix1 = input_matrix("Matrix 1")
matrix2 = input_matrix("Matrix 2")

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

result = np.dot(matrix1, matrix2)

print("\nResult of matrix multiplication:")
print(result)