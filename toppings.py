# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")


# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")

# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")

# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")


# requested_toppings = []
# # print(len(requested_toppings))
# if requested_toppings:
#     for requested_toping in requested_toppings:
#         print(f"Adding {requested_toping}.")
# else:
#     print("are you sure you want a plain pizza?")


# available_toppings = ('mushrooms', 'olives', 'green peppers', 'pineapple', 'extra cheese')

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")

# print("\nFinished making your pizza!")


message = "\nPlease enter the toppings for your pizza:"
message += "\n(Enter 'quit()' to end the program).\n"

toppings = []

active = True
while True:
# while active:
    topping = ((input(message).strip()).lower())

    if topping == 'quit()':
        break
        # active = False
    elif len(topping) == 0:
        print("Try again!") 
    else:
        toppings.append(topping)
        print(f"You added: {topping}.")

print(f"\nAll your pizza toppings:")
for topping in toppings:
    print(f"\t{topping.title()}")