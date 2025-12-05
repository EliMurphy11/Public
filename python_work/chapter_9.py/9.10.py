import restaurant
class Restaurant:
    """A simple Restaurant class stored in its own module."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")
        import restaurant
# ...existing code...

if __name__ == "__main__":
    my_restaurant = restaurant.Restaurant("Pasta Palace", "Italian")
    my_restaurant.describe_restaurant()
    import restaurant
