# write a function called city_country() that takes in the name of a city and its country
def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'
# call the function with at least three city-country pairs
print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))
