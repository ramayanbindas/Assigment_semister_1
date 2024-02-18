quit = "n"  # variable use for quit the program

while quit.lower() != "y":
	conversion = input("Press 'F' to convert Celsius to Fahrenheit or\
						Press 'C' to convert Fahrenheit to Celsius\t").lower()

	if conversion == "f":
		celsius = input("Enter the Celsius:\t")
		
		try:
			celsius = float(celsius)
			fahrenheit = (celsius * (9/5)) + 32
			print("Equals to ", fahrenheit, " Fahrenheit:")
		except:
			print("Celsius should be 'int/float' type")
	elif conversion == "c":
		fahrenheit = input("Enter the Fahrenheit:\t")

		try:
			fahrenheit = float(fahrenheit)
			celsius = (fahrenheit - 32) * (5/9)
			print("Equals to ", celsius, " Celsius")
		except:
			print("Fahrenheit should be 'int/float' type")
	
	else:
		print("Please select among 'F/C'")

	# asking if the user want to quit the program
	quit = input("Do you want to quit? (Y/N)\t")