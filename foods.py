my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_food = my_foods
numb = 0
print(f"My favorite foods are:")
my_foods.append('cannoli')
for my_food in my_foods:
    numb += 1
    print(f"\t\t\t{numb}) {my_food.title()}")

numb = 0
print(f"\nMy friend's favorite foods are:")
friend_foods.append('ice cream')
for friend_food in friend_foods:
    numb += 1
    print(f"\t\t\t{numb}) {friend_food.title()}")

print(f"\nThe irst three items in the list area: {my_foods[0:3]}.")
print(f"There items from the middle of the list are: {my_foods[1:3]}.")
print(f"The last three items in the list are: {my_foods[1:4]}.")