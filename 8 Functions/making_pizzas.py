# Importing module from pizzas.py

#import pizzas as p
from pizzas import make_pizza as p

p(16, 'pepperoni')

p(18, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific modules also works
# from module_name import function_0, function_1, function_2
# from module_name import function_name

# from pizzas import make_pizza as p

# to import all functions in a module do
# from pizza import *

# then can just simply do: make_pizza(16, 'pepperoni')
# don't need to use dot notation such as p.make_pizza(16, 'pepperoni)