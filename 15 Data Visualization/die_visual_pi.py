from die import Die
import plotly.graph_objects as go

# Create a D6

die_1 = Die()
die_2 = Die()

# Make some results and store results in a list
results = []

for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results

frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Visualise the results

labels = list(range(2, max_result + 1))
values = frequencies

fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            textinfo="label+percent",
            insidetextorientation="radial",
        )
    ]
)
fig.show()
