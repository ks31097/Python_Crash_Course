love_number = {'name1': [5, 35, 49], 'name2': [9], 'name3': [11, 6, 15], 'name4': [14, 93], 'name5': [77, 24]}
print(love_number)
print(f"\n{love_number['name1']}")
print(love_number['name2'])
print(love_number['name3'])
print(love_number['name4'])
print(love_number['name5'])

print(f"\nlove_numbers keys: {love_number.keys()}")
print(f"love_number values: {love_number.values()}")
print(f"love_number items: {love_number.items()}")

print(f"\n{love_number.get('name9', 'The name does not exist!')}")