def empty_line():
    print("")

names_of_my_friends = ['name1', 'name2', 'name3']
for name in names_of_my_friends:
    message = f"""Hello {name.title()},
    What do you think about the meeting tomorrow at 17.00?

Kostiantyn"""
    print(message)

    if name != names_of_my_friends[-1]: 
        empty_line()