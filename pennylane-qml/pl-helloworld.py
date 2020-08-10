from pennylane import *

dev = device('default.qubibt', wires = 2)	# No. of qubits represented by wires
# default.qubit is the deafult simulator

@qnode(dev)		# Connect the device to the program below

def circuit():
	# The circuit currently does nothing
	return probs(wires = [0, 1])

print(circuit())	# Returns probability of state 00 i.e. [1. 0. 0. 0.]
print(dev.state)	# Returns the statevector [1.+0.j 0.+0.j 0.+0.j 0.+0.j]