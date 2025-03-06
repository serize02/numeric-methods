import math
import numpy as np

def secant():

    p_0 = 0.6
    p_1 = 0.7
    tol = 1e-5
    n = 10

    f = lambda x: math.cos(x) - x
    
    q_0 = f(p_0)
    q_1 = f(p_1)

    for i in range(1, n):

        p = p_1 - q_1*(p_1 - p_0) / (q_1 - q_0)

        print(f'iteration: {i}', f'p_0: {p_0}', f'p_1: {p_1}', f'q_0: {q_0}', f'q_1: {q_1}', f'p: {p}')

        if np.abs(p - p_1) < tol:
            print('Procedure completed successfully. (converged)')
            return
        
        p_0 = p_1
        p_1 = p
        q_0 = q_1
        q_1 = f(p)

    print("Max number of iterations reached...")

if __name__ == '__main__':
    secant()
        