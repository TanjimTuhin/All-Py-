class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f'{self.name} is eating')
        
class Dog(Animal):
    def bark(self):
        print(self.name , "is barking")
        
#creating object--------------------------
animal1 = Animal("Platihelmentis")
my_dog  = Dog   ("Buddy")     #at first it find __init__ method known as method resolution order
print(my_dog.name) #Buddy
my_dog.bark()  
my_dog.eat()

animal1.eat()
#animal1.bark()        #AttributeError: 'Animal' object has no attribute 'bark'  