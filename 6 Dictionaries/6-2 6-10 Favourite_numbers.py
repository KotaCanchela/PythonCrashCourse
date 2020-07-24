# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number.

favourite_numbers = {
    'kota': 7,
    'frank': 16,
    'henry': 23,
    'james': 24,
    'bill': 7,
}

print(f"{[key for key in favourite_numbers.keys()][0].title()}'s "
      f"favourite number is {str(favourite_numbers['kota'])}")

print(f"{[key for key in favourite_numbers.keys()][1].title()}'s "
      f"favourite number is {str(favourite_numbers['frank'])}")

print(f"{[key for key in favourite_numbers.keys()][2].title()}'s "
      f"favourite number is {str(favourite_numbers['henry'])}")

print(f"{[key for key in favourite_numbers.keys()][3].title()}'s "
      f"favourite number is {str(favourite_numbers['james'])}")

print(f"{[key for key in favourite_numbers.keys()][4].title()}'s "
      f"favourite number is {str(favourite_numbers['bill'])}")

# V2
print("")
for key, value in favourite_numbers.items():
    print(f"{key.title()}'s favourite number is "
          f"{(str(value))}")


# 6-10
# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

favourite_numbers = {
    'kota': [7, 10, 15],
    'frank': [5, 11, 17],
    'henry': [23],
    'james': [27, 29, 31],
    'bill': [52, 73, 83],
}

print(f"\n\n\n")
for name, numbers in favourite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favourite number is:")
    else:
        print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{str(number)}")