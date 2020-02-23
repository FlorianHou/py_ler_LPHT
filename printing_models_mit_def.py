def print_models(unprinted_desigs, completed_models):
	"""
	drucken jedes Designs bis keinen genugenden Design. Gedruckte Designs werden nach 'Completeted_Designs' geschiebenn.
	"""
	
	while unprinted_designs:
		current_design = unprinted_designs.pop()
	 	
	 	#Simulation des Process des 3D Print
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
 	"""zeige alle gedrukte Models"""
	print()
	for completed_model in completed_models:
		print(completed_model)
		
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)