import numpy as np
import matplotlib.pyplot as plt

# array of random 10 integer range [1, 100]
integers = np.random.randint(1, 100, size=10)

# creating a histogram
plt.hist(integers, bins=5, edgecolor="black")

# adding label to the histogram
plt.xlabel("Random n integers")
plt.ylabel("frequency")
plt.title("n-integers histogram")

# show plot
plt.show()
