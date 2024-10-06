alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"Color: {alien_0['color']}")
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f"\nalien_0: {alien_0}")
print(f"\nOriginal x_position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Fast speed
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

del alien_0['points']
print(f"\nalien_0: {alien_0}")
# print('-' * 80) 

# alien_1 = {}

# alien_1['color'] = 'yellow'
# alien_1['points'] = 10
# print(f"\nalien_1 = {alien_1}")
# print(f"The alien_1 is {alien_1['color']}.")

# alien_1['color'] = 'red'
# print(f"\nalien_1 = {alien_1}")
# print(f"The alien is now {alien_1['color']}.")