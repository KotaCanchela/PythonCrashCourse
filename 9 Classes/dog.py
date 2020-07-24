# This class will tell Python how to make an object representing a dog.
# Each instance created from the Dog class will store a name and an age,
# and we’ll give each dog the ability to sit() and roll_over():
# __init__ is a special method that runs automatically whenever
# we create a new instance based on the Dog class
# self must come first before other parameters and is required in the method definition
# self gives an individual access to the attributes and methods in the class.
# we pass dog() a name and age as arguments. self is passed automatically
# therefore we only provide values for the last two parameters: name and age


class Dog:  # Capitalised names refer to classes
    """A simple statement to model a dog."""

    def __init__(self, name, age):  # A function that is part of a class is a "method"
        """Initialise name and age attributes."""
        self.name = name  # self.name takes value from the parameter name in __init__ & assigns it to variable name
        self.age = age  # variables accessible like this are called attributes

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Making an instance from a class
# Think of a class as a set of instructions for how to make an instance.
# The class Dog is a set of instructions that tells Python
# how to make individual instances representing specific dogs.

my_dog = Dog(
    "Willie", 6
)  # Lower class my_dog represents an instance from the class Dog

print(f"My dog is {my_dog.name}.")  # my_dog.name is accessing the attribute "name"
print(f"My dog is {my_dog.age} years old.")
print(
    my_dog
)  # prints attributes of the object (<__main__.Dog object at 0x7fd3faf831c0>)
print("")
# Calling methods

my_dog.sit()  # No need to do print(f"{my_dog.sit()") because there is already a print call in the method
my_dog.roll_over()  # dot notation is needed
print("")

# Creating multiple instances
my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
