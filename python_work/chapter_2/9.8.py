# write a class called icecreamstad that inherets from the restaurant class from restaurant import Restaurant
from Restaurant import Restaurant
class IceCreamStand(Restaurant):
    """A class representing an ice cream stand, inheriting from Restaurant."""

    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize the ice cream stand with a name and cuisine type."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        """Add a new ice cream flavor to the stand."""
        self.flavors.append(flavor)

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
