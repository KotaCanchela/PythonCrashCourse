#  A movie theater charges different ticket prices depending on a person’s age.
#  If a person is under the age of 3, the ticket is free; if they are between 3 and 12,
#  the ticket is $10; and if they are over age 12, the ticket is $15.
#  Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# The loop doesn't make too much sense if it quits after one answer.
# So I added a 'quit' variable and added a total tickets price at the end

prompt = "\nPlease enter your age: "
prompt += "\nOnce you are done please type 'quit'\n"
price = 0
while True:
    age = input(prompt)
    if age == 'quit':
        print(f"The total cost of your tickets are: {price}$")
        break
    elif int(age) < 3:
        print(f"Since you are {age} years old, your ticket is free.")
        continue
    elif 3 <= int(age) <= 12:
        print(f"Since you are {age} years old, your ticket will be $10.")
        price += 10
        continue
    elif int(age) > 12:
        print(f"Since you are {age} years old, your ticket will be $15.")
        price += 15
        continue