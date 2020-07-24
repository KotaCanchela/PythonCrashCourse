alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens

aliens = []

# Make 30 green aliens

for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first five aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.

print(f"The total number of aliens is: {len(aliens)} aliens")

# Change first 3 aliens to yellow, med speed, 10 pts (if already yellow then go red)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Following code will be only yellow bc there were no yellows prior to the code.
for alien in aliens[:3]:
    print(alien)
