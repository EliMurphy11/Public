# using dictionaries to store information about a person
person = {
    'first_name': 'Eli',
    'last_name': 'Murphy',
    'age': 16,
    'city': 'Mckinney',}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
# make two new dictionaries representig deiffferent people and store them in a list called people.
person_2 = {
    'first_name': 'jack',
    'last_name': 'Murphy',
    'age': 3,
    'city': 'Mckinney',}
person_3 = {
    'first_name': 'Asher',
    'last_name': 'Murphy',
    'age': 14,
    'city': 'Mckinney',}
people = [person, person_2, person_3]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name}, age {age}, lives in {city}.")


