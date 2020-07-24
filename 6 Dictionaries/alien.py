alien_0 = {'colour': 'green', 'points': 5}
alien_0['x_position'] = 0    # adding coordinates to the list
alien_0['y_position'] = 25

print(alien_0['colour'])    # printing from the key
print(alien_0['points'])

new_points = alien_0['points']
new_colour = alien_0['colour']

print(f"Congratulations! You have shot the {new_colour} alien "
      f"and have earned {new_points} points.\n")

print(alien_0)

alien_0 = {}    # better to start with an empty list and add to it

alien_0['colour'] = 'green'
alien_0['points'] = 5

print(alien_0)

print(f"The alien is {alien_0['colour']}")

alien_0['colour'] = 'yellow'    # Modifying values in a dictionary

print(f"The alien is now {alien_0['colour']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
      x_increment = 1
elif alien_0['speed'] == 'medium':
      x_increment = 2
else:
      x_increment = 3

# The new position is the old position plus the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The alien's new position is {alien_0['x_position']}")



alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

del alien_0['points']   # deletes the key and the value associated with i
print(alien_0)

alien_0 = {'colour': 'green', 'speed': 'slow'}
# print(alien_0['points']) results in keyerror

# Use the get() method to set a default value that will be returned if the requested key doesn't exist.
# “The get() method requires a key as a first argument.
# As a second optional argument, you can pass the value to be returned if the key doesn't exist:
alien_0 = {}
point_value = alien_0.get('points', 'No point value assigned.')
print("")
print(point_value)

# If there’s a chance the key you’re asking for might not exist
# consider using the get() method instead of the square bracket notation.
