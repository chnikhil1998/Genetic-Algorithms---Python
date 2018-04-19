# Genetic algorithm to find the max value of Functions

from random import randint
from math import sin ,radians 
import matplotlib.pyplot as plt

def selection(x_init):
	crossover_prob = 0.8 # Probability of Crossover = 0.8
	p = 100;              # Population size = 50
	bit_size = 8;        # Size of each chromosome
	X = ['0']*int((p*crossover_prob))
	x = x_init

	for i in range(int(p*crossover_prob)):
		a = randint(0,len(x)-1)
		b = randint(0,len(x)-1)
		if int(x[a],2) > int(x[b],2):
			X[i] = x[a]
			x.pop(a)
		else:
			X[i] = x[b]
			x.pop(b)
	return X


def crossover(X):
	crossover_prob = 0.8  # Probability of Crossover = 0.8
	p = 100;                # Population size = 50
	bit_size = 8;         # Size of each chromosome
	Y = ['0']*int((p*crossover_prob))

	for i in range(0,int(p*crossover_prob),2):
		a = randint(0,bit_size-1)
		Y[i]   = X[i][:a]+X[i+1][a:]
		Y[i+1] = X[i+1][:a]+X[i][a:]
	return Y


def mutation(Z):
	mutation_prob = 0.2  # Probability of Mutation = 0.2
	p = 100;               # Population size = 50
	bit_size = 8;        # Size of each chromosome

	for i in range(int(len(Z)*mutation_prob)):
		a = randint(0,len(Z)-1)
		b = randint(0,bit_size-1)
		if Z[a][b] == '0':
			temp = list(Z[a]) 
			temp[b] = '1'
			Z[a] = ''.join(temp)
		else :
			temp = list(Z[a]) 
			temp[b] = '0'
			Z[a] = ''.join(temp)
	return Z












#   Initialisation
p = 100        # Population size = 50
bit_size = 8     # Size of each chromosome




#    First Step - Encoding

x_init = [''.join([str(randint(0,1))for j in range(bit_size)]) for i in range(p)]
x = [x_init[i] for i in range(p)]








# Second Step - Selection

X = selection(x_init)






# Third Step -  Crossover

Y = crossover(X)







# Fourth Step - Mutation 

Z = mutation(x+Y)
func_value = {}
for i in range(len(Z)):
	func_value[sin(radians(int(Z[i],2)))] = Z[i]
sin_value = func_value.keys()
sin_value.sort()
sin_value.reverse()
Z = [func_value[i] for i in  sin_value]



max_ = max(func_value.keys())
diff = max_


while(diff!=0) :
	x_init = [Z[i] for i in range(p)]

	for i in range(p):
		x[i] = x_init[i]
	X = selection(x_init)
	Y = crossover(X)
	Z = mutation(x+Y)
		
	func_value = {}
	for i in range(len(Z)):
		func_value[sin(radians(int(Z[i],2)))] = Z[i]
	sin_value = func_value.keys()
	sin_value.sort()
	sin_value.reverse()
	Z = [func_value[i] for i in sin_value]

	diff = (max(func_value.keys()) - max_) 
	max_ = max(func_value.keys())
	print func_value.keys()
	
print max_
















