def build_person(first_name, last_name, age=None): # None == False
    """Returning dictionary with information about person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=46)
print(musician)