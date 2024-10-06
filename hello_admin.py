current_users_lower = []

current_users = ['NAME1', 'naMe2', 'nAmA3', 'name4', 'Name5']
print(current_users)

for current_user in current_users:
    current_users_lower.append(current_user.lower())

print(current_users_lower)

new_users = ['name6', 'name7', 'name1', 'name8', 'name5']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\nYou can not use name {new_user} to register.")
        print("Choose another name!")
    else:
        print(f"\nYou can use {new_user} to register.")


# names = []
# # names = ['name1', 'name2', 'admin', 'name3', 'name4']
# if names:
#     for name in names:
#         if name == 'admin':
#             print(f"\nHello {name} would you like to see a status report?")
#         else:
#             print(f"\nHello {name}, thank you for logging in again.")
# else:
#     print("We need to ind some users!")