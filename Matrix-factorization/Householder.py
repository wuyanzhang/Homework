import numpy as np
def householder_reflection(A):
    """Householder变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    for cnt in range(r - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_cnt)  # Q=H(n-1)*...*H(2)*H(1)  H为自逆矩阵
    return (Q, R)
