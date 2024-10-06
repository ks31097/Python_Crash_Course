print("Give me to nambers, and I'll sum them.")
print("Enter 'q' to quit.")
def simple_calculator():
    while True:
        first_number = input("\nFirst number: ")

        if first_number == "q":
            break

        second_number = input("Second number: ")

        if second_number == 'q':
            break

        try:
            first_number = float(first_number)
            second_number = float(second_number)
            
            sum = first_number + second_number
        except ValueError:
            print("Your input is text!")
        else:
            print(f"Result: {round(sum, 2)}")

simple_calculator()