user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fewmi',
}
print(type(user_0.items()))
print(type(type(user_0.items())))

print(user_0.items())

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")