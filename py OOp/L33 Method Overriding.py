"""Method Overloading"""
class A:
    def __init__(self):
        print("A's constructor")
    def method1(self):
        #print("Method 1 of A / always study")
        print('olpo study')
    def method2(self):
        print("You will get all my property")

class B(A):
    def __init__(self):
        #print("B's constructor") 
        pass
    def method1(self, num):           #method overriding
        super().method1()
        print("Method 1 of B / always party")
        
b1=B()
b1.method1(45)
b1.method2()
