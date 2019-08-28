import numpy as np
from cvxopt import matrix as cvxopt_matrix
from cvxopt import solvers as cvxopt_solvers


class SupportVectorMachine:
    def __init__(self, C=10):
        self.C = 10
        self.w = None
        self.b = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)

        m,n = X.shape
        y = y.reshape(-1,1) * 1.
        X_dash = y * X
        H = np.dot(X_dash , X_dash.T) * 1.

        # Quadratic Programming
        P = cvxopt_matrix(H)
        q = cvxopt_matrix(-np.ones((m, 1)))
        G = cvxopt_matrix(np.vstack((np.eye(m)*-1,np.eye(m))))
        h = cvxopt_matrix(np.hstack((np.zeros(m), np.ones(m) * self.C)))
        A = cvxopt_matrix(y.reshape(1, -1))
        b = cvxopt_matrix(np.zeros(1))

        # Run solver
        cvxopt_solvers.options['show_progress'] = False
        sol = cvxopt_solvers.qp(P, q, G, h, A, b)
        alphas = np.array(sol['x'])

        # Compute the weights and bias
        self.w = ((y * alphas).T @ X).reshape(-1,1)
        S = (alphas > 1e-4).flatten()
        self.b = np.mean(y[S] - np.dot(X[S], self.w))

    def predict(self, X):
        return np.sign(X@self.w + self.b)
