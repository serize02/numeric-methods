import numpy as np

def fixed_point():
    
    p_0 = 1.3
    tol = 1e-5
    n = 10

    f = lambda x: (10 / (4 + x))**(1/2)

    for i in range(n):

        p = f(p_0)

        print(f'iteration: {i}', f'p_0: {p_0}', f'f(p_0): {p}')

        if np.abs(p_0 - p) < tol:

            print('Procedure completed successfully. (converged)')
            return

        p_0 = p
    
    print("Max number of iterations reached...")


if __name__ == '__main__':
    fixed_point()