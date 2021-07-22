from pennylane import *

dev = device('default.qubibt', wires = 2)

# U is a square unitary matrix
U = np.array([[0., -0.70710678, 0., 0.70710678], 
	[0.70710678, 0., -0.70710678, 0.], 
	[0.70710678, 0., 0.70710678, 0.], 
	0., -0.70710678, 0., -0.70710678])
# 0.70710678118 = 1/√2

@qnode(dev)		

def circuit():
	QubitUnitary(U, wires = [0, 1])
	return probs(wires = [0, 1])

print(circuit())	# Returns probability of state 10 and 01 i.e. [0. 0.5 0.5 0.]
print(dev.state)	# Returns the statevector [0.+0.j 0.707+0.j 0.707+0.j 0.+0.j]

'''
def measurement():
	return sample(PauliZ(wires = 0)), sample(PauliZ(wires = 1))
	# Why PauliZ ? It measures -1 or 1 ?

print(circuit())	# Returns probability of state -1 and 1 i.e. [[-1], [1]] ??
# [[-1], [1]] means that the first qubit was in state 0 and second qubit was in state 1!
print(dev.state)	# Returns the statevector [0.+0.j 0.707+0.j 0.707+0.j 0.+0.j]	

'''