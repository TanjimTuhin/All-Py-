'''=========== Example 1 ===================================='''

class Employee:
#parameterized constructor
    def __init__ (self, name, no):
        self.id = no #instance variable
        self.name = name #instance variable

#instance method
    def display (self):
        print (self.name, self.id)

emp1=Employee ("John", 11) #instance 1 
emp2=Employee ("David", 12) #instance 2

emp1.display()
emp2.display()

""" ============ Example 2 ===================================="""
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, color, brand):
        # Instance attributes
        self.color = color
        self.brand = brand

# Creating instances of Car
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

print(car1.color)      # Output: Red (instance attribute)
print(car2.color)      # Output: Blue (instance attribute)
print(car1.wheels)     # Output: 4 (class attribute)
print(car2.wheels)     # Output: 4 (class attribute)
