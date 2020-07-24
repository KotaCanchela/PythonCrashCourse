# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served,
# and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.

# Add a method called increment_number_served()
# that lets you increment the number of customers who’ve been served. Call this method
# with any number you like that could represent how many customers were served in, say, a day of business.


class Restaurant:
    """Information is stored about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise information about the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints two sentences describing the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name.title()}")
        print(f"The type of cuisine at the restaurant is: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Prints a sentence displaying that the restaurant is open."""
        print(f"The restaurant, {self.restaurant_name.title()} is now open.")

    def set_number_served(self, number):
        """Sets the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, add_number):
        if add_number >= 0:
            self.number_served += add_number
        else:
            print("You can not serve negative people!")


restaurant = Restaurant("mcdonalds", "fast food")
print("")
restaurant.describe_restaurant()
print("")
restaurant.number_served = 23
print(restaurant.number_served)


restaurant.number_served = 43
print(f"The restaurant has served {restaurant.number_served} people")
print("")

# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.

restaurant.set_number_served(55)
print(f"The restaurant has now served {restaurant.number_served} people.")

# Add a method called increment_number_served()
# that lets you increment the number of customers who’ve been served. Call this method
# with any number you like that could represent how many customers were served in, say, a day of business.
print("")
restaurant.set_number_served(0)
restaurant.increment_number_served(15)
print(f"The restaurant has now served {restaurant.number_served} people.")
restaurant.increment_number_served(33)
print(f"The restaurant has now served {restaurant. Lnumber_served} people.")
restaurant.increment_number_served(-5)
