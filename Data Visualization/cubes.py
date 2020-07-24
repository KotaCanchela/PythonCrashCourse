import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [value ** 3 for value in x_values]

plt.style.use('seaborn-notebook')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100, c=y_values, cmap=plt.cm.GnBu)

# Set chart title and label axes

ax.set_title('Cubed Numbers', fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick params
ax.tick_params(axis='both', which='major', labelsize=14)



plt.show()