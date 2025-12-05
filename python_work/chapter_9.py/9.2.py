# start with the class from 9.1.py and then make three instances of the Restaurant class
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
# Create three instances of the Restaurant class
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Central", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
 