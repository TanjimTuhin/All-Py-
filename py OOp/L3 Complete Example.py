"""class object attribute method constructor argument parameter instance_variable"""

class Car:
    # This is the initializer method where we define the attributes of the Car class.
    # Constructor method
    def __init__(self, make, model, year, color): #make,model,year,color -> parameter
        # Attributes of the Car class
        self.make = make    # Car's brand #instance variable
        self.model = model  # Car's model
        self.year = year    # Year of manufacture
        self.color = color  # Car color

    # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model} in {self.color}")

    # Method to change the car's color; it takes 'new_color' as a parameter
    def change_color(self, new_color): #new_color-> parameter
        self.color = new_color
        print(f"Car color changed to {self.color}")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020, "Red")

# Accessing attributes
print(f"My car's make: {my_car.make}")
print(f"My car's model: {my_car.model}")

# Calling methods
my_car.display_info()      # Shows initial car information
my_car.change_color("Blue")  # Changes the car's color "Blue"->argument
my_car.display_info()      # Shows updated car information


# Attributes: (make),(model), (year), and (color) are attributes of the [Car] class, representing properties of a car.
# Parameters: The [__init__] method takes (make), (model), (year), and (color) as parameters to initialize each [Car] instance.
# Methods:(display_info) displays the car's information.
# (change_color) is a method that takes a new_color parameter to change the car's color.
# Argument: call my_car.change_color("Blue"), "Blue" is the argument for the new_color parameter.