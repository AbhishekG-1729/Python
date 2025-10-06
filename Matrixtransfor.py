import numpy as np
matrix = []
print("Enter the elements of the 3x3 matrix row-wise:")
for i in range(3):
    row = list(map(int, input(f"Enter 3 integers for row {i+1}, separated by space: ").split()))
    while len(row) != 3:
        print("Please enter exactly 3 integers.")
        row = list(map(int, input(f"Enter row {i+1} again: ").split()))
    matrix.append(row)
matrix_np = np.array(matrix)
print("\nOriginal 3x3 matrix:")
print(matrix_np)
one_d = matrix_np.reshape(-1)
print("\nReshaped to 1D array:")
print(one_d)
two_d = one_d.reshape(3, 3)
print("\nFlattened back to 2D array:")
print(two_d)