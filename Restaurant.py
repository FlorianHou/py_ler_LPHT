class Restaurant():
	""">>><<<"""
	def __init__(self,restaurant_name,cuisine_type):
		"""reset Name"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		"""Beschreiben das Restaurant"""
		print("Die Name der Restaurant ist " + self.restaurant_name.title())
		print("Cuisine Type ist " + self.cuisine_type.title())
		
	def open_restaurant(self):
		print("Das restaurant ist OFFEN")
		
restaurant_1 = Restaurant("hong kong", "asiatisch")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("vapiano", "italinisch")
restaurant_2.describe_restaurant()