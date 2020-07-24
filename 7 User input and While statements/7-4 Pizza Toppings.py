# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# For fun I will add the toppings to a list and display it

pizza_toppings = []
prompt = "\nPlease enter a topping that you would like on your pizza: "
prompt += "\nIf you have finished adding toppings then you may type 'quit'\n"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You have successfully added: \n\t{topping.title()}\n")
        pizza_toppings.append(topping)
        print(f"You now have the following toppings on your pizza:"
              f"\n\t{', '.join(pizza_toppings).title()}")