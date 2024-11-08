"""Multiple Inheritance==================================================================================="""

class A:
    def __init__(self):
        print("__init__ of class A")
    def method1(self):
        print("Method 1 of class A")

class B:
    def __init__(self):
        print("__init__ of class B")
    def method1(self):
        print("Method 1 of class B")
        
class C(A,B):
    def __init__(self):
        #super().__init__()
        #B.__init__(self)
        print("__init__ of class C")
    def method2(self):
        print("Method 1 of class C")
        
c1=C()
#c1.method1()
B.method1(c1)
        