import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyLogisticRegression:
    
    learning_rate = 0.01
    iterations = 10000
    threshold = 0.5

    def fit(self, X, y):

        m, n = X.shape
        X = np.c_[np.ones(m), X]
        n += 1
        theta = np.zeros(n)

        def logistic_func(z):
            return 1 / (1 + np.exp(-z))
        
        def gradient_logit(X, y):
            return (1 / m) * (X.T @ (logistic_func(X @ theta) - y))

        for _ in range(self.iterations):
            theta -= self.learning_rate * gradient_logit(X, y)

        self.theta = theta
        print(theta)

    def predict_proba(self, X):
        
        X = np.c_[np.ones(X.shape[0]), X]
        return 1 / (1 + np.exp(-(X @ self.theta)))
    
    def predict(self, X):

        return (self.predict_proba(X) >= self.threshold).astype(int)