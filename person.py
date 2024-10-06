people = []

for famous_person in range(0, 5):
    famous_person = {}
    famous_person['first_name'] = 'famous name'
    famous_person['last_name'] = 'famous surname'
    famous_person['age'] = 34
    famous_person['city'] = 'San Francisco'
    people.append(famous_person)

# for person in people:
#     print(person)

if people:
    for person in people:
        print(f"\nFull name: {person['first_name'].title()} {person['last_name'].title()}, age: {person['age']}")
        print(f"Location: {person['city']}")


# people = {}
# people['celebrity'] = famous_person

# print(people)

# for person, person_info in people.items():
#     print(f"\nPerson: {person}")
#     full_name = f"{person_info['first_name']} {person_info['last_name']}, age: {person_info['age']}"
#     location = f"{person_info['city']}"
#     print(f"\tGeneral information: {full_name}")
#     print(f"\tLocation: {location}")


# print(f"\n{person['first_name']}")
# print(person['last_name'])
# print(person['age'])
# print(person['city'])