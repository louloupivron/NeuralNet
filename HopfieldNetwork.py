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
			HebbianLearningRule = hl.HebbianLearningRule(self.patterns)
			HebbianLearningRule.learn()
			self.weights = HebbianLearningRule.weights

	def printWeights(self):
		print(self.weights)

# redefining print function
	def __str__(self):
		s=f"Hopfield network with the following properties:\n"
		s+=f"\tneurons: {self.neurons}\n"
		s+=f"\tpatterns_number: {self.patterns_number}\n"
		s+=f"\tpatterns: \n {self.patterns}\n"
		s+=f"\tweights: \n {self.weights}\n"
		return s


		# print('neurons: ', self.neurons)
		# print('patterns_number: ', self.patterns_number)
		# print('patterns: ', self.patterns)
		# print('weights: ', self.weights)
