# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person_0 = {
    'first_name': 'kota',
    'last_name': 'canchela',
    'age': 22,
    'city': 'paris'
}

print(f"\nFirst name is {person_0['first_name'].title()}")

print(f"Last name is {person_0['last_name'].title()}\n")

print(f"Their age is {str(person_0['age'])}")

print(f"They live in the city of {person_0['city'].title()}")


# 6-7 Person
# Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.
print("")
person_1 = {
    'first_name': 'rick',
    'last_name': 'james',
    'age': 37,
    'city': 'los angeles'
}

person_2 = {
    'first_name': 'will',
    'last_name': 'smith',
    'age': 51,
    'city': 'bel-air'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Full name: {full_name.title()}")
    print(f"\tAge: {str(person['age'])}")
    print(f"\tCity: {person['city'].title()}\n")