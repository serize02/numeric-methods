
def bisection():
    
    a = 1
    b = 2    
    tol = 1e-3
    n = 10

    f = lambda x: x**3 + 4*x**2 - 10

    for i in range(n):

        p = (a + b) / 2

        print(f'iteration: {i}', f'a: {a}', f'b: {b}', f'p: {p}', f'f(p): {f(p)}')

        if f(p) == 0 or (b - a) / 2  < tol:
            print('Procedure completed successfully. (converged)')
            return

        if f(p) * f(a) > 0:
            a = p
        else:
            b = p
    
    print("Max number of iterations reached...")


if __name__ == '__main__':
    bisection()