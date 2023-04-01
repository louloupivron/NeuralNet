import numpy as np

class HebbianLearningRule :
	def __init__(self):
		print('HebbianLearningRule class created')

	def sigma(self, x):
		if x >= 0:
			return 1
		else :
			return -1

	def learn(self, patterns):
		self.weights = np.zeros((patterns.shape[1], patterns.shape[1]))
		for i in range(patterns.shape[0]):
			


