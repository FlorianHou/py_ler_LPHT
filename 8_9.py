def show_magicians(zauberern):
	"""zeigen die Name von allen Zauberern"""
	for zauberer in zauberern:
		print("Hier sind die Name von Zauberern: " + zauberer.title())
		
def show_magicians_kopie(zauberern_kopie):
	"""zeigen die Name von allen Zauberern"""
	for zauberer in zauberern_kopie:
		print("Hier sind die Name von Zauberern: " + zauberer.title())

zauberern = ["florian", "xin", "hou","xiang"]
show_magicians_kopie(zauberern)