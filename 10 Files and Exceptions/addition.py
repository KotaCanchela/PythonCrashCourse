# One common problem when prompting for numerical input occurs when people provide
# text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError.
# Write a program that prompts for two numbers. Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.


def addition():
    """Adds two numbers together and prints the result."""
    try:
        num_1 = int(input("Please enter the first number: "))
        num_2 = int(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        print(num_1 + num_2)


addition()

# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even
# if they make a mistake and enter text instead of a number.


while True:
    try:
        num_1 = input("Please enter the first number: ")
        if num_1 == "q":
            break
        num_1 = int(num_1)
        num_2 = input("Please enter the second number: ")
        if num_2 == "q":
            break
        num_2 = int(num_2)
    except ValueError:
        print("Please enter a valid number.")

    else:
        print(num_1 + num_2)
