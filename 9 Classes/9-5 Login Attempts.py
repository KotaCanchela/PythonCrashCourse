# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.


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


print("")

user = User("kota", "canchela")
user.greet_user()
user.describe_user()
print(f"The user has made {user.login_attempts} login attempts.")

print("--------")
print("")
user.increment_login_attempts(10)
print(f"The user has now made {user.login_attempts} login attempts")

print("--------")
print("")
user.increment_login_attempts(25)
print(f"The user has now made {user.login_attempts} login attempts")
user.increment_login_attempts(-5)

print("--------")
print("")
user.reset_login_attempts()
print(f"The user has now made {user.login_attempts} login attempts")  # further proof
