# full marks of each subject is 100

try:
	math = float(input("Input the marks got in math:\t"))
	physics = float(input("Input the marks got in physics:\t"))
	chemistry = float(input("Input the marks got in chemistry:\t"))

	# calculating the percentage
	percentage = ((math + physics + chemistry) / 300) * 100

	if percentage >= 80:
		print("You got grade 'A'")
	elif percentage >= 70 and percentage < 80:
		print("You got grade 'B'")
	elif percentage >= 60 and percentage < 70:
		print("You got grade 'C'")
	elif percentage >= 40 and percentage < 60:
		print("You got grade 'D'")
	elif percentage < 40:
		print("You got grade 'E'")
except:
	print("all the input should be in 'float' type")