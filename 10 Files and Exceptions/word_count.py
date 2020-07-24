# To add onto the alice.py file, if we want to add more files to analyse...
from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(
            f"Sorry, the file '{Path(filename).stem}' could not be found."
        )  # Path(filename).stem allows us to remove the /Users/Kota/Desktop/pcc_2e-master/chapter_10/
    else:
        words = contents.split()
        num_words = len(words)
        print(
            f"The file '{Path(filename).stem}' contains approximately {num_words} words."
        )


filename = ""

filenames = [
    "/Users/Kota/Desktop/pcc_2e-master/chapter_10/siddhartha.txt",
    "/Users/Kota/Desktop/pcc_2e-master/chapter_10/alice.txt",
    "/Users/Kota/Desktop/pcc_2e-master/chapter_10/little_women.txt",
    "/Users/Kota/Desktop/pcc_2e-master/chapter_10/moby_dick.txt",
    "/Users/Kota/Desktop/pcc_2e-master/chapter_10/non_existant_file.txt",
]

for filename in filenames:
    count_words(filename)

# This function allows the program to continue cycling through files even if certain
# files could not be found. It does not stop counting after one file fails.

# FAILING SILENTLY
# if we do not want to inform the user of the exception we simply..


def count_words_pass(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # PASS INSTEAD OF PRINT
    else:
        words = contents.split()
        num_words = len(words)
        print(
            f"The file '{Path(filename).stem}' contains approximately {num_words} words."
        )


print("\n-----FAILING SILENTLY-----\n")
for filename in filenames:
    count_words_pass(filename)


print("\n-----Add the missing files to a new text file-----\n")


def count_words_add_to_file(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        with open("10 Files and Exceptions/missing_files.txt", "a") as g:
            g.write(f"{filename}\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(
            f"The file '{Path(filename).stem}' contains approximately {num_words} words."
        )


for filename in filenames:
    count_words_add_to_file(filename)
