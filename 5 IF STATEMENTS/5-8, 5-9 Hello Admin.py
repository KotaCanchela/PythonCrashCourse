# Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user:
usernames = ['admin', 'kingzwhip', 'frank', 'hopsin', 'king']

# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


if usernames:
    for user in usernames:
        if user in usernames:
            if user == 'admin':
                print(f"Hello {user.title()}, would you like to see a status report?\n")
            elif user in usernames:
                print(f"Hello {user.title()}, thank you for logging in again.\n")


# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed”

usernames = []

if usernames:
    for user in usernames:
        if user in usernames:
            if user == 'admin':
                print(f"Hello {user.title()}, would you like to see a status report?\n")
            elif user in usernames:
                print(f"Hello {user.title()}, thank you for logging in again.\n")
else:
    print("We need to find some users!")
