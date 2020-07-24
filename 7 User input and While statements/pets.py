# Removing all instances of specific values in a list
# If there are multiple instances of 'cat' and we want to remove them all

pets = ['dog', 'cat', 'hamster', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# If we want to remove all but one
print('\n\n')
pets = ['dog', 'cat', 'hamster', 'cat', 'rabbit', 'cat', 'cat']
print(pets)


while pets.count('cat') > 1:
    pets.remove('cat')

print(pets)