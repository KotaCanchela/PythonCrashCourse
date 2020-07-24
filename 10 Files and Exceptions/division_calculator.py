# Handling the zerodivisionerror exception
# print(5/0) returns --> ZeroDivisionError: division by zero
# Therefore we must use a try-except block

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by 0!")
# If the code in the try block works, then it skips over the except block
# If a code in a try block doesn't work, python looks for an except block
# whose error matches the one given in the try block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("You need to enter a number.")
    else:   # “Any code that depends on the try block executing successfully goes in the else block:”
        print(answer)
        