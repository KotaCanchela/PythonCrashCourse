import matplotlib.pyplot as plt

x_values = range(1, 101)  # Range of x-values from 1 to 100
y_values = [x ** 2 for x in x_values]  # The square of each subsequent x-value

plt.style.use("seaborn-notebook")

fig, ax = plt.subplots()
ax.scatter(
    x_values, y_values, s=10, c="red"
)  # S = size of dots C = colour. Can also be in RGB model (0, 0.8 0) for light green

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis

ax.axis(
    [0, 105, 0, 11000]
)  # First two numbers means from the values 0 - 105 on the x-axis
# the next 2 numbers are the values 0 to 11000 on the y-axis

plt.show()
