class Dog():
    """A simple model of a dog"""

    def __init__(self, name, age):
        """Initializing attribute name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """The dog sits down after the command"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """The dog rolls over after the command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name.capitalize()}.")
my_dog.name = 'tom'
print(f"My dog's name is {my_dog.name.capitalize()}.")

print(f"My dog is {my_dog.age} years old.")
my_dog.age = 9
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()