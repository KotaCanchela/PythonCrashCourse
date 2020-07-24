# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

dream_vacation = {}
polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("If you could travel one place in the world, where would you go?\n")
    dream_vacation[name] = response
    repeat = input("Would you like to ask another person? (yes/no)\n")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in dream_vacation.items():
    print(f"{name.title()} would like to travel to {response.title()}")
