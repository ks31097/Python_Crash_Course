class Car():
    """Simple car model"""

    def __init__(self, manufacturer, model, year):
        """Initializing the car attributes"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returning the car information list"""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Displays the vehicle's mileage in miles."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Update car odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Fill gas tank!")

class Battery():
    """Simple model of an electric car battery"""
    def __init__(self, battery_size=75):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Display information about battery power"""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Displays the approximate range of the battery"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")      

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# print(type(my_new_car.get_descriptive_name()))
# my_new_car.read_odometer()
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(1000)
# my_new_car.read_odometer()
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()

class ElectricCar(Car):
    """Represents aspects of the machine specific to electric vehicles"""
    def __init__(self, manufacturer, model, year):
        """Initialize the attributes of the parent class"""
        super().__init__(manufacturer, model, year)
        # self.battery_size = 75
        self.battrery = Battery()

    # def describe_battery(self):
    #     """Displays information about battery"""
    #     print(f"This car has a {self.battery_size}-KWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.battrery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battrery.get_range()
my_tesla.battrery.upgrade_battery()
my_tesla.battrery.get_range()