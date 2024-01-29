import matplotlib.pyplot as plt
import numpy as np

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
n_values = data[:, 0].astype(int)
y_values = data[:, 1].astype(int)

# Create a plot with a line plot
plt.plot(n_values, y_values, marker='o', linestyle='-', color='b', label='Line Plot')

# Add a stem plot
plt.stem(n_values, y_values, linefmt=':', markerfmt='r^', basefmt='b', label='Stem Plot')

plt.xlabel('n_values')
plt.ylabel('y_values')
plt.title('Plot of n_values vs y_values with Stem Plot')
plt.grid(True)
plt.legend()
plt.savefig('../figs/fig2.png')
plt.show()
