import numpy as np

def doolittle_decomposition(matrix):
    n = len(matrix)
    L = np.eye(n) 
    U = np.zeros((n, n))
    
    for i in range(n):

        for k in range(i, n):
            U[i][k] = matrix[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
        

        for k in range(i + 1, n):
            L[k][i] = (matrix[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
    
    return L, U

A = np.array([[2, -1, -1], [3, 3, 39], [3, 3, 5]], dtype=float)
L, U = doolittle_decomposition(A)

print("\nMatrix A:")
print(A)
print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
print("\nVerification (L @ U):")
print(np.dot(L, U))