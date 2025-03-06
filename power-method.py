import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([1, 2, 3])
n_estimators = 10
tol = 1e-5

def main():

    global x

    n = A.shape[0]
    p = np.linalg.norm(x, ord=np.inf)
    x = x / p

    for k in range(n_estimators):
        y = A.dot(x)
        u = p
        p = np.linalg.norm(y, ord=np.inf)
        err = np.linalg.norm(x - (y / p), ord=np.inf)
        x = y / p

        print(k, y, p)

        if err < tol:
            print("Converged...")
            return

    print("Max number of iterations reached...")


if __name__ == "__main__":
    main()