from random import randint


class Die:
    """A simple dice"""

    def __init__(self, sides):
        """Initialise the amount of sides on the dice"""
        self.sides = sides

    def roll_die(self):
        """Rolls the dice"""
        print(f"{randint(1, self.sides)}")


dice_6 = Die(6)
dice_10 = Die(10)
dice_20 = Die(20)


print("Rolling the  six sided dice 10 times...")
for x in range(10):
    dice_6.roll_die()
print("\nSix sided dice completed")


print("\nRolling the ten-sided dice 10 times...")
for x in range(10):
    dice_10.roll_die()
print("\nTen sided dice completed.")


print("\nRolling twenty sided dice 10 times...")
for x in range(10):
    dice_20.roll_die()
print("\nTwenty sided dice completed.")
