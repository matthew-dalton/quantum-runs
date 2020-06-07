import inspect 
import numpy as np
from qiskit.quantum_info.operators import Operator
from qiskit import Aer, QuantumCircuit, execute
import matplotlib.pyplot as plt
import sys

def bv_oracle(s, n):
	oracle_qc = QuantumCircuit(n)
	q = 0

	for char in s:
		if char == "1":
			oracle_qc.cx(q,n-1)
		q += 1
	oracle_gate = oracle_qc.to_gate()
	return oracle_gate
class BernsteinVazirani(object):

	def __init__(self):
		pass



	def run(self, U_f, n):
		# execute circuit on smallest possible qc available
		backend = Aer.get_backend('qasm_simulator')
		circ = self.get_circuit(U_f,n)
		result = self.execute(circ, backend)
		print(result)
		return result


	def get_circuit(self, U_f, n_qubits):

		# construct oracle and define its gate constructor
		# construct oracle and define its gate constructor
		# make circuit
		circ = QuantumCircuit(n_qubits+1, n_qubits+1)
		# apply the first hadamard to all qubits
		for i in range(n_qubits):
			circ.h(i)

		# NOT ancilla qubit then apply hadamard
		circ.x(n_qubits)
		circ.h(n_qubits)
		# apply oracle to all qubits
		circ.append(U_f, range(n_qubits+1))

		# apply hadamard to computational qubits
		for i in range(n_qubits):
			circ.h(i)
		circ.measure(range(0,n_qubits+1),range(0,n_qubits+1))
		return circ

		return circ


	def execute(self, circ, backend):
		job = execute(circ, backend)
		result = job.result().get_counts()
		return result
