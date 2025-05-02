import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=3)

data = np.array([1, 2, 3, 4, 1, 2, 3, 4], dtype=float)
data /= np.linalg.norm(data)  
@qml.qnode(dev)
def circuit():

    qml.AmplitudeEmbedding(features=data, wires=[0, 1, 2], normalize=False)
    qml.Hadamard(wires=0)
    return qml.probs(wires=[0, 1, 2])

probs = circuit()

print("Probabilities of basis states:")
for i, p in enumerate(probs):
    print(f"|{format(i, '03b')}>: {p:.4f}")