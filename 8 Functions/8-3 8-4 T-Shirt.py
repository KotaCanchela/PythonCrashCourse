# Write a function called make_shirt()
# that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.


def make_shirt(size, text):
    """Print a sentence summarizing the size of the shirt
    and the message printed on it."""
    print(f"\nI have ordered a size {size} t-shirt.")
    print(f"My size {size} t-shirt will have the following text printed on it:\n\t{text.capitalize()}")


make_shirt('medium', 'math is the best')
make_shirt(size='large', text='merry chrysler')


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

print("\n")


def make_shirt(size='large', text='I love python'):
    """Print a sentence summarizing the size of the shirt
    and the message printed on it."""
    print(f"\nI have order a size {size} t-shirt.")
    print(f"My size {size} t-shirt will have the following text printed on it:\n\t{text.capitalize()}")


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='python is weird')