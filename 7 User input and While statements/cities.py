# Using break to exit a loop
# Also adding input to dictionary for funsies

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you have finished)\n"

cities_visited = []

# A loop that starts with 'while True' will go forever until it reaches a break statement (no way to add "False")
while True:
    city = input(prompt)
    if city == 'quit':
        break
    elif city != 'quit':
        print(f"{city.title()} has been added to the list of cities visited")
        cities_visited.append(city)
        print(f"Current city list is: \n\t {', '.join(cities_visited).title()}")
