from random import randint

def rn():
	""" rand_number """
	x = randint(1,6)
	return x
	
for n in range(0,9):
	print(str(rn()))