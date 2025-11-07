# make a class called Restaurant the init method should take two parameters called retaurant_name and cuisine_type
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
# make a methoid called describe_restaurant that prints the restaurant name and cuisine type
    def describe_restaurant(self):
        """Display information about the restaurant."""
  