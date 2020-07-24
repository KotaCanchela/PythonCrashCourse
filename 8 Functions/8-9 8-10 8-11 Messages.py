# 8-9 Messages:
# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message

short_messages = ['hello, how are you?', 'i am good thank you.',
                  'what are you doing?', 'how is your family?']


def show_messages(messages):
    """Prints a series of text messages in a list"""
    for message in messages:
        print(message.capitalize())


show_messages(short_messages)


# 8-10 Sending Messages:
# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.




def show_messages(messages):
    """Prints a series of text messages in a list"""
    for message in messages:
        print(message.capitalize())


def sent_messages(short_messages):
    """Prints each text message and moves them to a new list"""
    while short_messages:
        send = short_messages.pop()
        print(f"\nThe following text has been sent:\n\t{send}")
        sent_message.append(send)
    print("\nAll messages have been sent.")


short_messages = ['hello, how are you?', 'i am good thank you.',
                  'what are you doing?', 'how is your family?']
sent_message = []

print(f"\n\n")
show_messages(short_messages)
print("")
sent_messages(short_messages)
print("")
print(short_messages)
print(sent_message)


# 8-11 Archived messages:
# “Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.


short_messages = ['hello, how are you?', 'i am good thank you.',
                  'what are you doing?', 'how is your family?']
sent_message = []


print(f"\n\n")
show_messages(short_messages)

print("")
sent_messages(short_messages[:])

print("")

print(short_messages)
print(sent_message)
