import numpy as np
from utils import compare_pauli


def learningDiagonal(N:int, n: int, k: int, rho_in: np.ndarray, rho_out: np.ndarray, a_p: np.ndarray, p_list: list, p_count: list) -> list:
    # Learning the matrix M and applies it to the list of coefficients
    M = []
    M.append(np.array([1]))
    for l in range(k):
        M_l = np.zeros((len(p_list[l]), len(p_list[l])))
        for Q in range(len(p_list[l])):
            q = p_list[l][Q]
            x_P = 0
            for i in range(N):
                x_j = 1
                for j in range(n):
                    if q[j] != 'I':
                        x_j = x_j * 3 * compare_pauli(q[j], rho_out[i][j])
                    if q[j] != 'I':
                        x_j = x_j * compare_pauli(q[j], rho_in[i][j])
                    if x_j == 0:
                        break
                x_P = x_P + x_j
            x_P = x_P / N
            a_P = x_P * pow(3, l + 1)
            M_l[Q][Q] = a_P
        M.append(M_l)
    M_inverse = []
    M_inverse.append(np.array([1]))
    for l in range(1, k + 1):
        M_l = M[l]
        M_inverse.append(np.linalg.inv(M_l))

    a_inverse = [a_p[0]]
    for l in range(1, k + 1):
        a_l = a_p[p_count[l - 1]:p_count[l]]
        a_inverse_l = np.matmul(M_inverse[l], a_l)
        a_inverse.extend(a_inverse_l.tolist())
    return a_inverse
