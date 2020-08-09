import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt

tensor_data = torch.tensor([(0, 0), (0.1, 0.1), (0.2, 0.2)])	# (data, label)

def function(phi, input_data = None):
	return phi*input_data	# Some Linear model/function.

def loss_function(output, label):
	return torch.abs(a-b)**2	# Mean Square loss

def gradient(phi):		# Minimize the average loss i.e. Gradient Descent
	c = 0
	for data, label in data:
		c += loss_function(function(phi, x = data), label)
	return c

if __name__ == '__main__':
	phi = Variable(torch.tensor(0.1), requires_grad = True)
	opt = torch.optim.Adam([phi], lr = 0.01)	# Adam Optimizer with learning rate of 0.01

	for i in range(5):
		loss = gradient(phi)
		loss.backward()		# Gradients i.e. move backwards
		opt.step() 			# Update parameters