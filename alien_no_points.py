alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# try:
#     print(alien_0['points'])
# except KeyError:
#     print("The key does not exist!")

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)