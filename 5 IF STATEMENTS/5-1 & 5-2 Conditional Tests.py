# “Write a series of conditional tests.
# Print a statement describing each test and your prediction for the results of each test.

car = 'bmw'
print("is car == 'bmw'? I predict True\n")
print(car == 'bmw')

print("\nis car == 'subaru'? I predict False\n")
print(car == 'subaru')

print("\nIs car == 'BMW'? I predict False\n")
print(car == 'BMW')

print("\n Is car.upper() == 'BMW'? I predict True\n")
print(car.upper() == 'BMW')

print("\n is car.upper() == 'BMW' and car == 'bmw'? I predict True\n")
print(car.upper() == 'BMW' and car == 'bmw')

# Test whether an item is in a list
# Test whether an item is not in a list

cars = ['bmw', 'volkswagen', 'mitsubishi']
car = 'volkswagen'

if car in cars:
    print(f"You own a {car}")
elif car not in cars:
    print(f"Unfortunately, you do not own a {car}")