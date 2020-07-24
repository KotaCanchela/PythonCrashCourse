# Positional arguments
# Need to be in same order that the parameters were written

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('dog', 'nymeria')
describe_pet('hamster', 'james')
# Simply put the first parameter is in the same position as the first argument

# ORDER MATTERS IN POSITIONAL ARGUMENTS

describe_pet('nymeria', 'dog')

# Keyword arguments
# They are name-value pairs passed onto a function
# Don't have to worry about order

print("\n")
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(animal_type='dog', pet_name='nymeria')


# Default values
# Basically setting a default value to a parameter
# Order of parameters had to be changed, default value is at the end

print("\n")


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='nymeria')


# Because no argument is provided for animal_type, it uses the default value dog


describe_pet(pet_name='frank', animal_type='hamster')


# All of the following calls would work for this function
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

