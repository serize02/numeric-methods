from sklearn.linear_model import LinearRegression
import numpy as np

lr = LinearRegression()

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6]).reshape(-1, 1)

lr.fit(x, y)

print(lr.intercept_, lr.coef_)