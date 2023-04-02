#creating a new class
import numpy as np
import random
import HebbianLearningRule as hl
import copy


class HopfieldNetwork:

	# static method

	@staticmethod
	def sigma(x):
		return [-1 if i<0 else 1 for i in x]

	def __init__(self, n, m, p=0):
		self.neurons = n
		self.patterns_number = m
		self.patterns = np.zeros((m,n))
		self.createRandomPatterns(m)
		self.starting_pattern = self.perturb_pattern(p)
		self.weights = None
		self.state_history = [self.starting_pattern]



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


	def perturb_pattern(self, n):
		perturbed_pattern = random.randint(0,self.patterns_number-1) # choosing a random pattern
		arr = np.copy(self.patterns[perturbed_pattern])
		print(arr)
		indices = np.random.choice(self.neurons, n, replace=False)   # choosing n random indices to perturb
		arr[indices] *= -1
		return arr


	def pattern_match(self, memorized_patterns, pattern):
		for i in range(self.patterns_number):
			if np.array_equal(memorized_patterns[i], pattern):
				return i+1
		return None

	def update(self, state, weights):
		return np.asarray(HopfieldNetwork.sigma(np.dot(weights, state)))

	def dynamics(self, t_max):
		state = self.starting_pattern
		for i in range(t_max):
			state = self.update(state, self.weights)
			self.state_history.append(state)
			if self.pattern_match(self.patterns, state) != None:
				return self.state_history
		print(f'convergence has not been reached after {t_max} iterations')
		return self.state_history

# i=0
# while i<t_max:
# 	p_new=HopfieldNetwork.sigma(np.dot(self.weights, p))
# 	if np.array_equal(p_new, p):
# 		return p_new
# 	p=p_new
