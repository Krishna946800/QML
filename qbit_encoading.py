from qiskit import QuantumCircuit
from qiskit.circuit.library import Initialize
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 1, 1, 0])
x = x / np.linalg.norm(x)

init_gate = Initialize(x)
qc = QuantumCircuit(2)
qc.append(init_gate, [0, 1])
fig = qc.draw('mpl')
plt.show()
