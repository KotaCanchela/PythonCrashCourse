# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['ham', 'cheese', 'egg', 'tomato']
finished_sandwiches = []
print("")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.\n")
    finished_sandwiches.append(sandwich)
print(f"The following sandwiches have been made:"
      f"\n\t{', '.join(finished_sandwiches).title()}")


# 7-9
# Make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
print("\n\n\n")
sandwich_orders = ['ham', 'pastrami', 'cheese', 'pastrami', 'egg', 'tomato', 'pastrami']
finished_sandwiches = []
print(f"Unfortunately the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.\n")
    finished_sandwiches.append(sandwich)
print(f"The following sandwiches have been made:"
      f"\n\t{', '.join(finished_sandwiches).title()}")
print(finished_sandwiches)