from typing import Callable
import copy
import numpy as np

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:

    x = np.array(point)
    n = len(point)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            e_i = np.zeros(n)
            e_j = np.zeros(n)
            e_i[i] = h
            e_j[j] = h
            H[i, j] = (
                f(x + e_i + e_j)
                - f(x + e_i - e_j)
                - f(x - e_i + e_j)
                + f(x - e_i - e_j)
            ) / (4 * h * h)
    return H

def f(p):
    return p[0]**2 + p[1]**2 

result = compute_hessian(f, [0.0, 0.0]) 
print([[round(v, 4) for v in row] for row in result])