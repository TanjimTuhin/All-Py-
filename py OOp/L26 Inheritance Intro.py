"""Single Inheritance==========="""

class ParentClass:                 #Base Class
    def method1(self):
        print("Parent method 1")
    def method2(self):
        print("Parent method 2")
        
class ChildClass(ParentClass):     #Derived Class
    def method3(self):
        print("Child method 3")

ch1=ChildClass()                   #object of child class
ch1.method1()             #works caz of method resolution order  
ch1.method2()
ch1.method3()