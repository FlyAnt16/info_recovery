import numpy as np
from paddle_quantum.trotter import get_1d_heisenberg_hamiltonian
from utils import convert_pauli_to_matrix

def generateObservable(n: int, k:int, j_x: float, j_y: float, j_z: float, h_z: float, p_list:list, p_count: list) -> np.ndarray:
    # Create a heisenberg-like observable and decompose it in Pauli basis, return its matrix form and the list of coefficients
    observable = get_1d_heisenberg_hamiltonian(length=n, j_x=j_x, j_y=j_y, j_z=j_z, h_z=h_z,
                                               periodic_boundary_condition=False)
    O = observable.construct_h_matrix()
    O = O / max(abs(np.linalg.eigvalsh(O)))
    a_p = np.zeros(p_count[-1])
    a_p[0] = np.trace(O) / pow(2, n)
    index = 1
    for l in range(k):
        for idx in range(len(p_list[l])):
            p = p_list[l][idx]
            p_matrix = convert_pauli_to_matrix(p[0])
            for j in range(1, n):
                p_matrix = np.kron(p_matrix, convert_pauli_to_matrix(p[j]))
            a_p[index] = np.trace(np.matmul(O, p_matrix)) / pow(2, n)
            index = index + 1
    return O, a_p