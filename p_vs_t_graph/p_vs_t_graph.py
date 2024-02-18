import numpy as np
import matplotlib.pyplot as plt

hour = int(input("Enter the current hour (24-hour format):\t"))

# list of hours range [0, hour]
hour_interval = [h for h in range(0, hour)]

# calculating the population
population = [(15000 * (1+h))/(15+np.e) for h in hour_interval]

# creating the plot
plt.plot(population, hour_interval, label="T vs P")
plt.xlabel("population")
plt.ylabel("time(h)")
plt.title("Population vs Time")

plt.show()
