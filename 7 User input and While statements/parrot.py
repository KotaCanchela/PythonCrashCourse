prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit or 'end' to end the program.\n"

# message = ""
# while message != 'quit':
    # message = input(prompt)
    # if message != 'quit':
       #  print(message)


# Using a flag (making a blank True statement) if there are multiple factors that could end the program
# Can use this to print a game over for many factors etc etc etc.

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif message == 'end':
        active = False
    else:
        print(message)
