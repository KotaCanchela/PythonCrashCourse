# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarise the order

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)

# favourite languages.py
print("")
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favourite languages are: ")
    elif len(languages) == 1:
        print(f"{name.title()}'s favourite language is: ")
    for language in languages:
        print(f"\t{language.title()}")