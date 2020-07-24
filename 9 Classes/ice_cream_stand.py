# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from
#  the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.”

from modules import Restaurant


class Restaurant_2(Restaurant):
    """Branching off of Restaurant Class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of the Restaurant Class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def display_flavours(self):
        print(f"We have the following list of flavours available")
        for flavour in self.flavours:
            print(f"\t{flavour.title()}")


IceCreamStand = Restaurant_2("burger king", "fast food")

IceCreamStand.describe_restaurant()
IceCreamStand.flavours = ["Chocolate", "vanilla", "strawberry"]

IceCreamStand.display_flavours()
