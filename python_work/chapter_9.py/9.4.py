# start with the class from 9.1.py and add an attribute called number_served with a default value of 0.
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 
    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Additional customers cannot be negative.")
