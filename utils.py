def convert_int_to_pauli(input: int, n: int):
    pauli = ''
    for i in range(n):
        y = input // pow(3, n - 1 - i)
        if y == 0:
            pauli += 'X'
        elif y == 1:
            pauli += 'Y'
        elif y == 2:
            pauli += 'Z'
        input = input - y * pow(3, n - 1 - i)
    return pauli

def compare_pauli(pauli: str, state: str):
    if pauli=='I':
        return 1
    elif pauli=='Z' and state=='0':
        return 1
    elif pauli=='Z' and state=='1':
        return -1
    elif pauli=='X' and state=='+':
        return 1
    elif pauli=='X' and state=='-':
        return -1
    elif pauli=='Y' and state=='<':
        return 1
    elif pauli=='Y' and state=='>':
        return -1
    else:
        return 0


def convert_pauli_to_matrix(pauli: str):
    if pauli == 'I':
        return [[1, 0], [0, 1]]
    elif pauli == 'X':
        return [[0, 1], [1, 0]]
    elif pauli == 'Y':
        return [[0, -1.j], [1.j, 0]]
    elif pauli == 'Z':
        return [[1, 0], [0, -1]]
