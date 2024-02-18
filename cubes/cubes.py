try:
	num = float(input("Enter any number:\t"))

	cube = num**3

	print(f"Cube of {num} is {cube}")
except:
	print("input must be a number")