# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.

pet_0 = {
    'animal': 'dog',
    'owner': 'kota',
    'price': 500
}

pet_1 = {
    'animal': 'frog',
    'owner': 'kyle',
    'price': 20
}

pet_2 = {
    'animal': 'snake',
    'owner': 'slytherin',
    'price': 1000
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['owner'].title()} owns a pet {pet['animal']}.\n"
          f"They bought their pet {pet['animal']} for {str(pet['price'])}$.\n")