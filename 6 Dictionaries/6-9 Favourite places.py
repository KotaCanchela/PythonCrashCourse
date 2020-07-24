# “Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
# and store one to three favorite places for each person. To make this exercise a bit more interesting,
# ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places = {
    'kota': ['paris', 'london', 'new york city'],
    'sarah': ['london'],
    'james': ['seattle', 'chicago']
}
for name, place in favourite_places.items():
    if len(place) == 1:
        print(f"{name.title()}'s favourite place is:")
    else:
        print(f"{name.title()}'s favourite places are:")
    for city in place:
        print(f"\t{city.title()}")