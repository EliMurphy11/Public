# make several dictionaries representing different pets
pet_1 = {
    'animal_type': 'dog',
    'name': 'Buddy',
    'owner': 'william',}
pet_2 = {
    'animal_type': 'tiger',
    'name': 'cuddles',
    'owner': 'Eli',}
pet_3 = {
    'animal_type': 'parrot',
    'name': 'Polly',
    'owner': 'Asher',}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    pet_type = pet['animal_type']
    pet_name = pet['name']
    pet_owner = pet['owner']
    print(f"{pet_name} is a {pet_type} owned by {pet_owner}.")