prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit()' when you are finished.) "

while True:
    city = ((input(prompt)).lower()).strip()

    if city == 'quit()':
        break
    elif len(city) == 0:
        print('Try again!')
    else:
        print(f"I'd love to go to {city.title()}!")