# make a dictionary called favorite_numbers
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
        # add new keys and values
favorite_numbers['Liam'] = [4, 6]
favorite_numbers['Sophia'] = [1, 2, 3]
print("\nUpdated favorite numbers:")
for name, numbers in favorite_numbers.items():      
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")    