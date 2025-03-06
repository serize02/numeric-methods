import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def df(x):
    return 2*x


def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    x_history = [x]
    for _ in range(num_iterations):
        x = x - learning_rate * df(x)
        x_history.append(x)

    return x, x_history


starting_point = 10  
learning_rate = 0.1 
num_iterations = 20 

final_x, history = gradient_descent(starting_point, learning_rate, num_iterations)

print(f'Valor final de x: {final_x}')
print(f'Historia de x: {history}')

x_values = np.linspace(-11, 11, 400)
y_values = f(x_values)

plt.plot(x_values, y_values, label='f(x) = x^2')
plt.scatter(history, f(np.array(history)), color='red', label='Camino del gradiente descendente')
plt.title('Método del Gradiente Descendente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()