# Passing an arbitrary number of arguments
# Sometimes you won’t know ahead of time how many arguments a function needs to accept.
# Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

# For example, consider a function that builds a pizza.
# It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want.
# The function in the following example has one parameter, *toppings,
# but this parameter collects as many arguments as the calling line provides:


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python
# to make an empty tuple called toppings and pack whatever values it receives into this tuple.

# Otherwise there would be an error :TypeError: make_pizza() takes 1 positional argument but 3 were given
# Python packs the arguments into a tuple


def make_pizza(*toppings):
    """Summarize the pizza that we are about to make."""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Now the arguments are not packed in a tuple thanks to the for loop it responds to each value appropriately


# Mixing positional and arbitrary arguments
# If you want a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be placed last in the function definition


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"""\nMaking a {size}" pizza with the following toppings:""")
    for topping in toppings:
        print(f"\t- {topping}")


make_pizza(16, 'pepperoni')    # The size goes first as it is positional
make_pizza(18, 'mushrooms', 'green peppers', 'extra cheese')
