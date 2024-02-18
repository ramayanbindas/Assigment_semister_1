import matplotlib.pyplot as plt

# acceleration is taken as constant

# initial velocity
initial_vel = float(input("Enter the initial velocity (m/s):\t"))
# acceleration
acc = float(input("Enter the acceleration (m/s^2):\t"))
# time taken
time = float(input("Enter the time taken (sec):\t"))

# list of time
time_interval = [t for t in range(0, round(time))]

# calculating the velocity wrt time
vel = [initial_vel + acc*t for t in time_interval]
# calculating the distance wrt time
dist = [initial_vel*t + 0.5*acc*t**2 for t in time_interval]
# calculating the distance wrt velocity
dist_2 = [(v**2 - initial_vel**2)/2*acc for v in vel]

# Plot each function
plt.figure(figsize=(10, 8))

# creating velocity vs time graph
plt.subplot(2, 2, 1)
plt.plot(time_interval, vel, label='V vs T')
plt.xlabel("T")
plt.ylabel("V")
plt.title('Velocity vs Time')
plt.legend()

# creating distance vs time graph
plt.subplot(2, 2, 2)
plt.plot(time_interval, dist, label='D vs T')
plt.xlabel("T")
plt.ylabel("D")
plt.title('Distance vs Time')
plt.legend()

# creating distance vs velocity graph
plt.subplot(2, 2, 3)
plt.plot(dist_2, vel, label='V vs D')
plt.xlabel("D")
plt.ylabel("V")
plt.title('Distance vs Velocity')
plt.legend()

# displaying the plot
plt.tight_layout()
plt.show()
