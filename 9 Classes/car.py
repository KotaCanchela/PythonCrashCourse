# Working with classes and instances


class Car:
    """A simple statement to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2019)

print(my_new_car.get_descriptive_name())
print(f"I have just purchased a {my_new_car.get_descriptive_name()}")

print(f"{my_new_car.year}")
print("")

# Add an attribute that changes over time
# Also a default value here


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


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying attribute values can be done in 3 ways:

# Modifying an attribute value directly


print("")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Modifying an attribute's value through a method


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
        """Set the odometer reading to a given value."""
        self.odometer_reading = mileage


print("-------------")
my_new_car = Car("audi", "a4", 2019)
my_new_car.update_odometer(55)
my_new_car.read_odometer()


# We can extend the method .read_odometer to do additional work every time the reading is modified


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


print("--------------")

my_new_car = Car("audi", "a4", 2019)

my_new_car.read_odometer()  # 0 by default

my_new_car.update_odometer(22)  # my_new_car new updated value is 22
my_new_car.read_odometer()

my_new_car.update_odometer(15)  # tried to go to 15 but it could not
my_new_car.read_odometer()


# Incrementing an attribute's value through a method


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


print("----------------")
print("")
my_used_car = Car("subaru", "outback", "2015")
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(500)
my_used_car.read_odometer()
