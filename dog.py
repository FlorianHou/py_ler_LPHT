class Dog():
	"""simulieren einen Hund"""
	
	def __init__(self, name,age):
		"""reset die Eigenschaften von Hund"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""anordnen Ducken"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""waelzen"""
		print(self.name.title() + " rolled over!")
	
	
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()