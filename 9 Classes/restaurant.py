# Make a class called Restaurant.
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
    """Information is stored about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}")
        print(f"The type of cuisine at the restaurant is: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The restaurant, {self.restaurant_name.title()} is now open.")


restaurant = Restaurant("mirazur", "french gourmet")

print(
    f"I am going to {restaurant.restaurant_name.title()} to eat some {restaurant.cuisine_type.title()}"
)
print("")
restaurant.describe_restaurant()
print("")
restaurant.open_restaurant()
