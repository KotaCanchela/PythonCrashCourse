# Write a program that prompts for the user’s favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message, “I know your favorite number! It’s _____.”
import json

def ask_number():
    """Asks the user for their favourite number and stores it."""
    filename = '10 Files and Exceptions/favourite_number.json'
    ask_number = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(ask_number, f)
    return filename

def remember_number():
    filename = '10 Files and Exceptions/favourite_number.json'
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"Your favourite number is {number}")


ask_number()

remember_number()
