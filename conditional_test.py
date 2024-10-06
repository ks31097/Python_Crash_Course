string1 = 'Hello world!'
string2 = "hello world!"

print(f"{string1} == {string2}: {string1 == string2}")
print(f"{string1}.lower() == {string2}: {string1.lower() == string2}")

numb1 = 5
numb2 = 7

print(f"\n{numb1} != {numb2}: {numb1 != numb2}")
print(f"{numb1} == {numb2}: {numb1 == numb2}")
print(f"{numb1} > {numb2}: {numb1 > numb2}")
print(f"{numb1} < {numb2}: {numb1 < numb2}")
print(f"{numb1} >= {numb2}: {numb1 >= numb2}")
print(f"{numb1} <= {numb2}: {numb1 <= numb2}")

print(f"\n{numb1} >= {numb2} and {numb1} <= {numb2}: {numb1 >= numb2 and numb1 <= numb2}")
print(f"\n{numb1} >= {numb2} or {numb1} <= {numb2}: {numb1 >= numb2 or numb1 <= numb2}")

names = ['name1', 'name2', 'name3']
print(f"\n{names}")
print(f"name in list names: {'name' in names}")
