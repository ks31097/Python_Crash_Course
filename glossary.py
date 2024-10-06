glossary = {
    'key2': 'value2',
    'key1': 'value1',
    'key4': 'value4',
    'key5': 'value5',
    'key3': 'value3',
    'key7': 'value7',
    'key6': 'value6'
    }

print("glossary keys:")
for key in sorted(set(glossary.keys())):
    print(key.title())

print("\nglossary values")
for value in set(glossary.values()):
    print(value.title())

print(f"\n{(list(glossary.keys())[0]).title()}: {glossary[list(glossary.keys())[0]]}.")
print(f"\n{type(list(glossary.keys()))}")
print(type(glossary.keys()))
print(glossary.values()[0])


