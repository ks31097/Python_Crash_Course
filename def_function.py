def first_function(message):
    print(message)

def second_function():
    first_function("I love Python!")

# second_function()

list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

string = ''.join(str(x) for x in list)
print(string)
print(type(string))