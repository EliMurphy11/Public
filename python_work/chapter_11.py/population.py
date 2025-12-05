# ...existing code...
def city_country(city, country, population):
    """Return a formatted string 'City, Country - population xxx'."""
    return f"{city.title()}, {country.title()} - population {population}"

if __name__ == "__main__":
    print(city_country("santiago", "chile", 500000))
    print(city_country("paris", "france", 2148327))
# ...existing code...