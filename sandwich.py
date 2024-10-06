sandwich_orders = ['hamburger', 'pastrami', 'pastrami', 'reuben sandwich', 'club sandwich', 'pastrami', 'croque-monsieur', 'jambon-beurre']
finished_sandwich = []
print(sandwich_orders)

print("\nPastrami was sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwich.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwich:
    print(f"\t{sandwich.title()}")