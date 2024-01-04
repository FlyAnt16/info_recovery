import math
import numpy as np
from utils import convert_int_to_pauli


def insert_identity(p, identity):
    p_list = list(p)
    identity = identity - 1
    for pos in range(len(identity)):
        p_list.insert(identity[pos], 'I')
    p = ''.join(p_list)
    return p


def generatePauli(n, k):
    # Create a list and count for all the n-qubit Pauli operators with weight at most k
    def makeCombiUntil(n, left, k):
        if (k==0):
            tmp_2 = np.asarray(tmp)
            ans.append(tmp_2)
            return
        for i in range(left, n+1):
            tmp.append(i)
            makeCombiUntil(n, i+1, k-1)
            tmp.pop()
    def makeCombi(n, k):
        makeCombiUntil(n, 1, k)
        return ans

    p_list = []
    p_count = [1]
    for l in range(1, k + 1):
        tmp = []
        ans = []
        combi = makeCombi(n, n - l)
        p_l_list = []
        count = 0
        for idx in range(math.comb(n, l)):
            for m in range(pow(3, l)):
                identity = combi[idx]
                p = convert_int_to_pauli(m, l)
                p = insert_identity(p, identity)
                p_l_list.append(p)
                count = count + 1
        p_list.append(p_l_list)
        p_count.append(p_count[l - 1] + count)
    return p_list, p_count