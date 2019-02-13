import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([[1], [2.5], [3.5]])

#slope of the best fit model
thetas = np.array([0.5, 1.0, 1.5])


def cost(X, y, theta):
    inner = np.power((theta.T - y), 2)
    return np.sum(inner) / (2 * len(X))

for i in range(len(thetas)):
    best_h = np.array([X[i] * thetas])
    print('this',cost(X, y, best_h))
