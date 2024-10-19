def country_and_city(country, city, population=''):
    if population:
        message = f"{country.title()}, {city.title()} - population {population}"
    else:
        message = f"{country.title()}, {city.title()}"
    return message