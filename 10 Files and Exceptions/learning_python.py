#   Open a blank file in your text editor and write a few lines summarizing
#  what you’ve learned about Python so far. Start each line with the phrase In
#  Python you can. . .. Save the file as learning_python.txt in the same
# directory as your exercises from this chapter. Write a program that reads the
#  file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by
#  storing the lines in a list and then working with them outside the with block.

filepath = "10 Files and Exceptions/learning_python.txt"

with open(filepath) as file_object:
    contents = file_object.read()
print(contents.strip())

print("-----1-----")
with open(filepath) as file_object:
    for line in file_object:
        print(line.strip())

print("----2----")

with open(filepath) as file_object:
    file_list = file_object.readlines()

for line in file_list:
    print(line.strip())

# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.”
print("-----3-----")
for line in file_list:
    print(line.replace('python', 'C').strip())

