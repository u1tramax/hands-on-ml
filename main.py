def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    m, n = 0, 0
    for (color, animal) in data:
      if color == x:
        m += 1
        if animal == y:
          n += 1
    return n / m
    
data = [
    ('red', 'cat'),
    ('blue', 'dog'),
    ('red', 'dog'),
    ('red', 'cat'),
    ('blue', 'cat'),
    ('red', 'dog')
]
print(conditional_probability(data, 'red', 'cat'))   # 0.5
print(conditional_probability(data, 'blue', 'cat'))  # 0.5
# print(conditional_probability(data, 'green', 'cat')) # 0.0