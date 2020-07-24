import json

# Load the username if it has been stored previously


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
    filename = "10 Files and Exceptions/usernameso.json"
    if username:
        ask_username = input(
            f"Is your username {username}, if yes please enter 'y' if no, enter 'n'"
        )
    if ask_username == "y":
        print(f"Welcome back {username}.")
    elif ask_username == "n":
        username = get_new_username()
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back {username}!\n")
    while ask_username != "y" or "n":
        print("Please enter a valid response.")
        break


greet_user()

