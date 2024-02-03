import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Read data from the "output.dat" file
data = np.loadtxt("output.dat")

# Extract n, x, and y from the data
n = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# Create a separate stem plot for x_values
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.stem(n, x, linefmt='-', markerfmt='o', basefmt='', label='x_n')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.legend()

# Create a separate stem plot for y_values
plt.subplot(1, 2, 2)
plt.stem(n, y, linefmt='-', markerfmt='o', basefmt='', label='y_n')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('../figs/fig2.png')
plt.show()


