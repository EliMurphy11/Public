# make a class called Restaurant. The _init_() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
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
if __name__ == "__main__":
        # create a Restaurant instance and call its methods
        r = Restaurant("Pasta Palace", "Italian")
        r.describe_restaurant()
        r.open_restaurant()


  