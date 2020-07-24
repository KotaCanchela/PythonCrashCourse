# This program imports get_formatted_name() from name_function.py.
# The user can enter a series of first and last names, and see the
# formatted full names that are generated:
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"Your neatly formatted name is {formatted_name}")

