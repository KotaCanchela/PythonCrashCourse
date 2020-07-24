# Filling a dictionary with user input

responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? \n")
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else would like to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) \n")
    while repeat != 'no' or 'yes':
        repeat = input("Would you like to let another person respond? (yes/no) \n")
        if repeat == 'yes':
            break
        elif repeat == 'no':
            break
    if repeat == 'no':
        polling_active = False #breaks
    elif repeat == 'yes':
         continue

# Polling is complete
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
print(responses)


# Kinda buggy but if any answer was something other than no or yes it would repeat the polling
# Therefore tried to fix it