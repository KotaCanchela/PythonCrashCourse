import json


filename = "10 Files and Exceptions/numbers.json"

with open(filename, "r") as f:
    numbers = json.load(f)

print(numbers)
