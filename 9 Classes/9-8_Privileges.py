# Write a separate Privileges class. The class should have one attribute, privileges,
#  that stores a list of strings as described in Exercise 9-7. Move the show_privileges()
# method to this class. Make a Privileges instance as an attribute in the Admin class.
#  Create a new instance of Admin and use your method to show its privileges.

from modules import User


class Admin(User):
    """Stores information about a user"""

    def __init__(self, first_name, last_name):
        """Initialise attributes about a person's name"""
        super().__init__(first_name, last_name)
        """Initialise an empty set of privileges"""
        self.privileges = Privileges()


    def show_privileges(self):
        """Shows the user's privileges"""
        print(
            f"{self.first_name.title()} {self.last_name.title()} has the following privileges:"
        )
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t{privilege.capitalize()}")
        else:
            print("This user has no privileges")


class Privileges():
    def __init__(self, privileges=[]):
        """Initialise privileges for the user."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Shows the user's privileges"""
        print(
            f"User has the following privileges:"
        )
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t{privilege.capitalize()}")
        else:
            print("This user has no privileges")


my_user = Admin('Kota', 'canchela')

my_user.describe_user()
my_user.show_privileges


my_user_privileges = [
    'mod mod any user',
    'can ban who they wish',
    'ability to promote any user'
]

my_user.privileges.privileges = my_user_privileges

my_user.privileges.show_privileges()

