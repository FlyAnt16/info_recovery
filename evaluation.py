import numpy as np
from paddle_quantum.state.common import random_state
from utils import convert_pauli_to_matrix

def evaluation(n:int, k:int, a_inverse: list, channel:list, p_list: list, p_count, O: np.ndarray, iter: int):
    # Generate 500 random quantum states and compare their true expectation value with recovered expectation value

    mae = 0
    num = 500
    no_mitigation_mae = 0
    for i in range(num):
        new_rho = random_state(n)
        actual = np.trace(np.matmul(O, new_rho.numpy()))

        for l in range(n):
            new_rho = channel[l](new_rho)

        estimate = a_inverse[0]

        for l in range(k):
            a_inverse_l = a_inverse[p_count[l]:p_count[l+1]]
            for P in range(len(p_list[l])):
                p = p_list[l][P]
                p_matrix = convert_pauli_to_matrix(p[0])
                for j in range(1,n):
                    p_matrix = np.kron(p_matrix, convert_pauli_to_matrix(p[j]))
                estimate = estimate + a_inverse_l[P] * np.trace(np.matmul(p_matrix, new_rho.numpy()))
        mae = mae + abs(actual-estimate)
        direct = np.trace(np.matmul(O, new_rho.numpy()))
        no_mitigation_mae = no_mitigation_mae + abs(direct - actual)
    print('iteration number:', iter+1)
    print('mean absolute error:', mae/num)
    print('mean absolute error without error mitigation:', no_mitigation_mae/num)