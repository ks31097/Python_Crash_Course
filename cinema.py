# prompt = "\nPlease enter your age:"
# prompt += "\n(Enter 'quit()' to end the program).\n"

# while True:
#     age = input(prompt).strip()

#     if age == 'quit()':
#         break
#     elif len(age) == 0:
#         print("Try again!")
#     else:
#         age = int(age)
        
#         if age < 3:
#             price = 'free'
#             # print("Free")
#         elif age >= 3 and age < 12:
#             price = "$10"
#             # print("$10")
#         elif age >= 12:
#             price = "$15"
#             # print("$15")
    
#         print(price)


prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit()' to end the program).\n"
age = ""

while age != 'quit()':
    age = input(prompt).strip()

    if len(age) == 0:
        print("Try again!")
    else:
         if age != 'quit()':
            age = int(age)
            
            if age < 3:
                price = 'free'
                # print("Free")
            elif age >= 3 and age < 12:
                price = "$10"
                # print("$10")
            elif age >= 12:
                price = "$15"
                # print("$15")
        
            print(price)
