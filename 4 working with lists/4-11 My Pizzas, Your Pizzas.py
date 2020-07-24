pizzas = ['pepperoni', 'ham', 'pineapple', 'sausage', 'cheese']
friend_pizzas = pizzas[:]

# Add a new pizza to the original list

pizzas.append('anchovies')

# Prove that you have two separate lists. Print the message My favorite pizzas are:

print(f"My favourite pizzas are: {pizzas}")
# Add a different pizza to the list friend_pizzas.

friend_pizzas.append('fish')

# and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:
for pizza in friend_pizzas:
    print(f"My friend's favourite pizzas are: {pizza}")
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.”

for pizza in pizzas:
    print(f"My favourite pizzas are: {pizza}")
