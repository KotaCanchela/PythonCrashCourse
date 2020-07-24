# Prompt user for their name and remember it

import json


def prompt_user():
    username = input("What is your name? ")
    filename = "10 Files and Exceptions/username.json"
    with open(filename, "a") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")


prompt_user()
