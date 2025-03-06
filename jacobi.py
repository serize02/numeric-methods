import numpy as np

A = np.array([[6, 2, 1], 
              [-1, 8, 2], 
              [1, -1, 6]], dtype=float)
b = np.array([22, 30, 23], dtype=float)

def jacobi_method(tol=1e-2, max_iterations=10):
    
    global A, b
    
    n = len(A)
    
    x = np.array([2,2,2])
    
    x_new = np.zeros(n)
    
    for iterations in range(max_iterations):
        for i in range(n):
            sum_others = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_others) / A[i, i]
        
        print(iterations, x_new)        
        if (np.linalg.norm(x_new - x, ord=np.inf) / np.linalg.norm(x_new, ord=np.inf)) < tol:
            print('Converged')
            return
        
        x = x_new.copy()
    
    print(f"Jacobi method did not converge within {max_iterations} iterations.")

if __name__ == "__main__":
    jacobi_method()