import numpy as np 

def f(x): 
    return np.sum(x**2) 

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    numerical_grad = []
    for i in range(len(x)):
        x_left, x_right = x.copy(), x.copy()
        x_left[i] += epsilon
        x_right[i] -= epsilon
        grad_i = (f(x_left) - f(x_right)) / (2 * epsilon)
        numerical_grad.append(grad_i)
    relative_error = np.linalg.norm(numerical_grad - analytical_grad) / (np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad))
    return numerical_grad, relative_error

x = np.array([3.0]) 
analytical_grad = np.array([6.0]) 
num_grad, rel_err = numerical_gradient_check(f, x, analytical_grad) 
print(([float(g) for g in np.round(num_grad, 4)], bool(rel_err < 1e-5)))