# alien_0 = {'color': 'green', 'points': 5,}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2,]

# for alien in aliens:
#     print(alien)

aliens = []

for alien_number in range(0, 30):
    # new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_number = {'color': 'green', 'points': 5, 'speed': 'slow'}

    # aliens.append(new_alien)
    aliens.append(alien_number)


print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:5]:
    print(alien)

print("...")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)

print(...)