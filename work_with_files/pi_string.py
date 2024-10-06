from decimal import Decimal as d

# filename = 'work_with_files/pi_digits.txt'
filename = 'work_with_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

pi_decimal = d(pi_string)
print(pi_decimal)
print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter yoir birthday, in the form mm/dd/yy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appeear in the first million digits of pi.")