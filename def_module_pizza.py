def make_pizza(size, *toppings): # *args
    """Show information about pizza"""
    print(f"\nMaking a {size}-inch pizza with the followong toppings:")
    for topping in toppings:
        print(f"- {topping}")