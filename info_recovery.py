from paddle_quantum import set_backend
from create_channel import createProductChannel
from generate_pauli import generatePauli
from generate_observable import generateObservable
from generate_data import generateData
from learning_diagonal import learningDiagonal
from evaluation import evaluation
import argparse
import toml
import warnings
warnings.filterwarnings("ignore", category=Warning)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str)
    args = parser.parse_args()
    config = toml.load(args.config)
    N = config.pop('N')
    n = config.pop('n')
    k = config.pop('k')
    num_repeat = config.pop('num_repeat')
    j_x = config.pop('j_x')
    j_y = config.pop('j_y')
    j_z = config.pop('j_z')
    h_z = config.pop('h_z')

    set_backend('density_matrix')
    channel = createProductChannel(n)
    p_list, p_count = generatePauli(n, k)
    O, a_p = generateObservable(n, k, j_x, j_y, j_z, h_z, p_list, p_count)

    for iter in range(num_repeat):
        rho_in, rho_out = generateData(N, n, channel)
        a_inverse = learningDiagonal(N, n, k, rho_in, rho_out, a_p, p_list, p_count)
        evaluation(n, k, a_inverse, channel, p_list, p_count, O, iter)