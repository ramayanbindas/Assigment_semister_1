try: # complex number are not allowed
	num = float(input("Please enter any number:\t"))

	if num >= 0:
		print("The", num, "is positive")
	else:
		print("The", num, "is negative")
except:
	print("The input must be a number")
