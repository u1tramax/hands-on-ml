import numpy as np
from scipy.stats import spearmanr, kendalltau, pearsonr

x = np.arange(-50, 50, 1)
y = x * -2
print(f'Spearman : {spearmanr(x, y)}\n, Kendall: {kendalltau(x, y)}\n Pearson: {pearsonr(x, y)}')