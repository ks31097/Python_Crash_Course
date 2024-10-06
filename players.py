players = ['charles', 'martina', 'michael', 'florence', 'eli']
# list_with_playrs = players[0:3]
# print(list_with_playrs)

# list_with_playrs_2 = players[1:4]
# print(list_with_playrs_2)

# list_with_playrs_3 = players[1:5]
# print(list_with_playrs_3)

# list_with_playrs_4 = players[:4]
# print(list_with_playrs_4)

# list_with_playrs_5 = players[2:]
# print(list_with_playrs_5)

# list_with_playrs_6 = players[-3:]
# print(list_with_playrs_6)
print("Here are the first three players on my team:")
for player in reversed(players[:3]):
    print(player.title())