import inspect
import math

import inspect 
import numpy as np
from qiskit.quantum_info.operators import Operator
from qiskit import Aer, QuantumCircuit, execute
import matplotlib.pyplot as plt
import sys

class Grover(object):
	"""
	Object that is solely used to construct Grover circuits for different oracles f.
	"""

	def __init__(self):
		pass

	# create phase_flipper gate
	def getFlipper(self, n):

		# create empty matrix
		flipper = np.zeros(shape=(2**n, 2**n))

		# flip amplitude signs for all inputs
		for i in range(2**n):
			flipper[i][i] = -1

		return flipper

	# create Z_0 gate
	def getHelper(self, n):
		
		# create empty matrix
		helper = np.zeros(shape=(2**n, 2**n))

		# flip amplitude sign for input 0^n
		helper[0][0] = -1

		# identity operator for all other inputs
		for i in range(1, 2**n):
			helper[i][i] = 1

		return helper

	# create Z_f gate
	def getOracle(self, f, n):

		# create empty oracle U_f
		oracle = np.zeros(shape=(2**n, 2**n))

		# flip amplitude for all inputs where f(x) = 1
		for i in range(2**n):
			oracle[i][i] = -1 if (f(i) == 1) else 1
		return oracle


	def run(self, f, n):
		# execute circuit on smallest possible qc available
		backend = Aer.get_backend('qasm_simulator')
		return self.execute(self.get_circuit(f, n),backend)


	def get_circuit(self, f, n_qubits):

		# make oracle gate Z_f
		oracle = Operator(self.getOracle(f,n_qubits))
		# make helper gate Z_0
		helper = Operator(self.getHelper(n_qubits))

		# make flipper gate -I
		flipper = Operator(self.getFlipper(n_qubits))

		# make circuit
		p = QuantumCircuit(n_qubits+1, n_qubits)

		# apply the first hadamard to all qubits
		for i in range(n_qubits):
			p.h(i)

		# apply oracle and diffuser designated amount of times
		NUM_ITERATIONS = int(math.sqrt(2**n_qubits) * math.pi / 4)
		for _ in range(NUM_ITERATIONS):

			# apply oracle
			p.append(oracle, reversed(range(n_qubits)))

			# apply diffuser
			for i in range(n_qubits):
				p.h(i)
			p.append(helper,range(n_qubits))
			for i in range(n_qubits):
				p.h(i)
			p.append(flipper, range(n_qubits))

		p.measure(range(0,n_qubits),range(0,n_qubits))
		return p


	def execute(self, p, backend):

		# run and measure circuit using 1 trial
		# print(to_latex(p))
		job = execute(p, backend)
		result = job.result().get_counts()
		return result