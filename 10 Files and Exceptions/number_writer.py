# Using json.dump() and json.load()

# Program that stores a set of numbers and another program that reads these back into memory

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '10 Files and Exceptions/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)


