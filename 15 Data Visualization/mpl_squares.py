import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]  # This is simply the x values
squares = [1, 4, 9, 16, 25]  # The y values

plt.style.use("seaborn-notebook")

fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=1)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", labelsize=10)

plt.show()
