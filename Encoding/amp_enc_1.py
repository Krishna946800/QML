import pennylane as qml
from pennylane import numpy as np


dev = qml.device("default.qubit", wires=2)

data = np.array([0.5, 0.5, 0.5, 0.5])

@qml.qnode(dev)
def circuit():
    
    qml.AmplitudeEmbedding(features=data, wires=[0, 1], normalize=True)
    return qml.state()


state = circuit()
print("Quantum state:\n", state)