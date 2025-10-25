import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    result = []
    m = X.shape[0]
    for i in range(0, m, batch_size):
        if y is not None:
            result.append([X[i:(i+batch_size)], y[i:(i+batch_size)]])
        else:
            result.append(X[i:(i+batch_size)])
    return result

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, batch_size=batch_size))