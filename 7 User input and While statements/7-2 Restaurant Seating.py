# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they’ll have to wait for a table.
# Otherwise, report that their table is ready.

dinner = int(input("How many people will be in your dinner group? "))

if dinner > 8:
    print("Unfortunately, you will have to wait for a table.")
else:
    print(f"Your table for {dinner} is ready.")