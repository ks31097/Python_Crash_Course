number = input("Enter a number, and I'll tell you"
               "if it's even or odd: ")
# number = int(number)

if int(number) % 2 == 0: # number % 2 == 0 -> even  
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")