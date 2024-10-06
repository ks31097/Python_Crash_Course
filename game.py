# result2 = 0
# alien_color = ['green', 'yellow', 'red']

# if 'green' in alien_color:
#     result1 = 5

# if 'blue' in alien_color:
#     result2 = 3

# print(f"Your result is: {result1 + result2}")

alien_color = ['green', 'yellow', 'red']
if 'blue' in alien_color:
    result = 5
elif 'yellow' in alien_color:
    result = 10
elif 'red' in alien_color:
    result = 15
else:
    result = 1

print(f"Your result is {result}")