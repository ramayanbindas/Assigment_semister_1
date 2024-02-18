import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Sine function
y_sin = np.sin(x)

# Cosine function
y_cos = np.cos(x)

# Polynomial function (quadratic)
y_poly = x**2 - 2*x + 1

# Exponential function
y_exp = np.exp(x)

# Plot each function
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_sin, label='sin(x)')
plt.title('Sine Function')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, y_cos, label='cos(x)')
plt.title('Cosine Function')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, y_poly, label='x^2 - 2x + 1')
plt.title('Polynomial Function')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, y_exp, label='e^x')
plt.title('Exponential Function')
plt.legend()

plt.tight_layout()
plt.show()

