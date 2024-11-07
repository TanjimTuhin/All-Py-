"""public and private variable"""
class Student:
    def __init__(self, name, id):
        self.name = name     #instance variable
        self.__id = id       #private instance variable
    def display(self):
        print("Name:", self.name, "ID:", self.__id)
    def updt_id(self, id):
        if(id>0):
            self.__id = id
        else:
            print("Invalid ID") 

#creating an object of Student class
s1=Student("Yuhan",17)
s2=Student("Frankestine",22)

#print(s1.__id) 
#s1.__id=-66
#print(s1.__dict__)

s1.updt_id(-66)       #invalid id 
s1.updt_id(66)        #updated id


s1.display()
s2.display()

"""
Encapsulation is a fundamental concept in object-oriented programming (OOP) that restricts access to certain parts of an object and ensures that its internal representation (data) is hidden from the outside. In Python, encapsulation is implemented using classes, and access to certain variables and methods can be controlled with access modifiers.

#Public Attributes and Methods: These are accessible from outside the class. By default, all class members in Python are public.
==============================
class Car:
    def __init__(self, model):
        self.model = model   # Public attribute
    
    def display_model(self):  # Public method
        print(f"The model of the car is {self.model}")

my_car = Car("Toyota")
print(my_car.model)         # Accessing public attribute
my_car.display_model()       # Accessing public method

#Protected Attributes and Methods: These are intended for use within the class and its subclasses. They are indicated by a single underscore (_attribute). This is more of a convention than a strict rule, as they can still be accessed outside the class, but it signals that they shouldn’t be accessed directly.
=================================
class Car:
    def __init__(self, model, year):
        self._year = year     # Protected attribute
        self.model = model

    def _display_year(self):  # Protected method
        print(f"The year of the car is {self._year}")

my_car = Car("Toyota", 2020)
print(my_car._year)           # Can access, but discouraged
my_car._display_year()         # Can call, but discouraged

#Private Attributes and Methods: These are meant to be hidden from outside the class and are indicated by a double underscore (__attribute). Python uses name mangling to make it harder (but not impossible) to access these from outside the class.
===============================
class Car:
    def __init__(self, model, year, price):
        self.model = model
        self._year = year
        self.__price = price   # Private attribute

    def __display_price(self): # Private method
        print(f"The price of the car is ${self.__price}")

my_car = Car("Toyota", 2020, 30000)

# Trying to access private attribute or method directly will raise an error
# print(my_car.__price)       # AttributeError
# my_car.__display_price()    # AttributeError

# However, they can be accessed using name mangling (not recommended)
print(my_car._Car__price)      # Accessing private attribute (not recommended)
my_car._Car__display_price()   # Calling private method (not recommended)

"""