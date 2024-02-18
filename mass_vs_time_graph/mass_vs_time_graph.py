import numpy as np
import matplotlib.pyplot as plt

hour = int(input("Enter the hour passed from the start of reaction (24-hour format):\t"))

# list of hours range [0, hour]
hour_interval = [h for h in range(0, hour)]

# calculating the mass
mass = [60/(t+2) for t in hour_interval]

# creating the plot
plt.plot(hour_interval, mass, label="H vs M")
plt.xlabel("T(h)")
plt.ylabel("M(gram)")
plt.title("Time vs Mass")

# displaying the plot
plt.show()
