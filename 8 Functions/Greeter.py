# Store functions in a file called modules
# Triple quotes are for a "docstring" (not assigned to anything and documents a segment of code
# Describes what the function does, not how.

def greet_user():
    """Display a simple greeting."""
    print("Hello.")
greet_user()

# Passing information to a function

def greet_user(username):   # Variable username is a parameter (info needed for the function to do its job)
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('kota')    # the value 'kota' is an argument (info passed from call to function)
greet_user('gab')


# Using a function with a while Loop


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop

#while True:
   # print("\nTell me your name:")
   # f_name = input("First name:")
   # l_name = input("Last name:")


# formatted_name = get_formatted_name(f_name, l_name)

# print(f"\nHello, {formatted_name}!")


# No quit condition!

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop


while True:
    print("\nTell me your name:")
    print("Enter 'q' at any time to quit")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)

    print(f"\nHello, {formatted_name}")
