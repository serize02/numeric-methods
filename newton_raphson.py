import math
import numpy as np

def newton_raphson():

    p_0 = 0.74
    tol = 1e-5
    n = 10

    f = lambda x: math.cos(x) - x
    df = lambda x: -math.sin(x) - 1

    for i in range(n):

        p = p_0 - f(p_0) / df(p_0)

        print(f'iteration: {i}', f'p_0: {p_0}', f'f(p_0): {f(p_0)}', f'df(p_0): {df(p_0)}', f'p: {p}')

        if np.abs(p - p_0) < tol:
            print('Procedure completed successfully. (converged)')
            return
        
        p_0 = p

    print("Max number of iterations reached...")

if __name__ == '__main__':
    newton_raphson()
        