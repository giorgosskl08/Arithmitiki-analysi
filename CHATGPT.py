import numpy as np

def QRmine(A):
    n = A.shape[0]
    Q = np.matrix(np.zeros((n, n)))
    R = np.matrix(np.zeros((n, n)))
    for j in range(n):
        q = A[:, j]
        for i in range(j):
            length_of_leg = np.sum(A[:, j] * Q[:, i])
            q = q - length_of_leg * Q[:, i]
            R[i, j] = length_of_leg
        R[j, j] = np.linalg.norm(q)
        Q[:, j] = q / R[j, j]
    return Q, R
