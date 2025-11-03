# make a dictionry called favorite_places
favorite_places = {
    'regina': ['paris', 'new zealand', 'switzerland'],
    'asher': ['greece', 'bali', 'Mckinney'],
    'eli': ['japan', 'italy', 'australia'],}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
        