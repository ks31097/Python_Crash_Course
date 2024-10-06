from  class_die import Die as D

object_die = D(6)

for throw in range(10):
    print(f"{throw + 1}) Your dice has a number: {object_die.roll_die()}")