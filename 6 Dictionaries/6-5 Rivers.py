# “Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
river_loc = {'nile': 'egypt', 'seine': 'france', 'yangtze': 'china'}
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

for key, value in river_loc.items():
    print(f"The {key.title()} river runs through {value.title()}")

# Use a loop to print the name of each river included in the dictionary.
print(f"\nThe following rivers are in the dictionary:")
for key in river_loc.keys():
    print(f"{key.title()} river ")
# Use a loop to print the name of each country included in the dictionary.”
print(f"\nThe rivers are located in the following countries: ")
for value in river_loc.values():
    print(value.title())