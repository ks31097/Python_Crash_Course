# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit()' to end the program.\n"

# message = ""
# while message != 'quit()':
#     message = input(prompt)
#     if message != 'quit()':
#         print(f"\n{message}")


prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n(Enter 'quit()' to end the program.) "

active = True
while active:
    message = (input(prompt)).lower()
    
    if message == 'quit()':
        active = False
    else:
        print(f"\n{message}")