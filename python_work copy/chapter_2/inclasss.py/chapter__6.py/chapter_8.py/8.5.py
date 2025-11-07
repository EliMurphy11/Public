# write a function called describe_city() that accepts the name of a city and its country
def describe_city(city, country='USA'):
    print(f"{city.title()} is in {country.title()}.")
# call the function for three different cities
describe_city('new york')
describe_city('los angeles')
describe_city('toronto', 'canada')
