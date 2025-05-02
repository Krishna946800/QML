from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate
import matplotlib.pyplot as plt
mcx_gate = MCXGate(3)
hadamard_gate = HGate()
 
qc = QuantumCircuit(4)
qc.append(hadamard_gate, [0])
qc.append(mcx_gate, [0, 1, 2, 3])
qc.x([0, 1])
qc.y([2, 3])
qc.z([1, 3])
print(qc.data)
fig1 = qc.draw("mpl")
plt.show()