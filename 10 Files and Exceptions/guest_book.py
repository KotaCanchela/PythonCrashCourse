# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line
# recording their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

filename = "10 Files and Exceptions/guest_book.txt"
while True:
    user_name = input("Please enter your name:\n")
    print("Type 'quit' to quit")
    if user_name == "quit":
        break
    else:
        print(f"Hello, {user_name.title()}. I hope that you are doing well.\n")
        with open(filename, "a") as file_object:
            file_object.write(f"{user_name.title()}\n")
