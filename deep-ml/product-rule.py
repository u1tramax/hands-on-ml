import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    df = [f_coeffs[i] * i for i in range(0, len(f_coeffs))]
    dg = [g_coeffs[i] * i for i in range(0, len(g_coeffs))]
    term1 = np.convolve(df, g_coeffs)
    term2 = np.convolve(f_coeffs, dg)
    result = term1 + term2
    if len(result) == 1:
        return result
    return result[1:]


f_coeffs = [5]
g_coeffs = [3, 2]
print(product_rule_derivative(f_coeffs, g_coeffs))