# You don’t always have to start from scratch when writing a class.
# If the class you’re writing is a specialized version of another class you,
#  wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes and methods,
#  of the first class.
# The original class is called the parent class, and the new class is the child class.
# The child class can inherit any or all of the attributes and methods of its parent class,
#  but it’s also free to define new attributes and methods of its own.

# When you’re writing a new class based on an existing class,
# you’ll often want to call the __init__() method from the parent class.
# This will initialize any attributes that were defined
# in the parent __init__() method and make them available in the child class.


from modules import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a battery size of {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range of this battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
        elif self.battery_size == 100:
            print("Your car has already been fully upgraded!")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric cars."""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75  # Unique to electriccar class
        self.battery = Battery()

    def describe_battery(self):
        """Describes the battery size."""
        print(
            f"This {self.make.title()} {self.model.title()} has a {self.battery_size}kWh battery."
        )

    def fill_gas_tank(
        self,
    ):  # Imagine this was in parent class. This overrides the method.
        """Fills gas tank."""
        print("An electric car does not have a gas tank!")


my_tesla = ElectricCar("tesla", "model s", "2019")

print(my_tesla.get_descriptive_name())

car = Car("audi", "r8", "2020")

car.read_odometer()

my_tesla.read_odometer()

my_tesla.update_odometer(23)

my_tesla.describe_battery()

# Can override any methods in the parent class

my_tesla.fill_gas_tank()

# Breaking classes into smaller classes
# New class is Battery


my_tesla.battery.describe_battery()

my_tesla.battery.get_range()


# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once,
# and then call get_range() a second time after upgrading the battery.
# You should see an increase in the car’s range.”
print("------------")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\nUpgrading battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
