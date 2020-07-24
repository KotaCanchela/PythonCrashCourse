#  Make a class called User. Create two attributes called first_name and last_name,
#  and then create several other attributes that are typically stored in a user profile.
#  Make a method called describe_user() that prints a summary of the user's information.
#  Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


class User:
    """Stores information about a user"""

    def __init__(self, first_name, last_name):
        """Initialise attributes about a person's name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Prints the name of a user"""
        print(f"The user's first name is {self.first_name.title()}")
        print(f"The user's last name is {self.last_name.title()}")

    def greet_user(self):
        """A simple statement greeting a user."""
        print(f"Hello {self.first_name.title()}, I hope that you are doing well today.")


user_0 = User("kota", "canchela")
user_1 = User("gabrielle", "henderson")
user_2 = User("fred", "ng")

list_of_users = [user_0, user_1, user_2]  # added a list for fun and to make it easier

print(f"\nHello {user_0.first_name.title()}")

for user in list_of_users:
    print("")
    user.greet_user()
    user.describe_user()
