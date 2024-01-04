import numpy as np
import random
from paddle_quantum import get_backend
from paddle_quantum.state.common import zero_state
from paddle_quantum.ansatz import Circuit
from paddle_quantum.shadow import shadow_sample
from tqdm import tqdm


def generateData(N, n, channel):
    # Generate the required data for learning
    # Create random Pauli eigenstates, subject them to noise, then make randomised Pauli measurement on each qubit
    rho_in = np.empty([N, n], dtype='str')
    rho_out = np.empty_like(rho_in, dtype='str')
    rand_state_dict = {1: '0', 2: '1', 3: '+', 4: '-', 5: '<', 6: '>'}
    for i in range(N):
        for j in range(n):
            rand = random.randint(1, 6)
            rho_in[i][j] = rand_state_dict[rand]

    for i in tqdm(range(N)):
        cir2 = Circuit(n)
        state_in = zero_state(n)
        for j in range(n):
            if rho_in[i][j] == '1':
                cir2.x([j], 1)
            elif rho_in[i][j] == '+':
                cir2.h([j], 1)
            elif rho_in[i][j] == '-':
                cir2.x([j], 1)
                cir2.h([j], 1)
            elif rho_in[i][j] == '<':
                cir2.rx(qubits_idx=[j], param=-np.pi / 2)
            elif rho_in[i][j] == '>':
                cir2.rx(qubits_idx=[j], param=np.pi / 2)
        state_in = cir2(state_in)

        for l in range(n):
            state_in = channel[l](state_in)

        state_out = shadow_sample(state=state_in, num_qubits=n, sample_shots=1, mode=get_backend())

        for p_str, res in state_out:
            for j in range(n):
                if p_str[j] == 'z' and res[j] == '0':
                    rho_out[i][j] = '0'
                elif p_str[j] == 'z' and res[j] == '1':
                    rho_out[i][j] = '1'
                elif p_str[j] == 'x' and res[j] == '0':
                    rho_out[i][j] = '+'
                elif p_str[j] == 'x' and res[j] == '1':
                    rho_out[i][j] = '-'
                elif p_str[j] == 'y' and res[j] == '0':
                    rho_out[i][j] = '<'
                elif p_str[j] == 'y' and res[j] == '1':
                    rho_out[i][j] = '>'
    return rho_in, rho_out