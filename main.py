#####
#imports
#####

import numpy as np
import cmath
import HopfieldNetwork as hn
import HebbianLearningRule as hl



if __name__ == '__main__':
	print('main.py is being run directly')

	HopfieldN = hn.HopfieldNetwork(50,3)
	HopfieldN.printPatterns()
	HopfieldN.learn(type='hebbian')






else:
	print('main.py has been imported')

