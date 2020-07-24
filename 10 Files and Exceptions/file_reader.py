file_path = r"/Users/Kota/Desktop/Python/python/10 Files and Exceptions/pi_digits.txt"  # Absolute path
# r is used as a raw string in case the file path includes a \n to avoid taking it as a line break
with open(file_path) as file_object:
    contents = file_object.read()

print(contents)
# Opens pi_digits.txt, reads, and prints
# However there is an extra blank line at the end of the script

print("-----1-----\n")
with open("10 Files and Exceptions/pi_digits.txt") as file_object:  # Relative path
    contents = file_object.read()

print(contents.rstrip())


# Use a for loop to examine each line at a time
print("-----2-----\n")

with open(file_path) as file_object:
    for line in file_object:
        print(line)
# More blank lines. Therefore we need to rstrip()
print("-----3-----\n")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())


# Making a list of lines from a file
print("-----4-----\n")

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

print(lines)  # Only here to show that the .readlines() created a list


# Attempt to build a single string containing all the digits in the file w/o whitespace

print("-----5-----")

with open(file_path) as file_object:
    lines = file_object.readlines()  # Creates list

pi_string = ""  # Empty string
for line in lines:
    pi_string += (
        line.strip()
    )  # Each line in the list is subsequently added to pi_string
    # With stripping newline character from each line

print(pi_string)  # Prints string
print(len(pi_string))  # Prints amt of chars(digits) in stirng
