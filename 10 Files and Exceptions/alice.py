# Handling the FileNotFoundError Exception
# Try to read a file that doesn't exist

filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()

except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")

# Analysing text
print("-----ANALYZING TEXT-----")
filename = "/Users/Kota/Desktop/pcc_2e-master/chapter_10/alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()

except FileNotFoundError:
    print(f"Sorry, the file, '{filename}' could not be found. ")

else:
    # Count the number of words in the text.
    words = contents.split()
    num_words = len(words)
    print(f"The file '{filename}' has about {num_words} words.")

