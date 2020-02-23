def greet_users(names):
	""" Gruessen Kunden"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)