"""Instance Method: Requires an instance (self). 
Used to access or modify instance-level data.
============================================="""
class Dog:
    def __init__(self, name): #constructor
        self.name = name  # Instance variable
        print(f"Dog named {self.name} is created.")

    def bark(self):  # Instance method
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())   #calling bark with the reference of my_dog obj
# Output: Buddy says woof!

"""Class Method: Requires a class (cls). 
Used to access or modify class-level data or create new instances.
============================================="""
class Dog:
    species = "Canis lupus familiaris"  # Class variable

    @classmethod
    def get_species(cls):  # Class method
        return cls.species

print(Dog.get_species())  # Output: Canis lupus familiaris


"""Static Method: Doesn’t require self or cls. 
Used for utility functions that don’t modify the instance or class.
============================================="""
class Dog:
    @staticmethod
    def bark_sound():  # Static method
        return "Woof!"

print(Dog.bark_sound())  # Output: Woof!

"""Methods==================================="""
class MyClass:
    def method (self):
        print(self,"instance method called")
    @classmethod
    def class_method(cls):
        print(cls,"class method called")
    @staticmethod
    def static_method():
        print("static method called")
