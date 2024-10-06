number = int(input("Enter a number, and I'll tell you"
                   "if it's divisible by 10 without remainder.\n"))

if number % 10 == 0:
    print(f"The number {number} is divisible by 10 without remainder.")
else:
    print(f"The number {number} is not divisible by 10 without remainder.")