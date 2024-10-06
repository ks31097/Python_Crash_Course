def empty_line():
    print("")

country_river = {'nile': 'egypt', 'dnipro': 'ukraine', 'amazon river': 'brazil'}
# country_river = {}
if country_river:
    for river, country in country_river.items():
        print(f"The {river.title()} runs through {country.title()}.")

    empty_line()
    for river in country_river.keys():
        print(river.title())

    empty_line()
    for country in sorted(country_river.values(), reverse=True):
        print(country.title())
else:
    print("The dictionary is empty!")