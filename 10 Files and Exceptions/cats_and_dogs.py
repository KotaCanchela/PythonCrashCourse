# Make two files, cats.txt and dogs.txt. Store at least three names of cats
# in the first file and three names of dogs in the second file. Write a program
# that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error, and print
# a friendly message if a file is missing. Move one of the files to a different location
# on your system, and make sure the code in the except block executes properly.

from pathlib import Path


def read_file(filename):
    """Reads and prints the contents of a file to the screen"""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Unfortunately your file {Path(filename).stem} could not be found.")
    else:
        print(contents)


filename = ""

filenames = [
    "10 Files and Exceptions/dogs.txt",
    "10 Files and Exceptions/cats.txt",
    "10 Files and Exceptions/hamsters.txt",
]

for filename in filenames:
    read_file(filename)


# 10-9 SILENT CATS AND DOGS
# Modify your except block in Exercise 10-8 to fail silently if either file is missing

print("\n----SILENT CATS AND DOGS----\n")


def read_file(filename):
    """Reads and prints the contents of a file to the screen"""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


for filename in filenames:
    read_file(filename)
