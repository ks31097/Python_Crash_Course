cars = ['car1', 'car2', 'car3']
text = 'I want to buy a car:'

for car in cars:
    message = f"{text} {car.title()}"
    print(message)