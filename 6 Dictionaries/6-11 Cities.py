# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city. The keys for each city’s dictionary should
# be something like country, population, and fact.

cities = {
    'london': {
        'country': 'england',
        'population': 8_982_000,
        'fact': 'london Has 170 museums',
    },
    'paris': {
        'country': 'france',
        'population': 2_148_000,
        'fact': """paris was originally a Roman City called 'lutetia'"""
    },
    'new york city': {
        'country': 'the united states of america',
        'population': 8_399_000,
        'fact': 'the oldest building in the city dates to 1642'
    },
}
# Print the name of each city and all of the information you have stored about it.”

for city, information in cities.items():
    print(f"{city.title()}")
    print(f"\tCountry: {information['country'].title()}\n\t"
          f"Population: {str(information['population'])}\n\t"
          f"Fact: {information['fact'].capitalize()}")