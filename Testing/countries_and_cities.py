from country_and_city_function import  country_and_city

print("Enter 'q' at any time to quit.")
while True:
    country = ((input("\nPlease give me name of the country: ")).strip()).lower()
    if country == 'q':
        break
    
    city = ((input("Please give me name of the city: ")).strip()).lower()
    if city == 'q':
        break

    answer = ((input("Would you like to add additional population information?: ")).strip()).lower()
    if answer == 'yes' or answer == 'y':
        population = ((input("Please give me population in the city: ")).strip()).lower()
        if population == 'q':
            break
        message = country_and_city(country, city, population)
    else:
        message = country_and_city(country, city)
    print(f"Your choice: {message}.")