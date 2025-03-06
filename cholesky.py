import numpy as np

def cholesky_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1):
            if i == j: 
                L[i][i] = np.sqrt(matrix[i][i] - sum(L[i][k]**2 for k in range(i)))
            else:
                L[i][j] = (matrix[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    return L


A = np.array([[2, -1, 0], [-1, 2, -1], [0,  -1, 2]], dtype=float)
L = cholesky_decomposition(A)

print("Matrix A:")
print(A)
print("\nLower Triangular Matrix L:")
print(L)
print("\nVerification (L @ L.T):")
print(np.dot(L, L.T))