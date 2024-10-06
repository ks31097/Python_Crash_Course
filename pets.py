# chloe = {'chloe': {'type': 'cat', 'owner': 'sam'}}
# max = {'max': {'type': 'dog', 'owner': 'tomas'}}
# daisy = {'daisy': {'type': 'dog', 'owner': 'phil'}}

# pets = []
# pets.append(chloe)
# pets.append(max)
# pets.append(daisy)

# print(type(pets))
# for pet in pets:
#     for pet_name, pet_info in pet.items():
#         print(f"\nPat name: {pet_name.title()}")
#         print(f"\tPet type: {pet_info['type']}")
#         print(f"\tOwner: {pet_info['owner'].title()}")


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(f"\n{pets}")