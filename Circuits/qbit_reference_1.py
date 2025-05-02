from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
qc = QuantumCircuit(2)
print(qc.qubits)
qc.x(0)
qc.cx(0, 1)
qc.h([0, 1])
print(qc.data)
fig1 = qc.draw("mpl")
fig2 =qc.data[0].operation.definition.draw("mpl")
qc.measure_all()
plt.show()