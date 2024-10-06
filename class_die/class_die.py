from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        random_numb = randint(1, self.sides)
        return random_numb
    
# object_die = Die(20)
# for _ in range(10):
#     print(f"{_ + 1}) Random number: {object_die.roll_die()}")

    


    