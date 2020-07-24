# Admission for anyone under age 4 is free
# Admission for anyone between the ages of 4 and 18 is $25
# Admission for anyone age 18 or older is $40

age = int(input('How old are you?\n'))

if age < 4:
    print("The cost of your ticket is $0")
elif age < 18:
    print("The cost of your ticket is $25")
else:
    print("The cost of your ticket is $40")

# V2

age = int(input('\nHow old are you?\n'))

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"The cost of your admission is ${price}")