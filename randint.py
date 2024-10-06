from random import randint
from random import choice

random_numb = randint(1, 6)
print(f"Random number: {random_numb}")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(f"Choice function: {first_up.title()}")