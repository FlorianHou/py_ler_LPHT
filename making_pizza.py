def make_pizza(size, *toppings):
	"""Durcken alle Zutat"""
	print("\nMaking a " + str(size) + 
	" inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)