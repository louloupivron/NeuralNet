#####
#imports
#####

import numpy as np
import cmath
import HopfieldNetwork as hn
import HebbianLearningRule as hl



if __name__ == '__main__':


	### set parameters of the network ###

	# number of neurons
	n = 50
	# number of patterns
	m = 3
	# number of perturbations
	p = 3
	# number of iterations
	iterations = 100




	print('main.py is being run directly')

	HopfieldN = hn.HopfieldNetwork(50,3)
	HopfieldN.learn(type='hebbian')
	print(HopfieldN)
	HopfieldN.dynamics(iterations)









else:
	print('main.py has been imported')

