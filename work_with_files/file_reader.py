# file_path = '/home/kostiantyn/python_work/work_with_files/pi_digits.txt'

# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

# with open('text_file.txt') as file_object:
#     content = file_object.read()
# print(f"\n{content}")

filename = 'work_with_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(type(file_object))
print(file_object.__dict__)

print(type(lines))
print(f"{lines}\n")

for line in lines:
    print(line.rstrip())