from simon import Simon

import time
import sys
from random import seed
from random import randint
from random import randrange
import numpy as np
import matplotlib.pyplot as plt

def main():
	
	simonObject = Simon()

	# constants
	QUBIT_RANGE = 7
	ITERATIONS = 2


	worked = np.zeros(shape=(QUBIT_RANGE-1, ITERATIONS))
	timing = np.zeros(shape=(QUBIT_RANGE-1, ITERATIONS))

	print('Testing out Simon\'s alorithm...')

	seed(3245234)
	for n in range(2, QUBIT_RANGE+1):
		print(f'Trying {2*n}-qubit machine...')
		for j in range(ITERATIONS):
			print(f'Iteration {j+1}...')

			# randomly decide f
			# for ease of construction, the output for each x,y such that x^y=s is min(x,y)
			s = randint(0,2**n - 1)
			print("S: " + "{0:b}".format(s))
			def f(x):
				return x if (x^s > x) else x^s

			start = time.perf_counter()
			result = simonObject.run(f, n)
			end = time.perf_counter()

			print("Result = " + str(result) + (": Worked" if result == s else ": Failed"))
			print("Timing: " + str(end-start))
			timing[n-2][j] = (end - start)

	qubit_values = []
	for n in range(2, QUBIT_RANGE+1):
		qubit_values += [2*n]

	average_runtimes = []
	for i in range(QUBIT_RANGE-1):
		average_runtimes += [np.mean(timing[i])]

	plt.plot(qubit_values, average_runtimes)
	plt.ylabel('Runtime (s)')
	plt.xlabel('Number of Qubits')
	plt.xticks(qubit_values)
	plt.title('Quantum Simulation Scaling for Simon\'s Algorithm')
	plt.show()

if __name__ == "__main__":
	main()
