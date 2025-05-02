from PIL import Image
import numpy as np
import pennylane as qml
import matplotlib.pyplot as plt

img = Image.open("eye.png").convert("L").resize((4, 4))
vec = np.array(img).flatten().astype(float)
vec /= np.linalg.norm(vec)  

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def circuit():
    qml.AmplitudeEmbedding(features=vec, wires=range(4), normalize=False)
    return qml.state()

state = circuit()


state = np.array(state).flatten()
print("Quantum state shape:", state.shape)
print("Quantum state:", state)
