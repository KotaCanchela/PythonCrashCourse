# An administrator is a special kind of user. Write a class called Admin
# that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores
# a list of strings like "can add post", "can delete post", "can ban user",
#  and so on. Write a method called show_privileges() that lists the
# administrator’s set of privileges. Create an instance of Admin, and call your method.

from modules import User


class Admin(User):
    """Stores information about a user"""

    def __init__(self, first_name, last_name):
        """Initialise attributes about a person's name"""
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        """Shows the user's privileges"""
        print(
            f"{self.first_name.title()} {self.last_name.title()} has the following privileges:"
        )
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}")


username = Admin("Kota", "Canchela")

username.greet_user()


username.describe_user()


print("")

username.privileges = [
    "adminstrator privileges",
    "access to database",
    "can kick or ban users",
]

username.show_privileges()

