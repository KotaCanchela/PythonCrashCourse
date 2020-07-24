# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt”

filename = "10 Files and Exceptions/guest.txt"

guest_name = input("Please enter your name:\n")

with open(filename, "w") as file_object:
    file_object.write(guest_name)

# This program created a text file and entered the user's input into the text file
