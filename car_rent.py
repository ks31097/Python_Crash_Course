car_type = (input("What type of car do you want to rent? ")).lower()

if car_type == 'bmw':
    car_type = car_type.upper()
else:
    car_type = car_type.title()

print(f"Let me see if I can find you a {car_type}.")