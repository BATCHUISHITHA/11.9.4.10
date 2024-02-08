import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Read data from the "output.dat" file
data = np.loadtxt("output.dat")

# Extract n, x, and y from the data
n = data[:, 0]
x = data[:, 1]
y = data[:, 2]
Simulation = data[:, 3]

# Create two separate plots
plt.figure(figsize=(12, 6))

# Plot for x(n)
plt.subplot(1, 2, 1)
plt.stem(n, x, linefmt='-', markerfmt='o', basefmt='', label='$x(n)$')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.legend()

# Plot for y(n) and Simulation
plt.subplot(1, 2, 2)
plt.stem(n, y, linefmt='r-', markerfmt='ro', basefmt='r-', label=r'$y(n)$')
plt.stem(n, Simulation, linefmt='g-', markerfmt='gx', basefmt='g-', label='Simulation')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('../figs/fig2.png')
plt.show()


