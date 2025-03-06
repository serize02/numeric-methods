import numpy as np

A = np.array([[6, 2, 1], 
              [-1, 8, 2], 
              [1, -1, 6]], dtype=float)
b = np.array([22, 30, 23], dtype=float)

def gauss_seidel_method(tol=1e-2, max_iterations=10):
    
    global A, b
    
    n = len(A)
    
    x = np.zeros(n)  # Inicializar x con ceros
    
    for iterations in range(max_iterations):
        x_old = x.copy()  # Guardar el valor anterior de x
        
        for i in range(n):
            sum_previous = sum(A[i, j] * x[j] for j in range(i)) 
            sum_next = sum(A[i, j] * x_old[j] for j in range(i + 1, n)) 
            
            x[i] = (b[i] - sum_previous - sum_next) / A[i, i]
        
        print(iterations, x)
        
        residual = np.linalg.norm(x - x_old, ord=np.inf)
        if residual < tol:
            print("Converged")
            return
    
    print(f"Gauss-Seidel method did not converge within {max_iterations} iterations.")

if __name__ == "__main__":
    gauss_seidel_method()