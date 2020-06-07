from grover import Grover

import time
import sys
from random import seed
from random import randrange
import numpy as np
import matplotlib.pyplot as plt

def main():
	
	groverObject = Grover()

	# constants
	QUBIT_RANGE = 9
	ITERATIONS = 1


	worked = np.zeros(shape=(QUBIT_RANGE, ITERATIONS))
	timing = np.zeros(shape=(QUBIT_RANGE, ITERATIONS))

	print('Testing out Grover\'s alorithm...')

	seed(12345234)
	for n in range(0,QUBIT_RANGE):
		print(f'Trying {n+2}-qubit machine...')

		for j in range(ITERATIONS):
			print(f'Iteration {j+1}...')

			# randomly decide target value
			target = randrange(0,2**(n+2))
			print('Target value: ' + str(target))

			def f(x):
				return (x == target)

			start = time.perf_counter()
			result = groverObject.run(f, n+2)
			end = time.perf_counter()

			worked[n][j] = (result == target)
			timing[n][j] = (end - start)

	qubit_values = []
	for i in range(QUBIT_RANGE):
		qubit_values += [i+2]

	average_runtimes = []
	for i in range(QUBIT_RANGE):
		average_runtimes += [np.mean(timing[i])]

	plt.plot(qubit_values, average_runtimes)
	plt.ylabel('Runtime (s)')
	plt.xlabel('Number of Qubits')
	plt.xticks(qubit_values)
	plt.title('Quantum Simulation Scaling for Grover\'s Algorithm')
	plt.show()


if __name__ == "__main__":
	main()