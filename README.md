# Efficient information recovery from Pauli noise via classical shadow
This is the code used to perform the numerical experiments outlined in the paper https://arxiv.org/abs/2305.04148. It's a machine learning algorithm that can remove the effect of Pauli noise when estimating property of noisy quantum state. This is a numerical simulation evaluating the effectiveness of the algorithm.

To run the code, `paddle-quantum` and `toml` is required. Their installation instructions can be found [here](https://qml.baidu.com/install/installation_guide.html) and [here](https://pypi.org/project/toml/).

## Quick Start
The `config.toml` file contains the parameters that can be changed. Additionally, to change the channel used in the numerical experiment, one can change `create_channel.py`.
To run the code, call `python info_recovery.py --config config.toml`.