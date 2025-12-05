import electric_car
# ...existing code...
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple battery for an electric car."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        """Upgrade the battery to 100 kWh if it's less than 100."""
        if self.battery_size < 100:
            self.battery_size = 100
# ...existing code...
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size=75):
        """Initialize attributes of the parent class and add battery."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    def describe_battery(self):
        self.battery.describe_battery()

# ...existing code...
if __name__ == "__main__":
    my_leaf = ElectricCar('tesla', 'model s', 2019, battery_size=75)
    print(my_leaf.get_descriptive_name())
    my_leaf.describe_battery()
    # upgrade battery and show the result
    my_leaf.battery.upgrade_battery()
    my_leaf.describe_battery()
    


