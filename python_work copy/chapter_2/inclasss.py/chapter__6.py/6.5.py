# dictionary containing three major rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
# loop through the dictionary items and print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
# loop through the dictionary keys and print the names of the rivers
for river in rivers.keys():
    print(river.title())
# loop through the dictionary values and print the names of the countries
for country in rivers.values():
    print(country.title())