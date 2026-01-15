import numpy as np

def calinski_harabasz_score(X: np.ndarray, labels: np.ndarray) -> float:
    """
    Compute the Calinski-Harabasz Index for clustering evaluation.
    
    Args:
        X: numpy array of shape (n_samples, n_features) containing data points
        labels: numpy array of shape (n_samples,) containing cluster assignments
    
    Returns:
        float: Calinski-Harabasz score (higher is better)
    """
    # Your code here
    k = len(np.unique(labels))
    if k == len(X) or k == 1:
        return 0.0
    centroids = dict()
    counts = dict()
    global_center = np.zeros(len(X[0]))
    for sample, cluster in zip(X, labels):
        centroids[cluster] = centroids.get(cluster, np.zeros_like(sample)) + sample
        counts[cluster] = counts.get(cluster, 0) + 1
        global_center += sample
    n = X.shape[0]
    global_center = global_center / n
    for cluster in centroids.keys():
        centroids[cluster] = centroids[cluster] / counts[cluster]
    wcd = 0
    for i in range(k):
        for sample, cluster in zip(X, labels):
            if cluster == i:
                wcd += np.sum((sample - centroids[i]) ** 2)
    bcd = 0
    for i in range(k):
        bcd += counts[i] * np.sum((centroids[i] - global_center) ** 2)
    
    return (bcd / (k - 1) ) / (wcd / (n - k))
    
X = np.array([[0, 0], [1, 0], [0, 1], [10, 10], [11, 10], [10, 11]])
labels = np.array([0, 0, 0, 1, 1, 1])
print(calinski_harabasz_score(X, labels))