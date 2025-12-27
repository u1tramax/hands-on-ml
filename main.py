import numpy as np

def rl_budget_loss(
    rewards: np.ndarray,
    log_probs: np.ndarray,
    old_log_probs: np.ndarray,
    response_lengths: np.ndarray,
    token_budget: int,
    kl_coef: float,
    budget_penalty_coef: float
) -> float:
    """
    Compute the budget-constrained RL loss.
    
    The loss combines:
    1. Budget penalty for responses exceeding token_budget
    2. Advantage estimation (adjusted reward - baseline)
    3. KL regularization between current and old policy
    
    Loss formula: E[(advantage - kl_term)^2]
    
    Args:
        rewards: Shape (batch_size, K) - rewards for K samples per prompt
        log_probs: Shape (batch_size, K) - log π_θ(y|x) current policy
        old_log_probs: Shape (batch_size, K) - log π_old(y|x) old policy
        response_lengths: Shape (batch_size, K) - token lengths of responses
        token_budget: Maximum allowed tokens before penalty
        kl_coef: τ coefficient for KL regularization
        budget_penalty_coef: λ coefficient for budget penalty
        
    Returns:
        Scalar loss value (float)
    """
    # Your code here
    for j, array in enumerate(response_lengths):
        for i, response in enumerate(array):
            rewards[j][i] = max(0, rewards[j][i] - max(0, response - token_budget) * budget_penalty_coef)
    print(rewards)
    
    advantages = rewards - np.mean(rewards, axis=0)
    kl_terms = kl_coef * (log_probs - old_log_probs)
    print(advantages, kl_terms)
    loss = np.mean([(advantage - kl) ** 2 for advantage, kl in zip(advantages, kl_terms)])
    return loss

import numpy as np 
rewards = np.array([[1.0, 0.8, 0.6], [0.5, 0.7, 0.9]]) 
log_probs = np.array([[-1.0, -1.2, -1.4], [-0.8, -1.0, -1.2]]) 
old_log_probs = np.array([[-1.1, -1.1, -1.1], [-0.9, -0.9, -0.9]]) 
response_lengths = np.array([[80, 120, 150], [90, 100, 200]]) 
result = rl_budget_loss(rewards, log_probs, old_log_probs, response_lengths, 100, 0.1, 0.01) 
print(round(result, 4))