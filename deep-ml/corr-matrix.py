import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
    if Y is None:
        Y = X
        # return np.ones((X.shape[1], X.shape[1]))
    corr = np.diag(np.zeros(X.shape[1]))
    n = X.shape[0]
    for i in range(X.shape[1]):
        for j in range(Y.shape[1]):
            mean_X, mean_Y = X[:, i].mean(), Y[:, j].mean()
            std_X, std_Y = X[:, i].std(), Y[:, j].std()
            corr[i, j] = np.sum((X[:, i] - mean_X) * (Y[:, j] - mean_Y)) / (n * std_X * std_Y)
    return corr

def calculate_correlation_matrix_2(X, Y=None):
	# Your code here
    if Y is None:
        Y = X
    n = X.shape[0]
    mean_X, mean_Y = np.mean(X, axis=0), np.mean(Y, axis=0)
    std_X, std_Y = np.std(X, axis=0), np.std(Y, axis=0)
    corr = (X - mean_X).T @ (Y - mean_Y) / (n * std_X[:, None] * std_Y[None, :])
    return corr

# X = np.array([[1, 2], [3, 4], [5, 6]])
# output = calculate_correlation_matrix_2(X)
# print(output)

print(calculate_correlation_matrix_2(np.array([[1, 0], [0, 1]]), np.array([[1, 2], [3, 4]])))