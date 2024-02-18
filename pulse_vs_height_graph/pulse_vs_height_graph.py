import json
import matplotlib.pyplot as plt

p = float(input("Input your pulse rate:\t"))
h = float(input("Input your height:\t"))

filename = "data.json"
new_data = {"pulse_rate": p, "height": h}

def read_data(filename: str) -> list:
	""":about: function used to read the data from the give json file
	   :param filename: name of the file which should be read.
	   :return: return the list of pulse rate and height.
	"""

	# function try to read the file else create a empty json file
	try:
		with open(filename, "r") as f:
			existing_data = json.load(f)
	except Exception as error:
		existing_data = write_data(filename)
		print(error)

	return existing_data

def write_data(filename: str, new_data: dict[list] = None, existing_data: dict[list] = None):
	""":about: function used to write a data over the give file"""

	if existing_data and new_data:
		existing_data["pulse_rate"].append(new_data["pulse_rate"])
		existing_data["height"].append(new_data["height"])
	else:
		# default data if their in no data available.
		existing_data = {"pulse_rate": [], "height": []}
	
	with open(filename, "w") as f:
		json.dump(existing_data, f)

	return existing_data

# read the existing data if present if not create the new file
existing_data = read_data(filename)
# write the new input data to the existing data
modified_data = write_data(filename, new_data, existing_data)

# create the bar chart
plt.bar(modified_data["pulse_rate"], modified_data["height"])

# adding the label to the bar chart
plt.xlabel("pulse rate (p)")
plt.ylabel("height (h)")
plt.title("Pulse rate vs height graph")

plt.show()
