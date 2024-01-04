from paddle_quantum.channel.common import PauliChannel

def createProductChannel(n:int):
    # Create channel used in learning
    channel_0 = PauliChannel([0.1, 0.1, 0.05], qubits_idx=[0], num_qubits=1)
    channel_1 = PauliChannel([0.09, 0.09, 0.05], qubits_idx=[1], num_qubits=1)
    channel_2 = PauliChannel([0.08, 0.08, 0.09], qubits_idx=[2], num_qubits=1)
    channel_3 = PauliChannel([0.05, 0.05, 0.1], qubits_idx=[3], num_qubits=1)
    channel_4 = PauliChannel([0.05, 0.04, 0.01], qubits_idx=[4], num_qubits=1)
    channel_5 = PauliChannel([0.05, 0.2, 0.15], qubits_idx=[5], num_qubits=1)

    channel = [channel_0, channel_1, channel_2, channel_3, channel_4, channel_5]
    return channel[:n]
