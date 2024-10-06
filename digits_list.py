def empty_line():
    print(" " * 60)

# for value in range(1, 21):
#     print(value)
# empty_line()

# numbers = list(range(1, 1_000_001))
# for number in numbers:
#     print(number)
# empty_line()

# print(f"Min number: {min(numbers)}")
# print(f"Max number: {max(numbers)}")
# print(f"Sum: {sum(numbers)}")

digits_list = []
for value in range(1, 20, 2):
    print(value)
    digits_list.append(value)

empty_line()
print(digits_list)

empty_line()
digits_list_2 = [value for value in range(3, 31, 3)]
print(digits_list_2)

empty_line()
cube = [value**3 for value in range(2, 11, 2)]
print(cube)

empty_line()
cube_list = []
for value in range(2, 11, 2):
    print(value)
    cube_list.append(value**3)

print(cube_list)

empty_line()
cube_list_2 = [value**3 for value in range(1, 11)]
print(cube_list_2)