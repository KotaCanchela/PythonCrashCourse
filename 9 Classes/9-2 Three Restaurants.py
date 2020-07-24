# Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance
class Restaurant:
    """Information is stored about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes describing a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints two statements describing a restaurant."""
        print(f"The restaurant's name is {self.restaurant_name.title()}")
        print(f"The type of cuisine at the restaurant is: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Prints a statement displaying that the restaurant is open."""
        print(f"The restaurant, {self.restaurant_name.title()} is now open.")


restaurant_0 = Restaurant("mcdonalds", "fast food")
restaurant_1 = Restaurant("saint antonio", "pizza")
restaurant_2 = Restaurant("Five guys", "burgers")

restaurant_0.describe_restaurant()
print("")
restaurant_1.describe_restaurant()
print("")
restaurant_2.describe_restaurant()
