# Writing to an empty file
# Created a programming.txt file that is empty

filename = "10 Files and Exceptions/programming.txt"

with open(
    filename, "w"
) as file_object:  # 'w' tells python that we want to open in write mode
    # can open in 'w' write mode 'r' read mode or 'a' append mode as well as 'r+' which is read and write mode
    # with omitting the argument, with opens as read mode by default
    file_object.write("I love programming.")

# Instantly shows up in the programming.txt file
# Be careful as 'w' write mode erases the contents of the file before returning the file object


# Writing multiple lines

with open(filename, "w") as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games.\n")

# Appending to a file
# Adding content to a file instead of writing over the existing content
# Go into append mode

with open(filename, "a") as file_object:
    file_object.write("\nI also love playing new games.")
    file_object.write("\nIt has been a while since I have played any games.\n")


