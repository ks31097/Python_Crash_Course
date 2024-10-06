list_menu = ['list_dish1', 'list_dish2', 'list_dish3']
menu = ('dish1', 'dish2', 'dish3', 'dish4', 'dish5')
print(menu)

for dish_menu in menu:
    print(dish_menu.title())

print(f"\n{list_menu}")
print(f"{list_menu[2]}")
list_menu[2] = 'new_list_dish'
print(f"{list_menu}")

# print(f"\n{menu[3]}")
# menu[3] = 'new dish'

print(f"\n{menu}")
menu = ('dish1', 'dish2', 'dish3', 'new_dish4', 'new_dish5')
print(menu)

print(f"\n{menu[2]}")
menu[3] = 'new_dish3'