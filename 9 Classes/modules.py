class Car:
    """A simple statement to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You need to add a positive number")


class Laptop:
    """A simple statement to represent a laptop."""

    def __init__(self, price, screen_size, ram, make):
        """Initialise attributes to describe a laptop."""

        self.price = price
        self.screen_size = screen_size
        self.ram = ram
        self.make = make
        self.keyboard = Keyboard()

    def get_price(self,):
        """Retrieves price of laptop."""
        print(f"The {self.make.title()} laptop costs approximately ${self.price}.")

    def get_ram(self):
        """Retrieves the ram of the laptop."""
        print(f"The {self.make.title()} laptop has approximately {self.ram}GB of RAM.")

    def get_screen_size(self):
        """Retrieves the screen size of the laptop."""
        print(
            f"The {self.make.title()} laptop has a screen size of {self.screen_size} inches."
        )


class Keyboard:
    """A simple statement to describe a keyboard."""

    def __init__(self, keyboard="Logitech"):
        """Initialise attributes describing a keyboard."""
        self.keyboard = keyboard

    def get_keyboard(self):
        """Prints a statement describing the keyboard."""

        print(f"My computer comes with an excellent {self.keyboard} keyboard.")


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


class User:
    """Stores information about a user"""

    def __init__(self, first_name, last_name):
        """Initialise attributes about a person's name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Prints the name of a user"""
        print(f"The user's first name is {self.first_name.title()}")
        print(f"The user's last name is {self.last_name.title()}")

    def greet_user(self):
        """A simple statement greeting a user."""
        print(f"Hello {self.first_name.title()}, I hope that you are doing well today.")

    def increment_login_attempts(self, attempt):
        """Increments the login attempts."""
        if attempt >= 0:
            self.login_attempts += attempt
        else:
            print("You can not decrease the login attempts!")

    def reset_login_attempts(self):
        """Resets the login attempts"""
        self.login_attempts = 0
        print(
            f"The user's login attempts have been reset. They are now at: {self.login_attempts}"
        )
