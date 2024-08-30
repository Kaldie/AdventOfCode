import matplotlib.pyplot as plt
import numpy as np


61677571
# Define the function you want to plot
def my_function(x):
    return (61677571 - x) * x

# Generate x values
x_values = np.linspace(0, 61677571, 1000)  # Adjust the range and number of points as needed

# Calculate corresponding y values using the function
y_values = my_function(x_values)

# Plot the function
plt.plot(x_values, y_values, label='y = x^2')  # You can change the label as needed
plt.title('Plot of a Function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()  # Display the legend if multiple functions are plotted
plt.grid(True)  # Add a grid for better readability
plt.savefig("fuck.png")