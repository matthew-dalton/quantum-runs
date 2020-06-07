from bv import BernsteinVazirani

import time
import sys
from random import seed
from random import randint
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
import bv

def main():
	
	bvObject = BernsteinVazirani()

	# constants
	QUBIT_RANGE = 65
	ITERATIONS = 10


	worked = np.zeros(shape=(QUBIT_RANGE, ITERATIONS))
	timing = np.zeros(shape=(QUBIT_RANGE, ITERATIONS))

	print('Testing out Bernstein-Vazirani alorithm...')

	seed(3245234)
	for n in range(QUBIT_RANGE):
		print(f'Trying {n+3}-qubit machine...')
		for j in range(ITERATIONS):
			print(f'Iteration {j+1}...')

			# randomly decide f
			a = randrange(0,2**(n+1))
			b = randint(0,1)
			hstr = ""
			for i in range(n+2):
				hstr+=str(randint(0,1))
			print(hstr[::-1])
			oracle = bv.bv_oracle(hstr,n+3)
			start = time.perf_counter()
			bvObject.run(oracle, n+2)
			end = time.perf_counter()

			timing[n][j] = (end - start)

	qubit_values = []
	for i in range(QUBIT_RANGE):
		qubit_values += [i+3]

	average_runtimes = []
	for i in range(QUBIT_RANGE):
		average_runtimes += [np.mean(timing[i])]

	plt.plot(qubit_values, average_runtimes)
	plt.ylabel('Runtime (s)')
	plt.xlabel('Number of Qubits')
	plt.xticks(qubit_values)
	plt.title('Quantum Simulation Scaling for Bernstein-Vazirani Algorithm')
	plt.show()

if __name__ == "__main__":
	main()
