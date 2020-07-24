# “4-6. Odd Numbers: Use the third argument of the range() function
# to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
odd_number = [value for value in range(1, 21, 2)]
print(odd_number)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30.
# Use a for loop to print the numbers in your list.

threes = [value for value in range (3, 31, 3)]
print(threes)
threes_alt = []
for value in range (3, 31, 3):
    threes_alt.append(value)
print(threes_alt)

# 4-8 Cubes: “ A number raised to the third power is called a cube.
# For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10)
# and use a for loop to print out the value of each cube.

cubes = [value ** 3 for value in range (1, 11)]
print(cubes)

cubes_alt = []
for value in range (1, 11):
    cubes_alt.append(value ** 3)
print(cubes_alt)