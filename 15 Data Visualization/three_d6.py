from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some results and store results in a list
results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyse the results

frequencies = []

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Visualise the results

x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling three D6 dice 50,000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

offline.plot({"data": data, "layout": my_layout}, filename="d6_d6_d6.html")

