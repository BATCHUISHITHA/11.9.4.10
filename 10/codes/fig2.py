import matplotlib.pyplot as plt

# Define the sequence function
def sequence(n):
    return (2 * n - 1) ** 2

# Generate x values (e.g., n values)
x_values = range(0, 15)

# Generate y values using the sequence function
y_values = [sequence(n) for n in x_values]

# Plot the graph
plt.plot(x_values, y_values, marker='o')
plt.title('Graph of (2n-1)^2')
plt.xlabel('n')
plt.ylabel('(2n-1)^2')
plt.grid(True)

# Save the plot as a PNG (should be before plt.show())
plt.savefig('fig2.png')

# Display the plot
plt.show()

