import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.


def remember_load():
    """Greet the user by name."""
    filename = "10 Files and Exceptions/usernames.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, "a") as g:
            json.dump(username, g)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back {username}!")


remember_load()

# Let's refactor this
print("\n-----Refactor part 1-----\n")


def get_stored_username():
    """Get stored username if available"""
    filename = "10 Files and Exceptions/usernameso.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        username = input("Please enter your username: ")
        filename = "10 Files and Exceptions/usernameso.json"
        with open(filename, "a") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back {username}")


greet_user()


# If we want to refactor even more
print("\n-----Refactor part 2-----\n")


def get_new_username():
    """Prompt for a new username."""
    username = input("Please enter your username. ")
    filename = "10 Files and Exceptions/usernameso.json"
    with open(filename, "a") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}\n")
    else:
        username = get_new_username()
        with open(filename, "a") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back {username}!\n")


greet_user()


# END PRODUCT


def get_stored_username():
    """Get stored username if available"""
    filename = "10 Files and Exceptions/usernameso.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("Please enter your username. ")
    filename = "10 Files and Exceptions/usernameso.json"
    with open(filename, "a") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        ask_user = input(
            f"Welcome back, are you {username}? Enter 'y' if yes or 'n' if you are a new user."
        )
        if ask_user == "y":
            print(f"Welcome back, are you {username}?\n")
        else:
            username = get_new_username()
            with open(filename, "a") as f:
                json.dump(username, f)
                print(f"We'll remember you when you come back {username}!\n"


# 1 0-13. Verify User: The final listing for remember_me.py assumes either that
# the user has already entered their username or that the program is running
# for the first time. We should modify it in case the current user is not the
# person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this
# is the correct username. If it’s not, call get_new_username() to get the correct username.