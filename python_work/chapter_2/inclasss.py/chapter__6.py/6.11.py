# make a dictionary called cities
cities = {
    'mckinney': {
        'country': 'usa',
        'population': 180000,
        'fact': 'home of me',},
    'paris': {
        'country': 'france',
        'population': 11000000, 
        'fact': 'the city of lights',},
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'the largest metropolitan area in the world',},}
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"{city.title()} is in {country.title()}. It has a population of about {population} people. Fun fact: {fact}.")