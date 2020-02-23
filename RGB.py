import random
for z in range(1,3):
	spalte = "spalte_" + str(z)
	spalte = []
	for n in range(1,145):
		lednumber = "led_" + str(n)
		#print(lednumber)
		lednumber = []
		
		for r in range(1,4):
			color_r = random.randint(0,255)
			lednumber.append(color_r)
			#print(color_r)
		#print(lednumber)
			
		spalte.append(lednumber)
	print("Spalt_" + str(z))
	print(spalte)