import numpy as np

class HebbianLearningRule :
	def __init__(self, patterns):
		print('HebbianLearningRule class created')
		self.patterns = patterns
		self.m = patterns.shape[0]
		self.n = patterns.shape[1]


	def sigma(self, x):
		if x >= 0:
			return 1
		else :
			return -1

	def learn(self):
		weights = np.zeros((self.m,self.n, self.n))
		for i in range(self.m):
			weights[i]=self.patterns[i].reshape(self.n, 1)*self.patterns[i]
		weights = np.sum(weights, axis=0)
		np.fill_diagonal(weights, 0)
		self.weights = weights*1/self.m

