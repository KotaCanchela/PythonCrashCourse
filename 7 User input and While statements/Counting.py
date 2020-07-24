# Using continue in a loop
# continue allows the user to return to the beginning of the loop rather than breaking out entirely

# The continue statement tells Python to ignore the rest of the loop
# Therefore, when current_number is divisible by 2 it loops back
# otherwise when it is odd it goes to the next line (print)
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Avoiding infinite loops
# If you forget to add the x += 1 the loop will run forever

print("")
x = 1
while x <= 5:
    print(x)
    x += 1