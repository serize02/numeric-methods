import numpy as np

def crout_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.eye(n)
    
    for j in range(n):
        for i in range(j, n):
            L[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(j))
        for i in range(j + 1, n):
            U[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]
    
    return L, U

A = np.array([[3, 1, 2], [1, 3, 1], [2, 1, 3]], dtype=float)
L, U = crout_decomposition(A)

print("\nMatrix A:")
print(A)
print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
print("\nVerification (L @ U):")
print(np.dot(L, U))