filename = 'guests.txt'

while True:	
	name = input("Biite geben Sie Ihr Name ein. : ")
	if name == "q":
		break
		
	else:
		with open(filename,'a') as file_object:
			file_object.write(name.title() + "\sn")
		