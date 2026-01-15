import numpy as np

def noisy_topk_gating(
    X: np.ndarray,
    W_g: np.ndarray,
    W_noise: np.ndarray,
    N: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Args:
        X: Input data, shape (batch_size, features)
        W_g: Gating weight matrix, shape (features, num_experts)
        W_noise: Noise weight matrix, shape (features, num_experts)
        N: Noise samples, shape (batch_size, num_experts)
        k: Number of experts to keep per example
    Returns:
        Gating probabilities, shape (batch_size, num_experts)
    """
    # Your code here
    def softplus(h):
        return np.log(1 + np.exp(h))
    h_base = X @ W_g
    h_noise = X @ W_noise
    print(h_base.shape, N.shape, softplus(h_noise).shape)
    h = h_base + N * softplus(h_noise)
    h_ap = h[:k]
    g = np.exp(h_ap) / np.sum(np.exp(h_ap), axis=1, keepdims=True)
    return g.round(4)

X = np.array([[1.0, 2.0]])
W_g = np.array([[1.0, 0.0], [0.0, 1.0]])
W_noise = np.array([[0.5, 0.5], [0.5, 0.5]])
N = np.array([[1.0, -1.0]])
k = 2
print(noisy_topk_gating(X, W_g, W_noise, N, k))