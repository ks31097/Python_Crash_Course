def city_country(city='', country=''):
    return f"{city}, {country}"

counter = 3
while counter:
    message = city_country(city='Santiago', country='Chile')
    print(f"{counter} {message}")
    counter -= 1