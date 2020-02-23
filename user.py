class User():
	def __init__(self,first_name,last_name):
		"""reset Name"""
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts  = 0
		
	def describe_user(self):
		"""Information des Kunde"""
		print("first_name: " + self.first_name)
		print("last_name: " + self.last_name)
		
	def greet_user(self):
		"""Gruessen Kunde"""
		print("Hallo!" + self.first_name.title() + self.last_name.title())
	
	def increment_login_attempts(self):
		"""attempt +1"""
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		"""reset attempt"""
		self.login_attempts = 0
				
Kunde_1 = User("hou", "zhaoyang")
print(Kunde_1.first_name)
Kunde_1.describe_user()
Kunde_1.greet_user()
Kunde_1.increment_login_attempts()
Kunde_1.increment_login_attempts()
Kunde_1.increment_login_attempts()
print("Du hast " + str(Kunde_1.login_attempts) + " mals versucht!!")