#creating a new class
import numpy as np
import HebbianLearningRule as hl


class HopfieldNetwork:

	def __init__(self, n, m):
		self.neurons = n
		self.patterns_number = m
		self.patterns = np.zeros((m,n))
		self.createRandomPatterns(m)


	def createRandomPatterns(self, m):
		for i in range(m):
			self.patterns[i] = np.random.choice([-1,1], self.neurons)

	def printPatterns(self):
		print(self.patterns)

	def learn(self, type):
		if type == 'hebbian':
			HebbianLearningRule = hl.HebbianLearningRule()
			HebbianLearningRule.learn(self.patterns)

