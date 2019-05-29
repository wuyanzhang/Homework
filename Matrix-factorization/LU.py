import numpy as np
def LU_reflection(B):
    """LU分解"""
    A = np.array(B)
    n = len(A)
    L = np.zeros(shape=(n, n))
    U = np.zeros(shape=(n, n))
    for k in range(n - 1):
        gauss_vector = A[:, k]
        gauss_vector[k + 1:] = gauss_vector[k + 1:] / gauss_vector[k]
        gauss_vector[0:k + 1] = np.zeros(k + 1)
        # print(gauss_vector)
        L[:, k] = gauss_vector
        L[k][k] = 1.0
        for l in range(k + 1, n):
            B[l, :] = B[l, :] - gauss_vector[l] * B[k, :]
        A = np.array(B)
    L[k + 1][k + 1] = 1.0
    U = A
    return (L, U)
