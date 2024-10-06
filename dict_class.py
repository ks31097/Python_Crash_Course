def line():
    print("=" * 60 + "\n")


# class Person():
#     name = "Jason"

#     def greeting():
#         return "Hello, there!"

# print(Person.__dict__)
# print(Person.name)
# print(Person.greeting())
# line()

# one_person = Person()
# print(one_person.__dict__)
# hex_id_one_person = hex(id(one_person))
# print(hex_id_one_person)


# class Person():
#     name = "Jason"

#     def greeting(obj):
#         "Hello, there!"
#         return(f"{hex(id(obj))}")
# print(Person.__dict__)
# # print(Person.name)
# # print(Person.greeting())
# line()

# one_person = Person()
# print(one_person.__dict__)
# hex_id_one_person = hex(id(one_person))
# print(hex_id_one_person)
# line()

# print(one_person.name)
# one_person.name = "Max"
# print(one_person.name)
# print(one_person.__dict__)
# one_person_greeting = one_person.greeting()
# print(one_person_greeting)
# line()

# print(hex_id_one_person == one_person_greeting)


# class Person:
#     """Simple Person model"""

#     def constructor(self, name):
#         """Update person name"""
#         self.name = name
    
#     def greeting(self):
#         """Show the greeting message"""
#         return "Hello there!"

# one_person = Person()
# print(one_person.__dict__)
# one_person.constructor("Jason")
# print(one_person.greeting())
# print(one_person.__dict__)
# print(one_person.name)
# one_person.name = "David"
# print(one_person.name)
# line()


class Person:
    """Simple Person model"""

    def __init__(self, name):
        """Update person name"""
        self.name = name
    
    def greeting(self):
        """Show the greeting message"""
        return f"Hello there! My name is {self.name}."

one_person = Person("Tom")
print(one_person.__dict__)
print(one_person.greeting())
print(one_person.name)
one_person.name = "David"
print(one_person.name)
line()