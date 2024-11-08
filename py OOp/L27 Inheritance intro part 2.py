"""Multilevel Inheritance================================================================================"""

class ParentClass:              #Base Class
    def method1(self):
        print("This is method 1 from ParentClass")

class childclass1(ParentClass): #Derived class 1
    def method2(self):
        print("This is method 2 from childclass1")

class childclass2(childclass1): #Derived class 2
    def method3(self):
        print("This is method 3 from childclass2")

ch1 = childclass2()             #Object of childclass 2
ch1.method1()
ch1.method2()
ch1.method3()
    
"""Hierarchical Inheritance============================================================================="""

class ParentClass:              #Base Class
    def method1(self):
        print("This is method 1 from ParentClass")

class childclass1(ParentClass): #Derived class 1
    def method2(self):
        print("This is method 2 from child 1")

class childclass2(ParentClass): #Derived class 2
    def method3(self):
        print("This is method 3 from child 2")

ch1 = childclass1()             #Object of childclass 2
ch2 = childclass2() 

ch1.method1()
ch1.method2()
#ch1.method3()        #This will make error caz method 3 is in another chlid class

ch2.method1()
#ch2.method2()         #This will make error caz method 3 is in another chlid class
ch2.method3()

"""Multiple Inheritance==================================================================================="""

class ParentClass1:              #Base Class 1
    def method1(self):
        print("This is method 1 from ParentClass 1")

class ParentClass2:              #Base class 2
    def method2(self):
        print("This is method 2 from Parentclass 2")

class childclass(ParentClass1, ParentClass2): #Derived class 2
    def method3(self):
        print("This is method 3 from childclass")

ch1 = childclass()             #Object of childclass 2
ch1.method1()
ch1.method2()
ch1.method3()

"""Hybrid Inheritance===================================================================================="""

class ParentClass:              #Base Class
    def method1(self):
        print("This is method 1 from ParentClass")

class childclass1(ParentClass): #Derived class 1
    def method2(self):
        print("This is method 2 from childclass1")

class childclass2(childclass1): #Derived class 2
    def method3(self):
        print("This is method 3 from childclass2")

class childclass3(childclass1): #Derived class 2
    def method4(self):
        print("This is method 4 from childclass3")

ch1 = childclass2()             #Object of childclass 2
ch1.method1()
ch1.method2()
ch1.method3()
#ch1.method4()                #This will make error caz method 4 is in another childclass

"""super()== allowa to call a method of the parent class======================================================"""
class ParentClass:
    def feature1(self):
        print("This is feature 1 from ParentClass")
    def feature2(self):
        print("This is feature 2 from ParentClass")

class childclass(ParentClass):
    def feature3(self):
        super().feature1()           #automatically call feature 1 from parent class 
        print("This is feature 3 from childclass")
        super().feature2()

obj= childclass()
obj.feature3()

"""Method Overloading==allows to define multiple methods with same name but different parameters================="""

class ParentClass:              #Base Class
    def method1(self):
        print("This is method 1 from ParentClass")

class childclass(ParentClass): #Derived class 1
    def method1(self):         #child class overrifing the method of parent class 
        print("This is method 2 from childclass")

ch1=childclass()
ch1.method1()
