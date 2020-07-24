# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that’s being ordered. Call the function three times,
# using a different number of arguments each time.


def make_sandwich(*toppings):
    print("\nThe following toppings have been added to the sandwich:")
    for topping in toppings:
        print(f"\t- {topping}")


make_sandwich('cheese')
make_sandwich('cheese', 'tomato')
make_sandwich('tomato', 'bacon', 'lettuce')