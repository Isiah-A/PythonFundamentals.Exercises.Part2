def exponentiate(x,y):
	"""
	This is for returning the value of the first int 
	raised to the power of the second int
	"""
	return x**y

def raise_to_forth_power(x):
	"""
	This takes one int as an arguement
	and calls the exponentiate function
	to raise the given power to the 4th power
	"""
	return exponentiate(x,4)
	


square = lambda a:  exponentiate(a,2)  	
print(square(2))

cube = lambda b: exponentiate(b,3)
print(cube(2))

print(raise_to_forth_power(2))
