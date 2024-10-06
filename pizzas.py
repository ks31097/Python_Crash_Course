my_pizzas = ["pizza alla marinara", "pizza margherita", "pizza napolitana"]
print("I really love pizza!")

friend_pizzas = my_pizzas[:]
my_pizzas.append("pizza capricciosa")
for pizza in my_pizzas:
    message = f"My favorite pizzas are: {pizza.title()}."
    print(message)

print(" " * 60)

friend_pizzas.append("pizza regina")
for pizza in friend_pizzas:
    message = f"My friend'sasvorite pizzas are: {pizza.title()}."
    print(message)