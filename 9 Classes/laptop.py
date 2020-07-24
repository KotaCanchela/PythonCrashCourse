# Test for a laptop
from modules import Laptop

my_laptop = Laptop(price=500, screen_size="15", ram=16, make="dell")

my_laptop.get_price()
my_laptop.get_ram()
my_laptop.get_screen_size()

my_laptop.keyboard.get_keyboard()

