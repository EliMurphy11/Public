# using dictionaries to store peoples favorite numbers but now they can have more than one favorite number
favorite_numbers = {
    'Eli': [7, 3],
    'Regina': [3, 9, 12],
    'Asher': [12, 5],
    'Pax': [7, 11],
    'Mia': [5, 8],}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
        