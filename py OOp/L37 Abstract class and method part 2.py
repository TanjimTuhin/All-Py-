from abc import ABC, abstractmethod

class Animal(ABC):            #abstract class
    @abstractmethod
    def sound(self):          #abstract method
        pass
    def eat(self):            #concreate method
        print("Eating...")

class Dog(Animal):            #concreate class
    def sound(self):
        print("Barking...")

class Cat(Animal):            #concreate class
    def sound(self):
        print("Meowwing...")

class Snake(Animal):            #concreate class
    def sound(self):
        print("Hissssh...")


d1=Dog()
d1.sound()
d1.eat()                                  

c1=Cat()
c1.sound()
c1.eat()

s1=Snake()
s1.eat()
s1.sound()
