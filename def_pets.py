def describe_pet(pet_name="---", animal_type='dog'):
    """Information about the animal."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
print("")
describe_pet(animal_type='rabbit', pet_name='rex')
print("")
describe_pet(pet_name='willie')
print("")
describe_pet('RandName', "New")
print("")
describe_pet("Max")
print("")
describe_pet()