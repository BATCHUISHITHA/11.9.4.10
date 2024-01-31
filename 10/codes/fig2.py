import matplotlib.pyplot as plt
import numpy as np

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
n_values = data[:, 0].astype(int)
y_values = data[:, 1].astype(int)

# Add a stem plot
plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt='', label='Stem Plot')

plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()
plt.savefig('../figs/fig2.png')
plt.show()
