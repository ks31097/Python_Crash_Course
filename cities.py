cities = {
    'city1': {'country': 'country1', 'population': 'population1', 'fact': 'fact1',},
    'city2': {'country': 'country2', 'population': 'population2', 'fact': 'fact2',},
    'city3': {'country': 'country3', 'population': 'population3', 'fact': 'fact3',},
}

for city, city_information in cities.items():
    print(f"\nInformation about the {city.title()}:")

    for value in city_information.values():
        print(f"\t{value}")