def empty_line():
    print(" " * 60)

"""
user_name = input("Input name:\t")
"""

"""
# first task
message = f"Hello {user_name}, would you like to learn some Python today?"

empty_line()
print(message)
"""

"""
# second task
print(user_name.title())
empty_line()

print(user_name.upper())
empty_line()

print(user_name.lower())
"""

famous_person = " Francis Drake "
text = "\"Sic Parvis Magna\""
message = f"{famous_person} once said, {text}"
print(message)
empty_line()

message = f"{famous_person} once said, {text}"
print(message.lstrip())
empty_line()

message = f"{famous_person} once said, {text}"
print(message.rstrip())
empty_line()

message = f"{famous_person} once said, {text}"
print(message.strip())