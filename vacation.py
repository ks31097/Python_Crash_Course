vacations = {}

# active = True
# while active:
while True:
    name = input("\nWhat is your name? ")
    response = input("Where will you spend your vacation? ")
    vacations[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        # active = False
        break

print("\n--- Poll Result ---")
for name, response in vacations.items():
    print(f"{name} would like to climb {response}.")