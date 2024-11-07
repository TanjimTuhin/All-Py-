"""we can't call private variable or method from outside. 
We have to call from inside class """

class ABC:
    def __init__(self, x, y):
        self.x = x
        self.__y = y             #private variable
    def details(self):
        print(f"X: {self.x}, Y: {self.__y}")
        self.__method()          #calling private method 
    def __method(self):
        print("This is a private method")  #private method
#creating object----------------------------------
a1=ABC(5,6)
a2=ABC(15,17)
print(a1.x)
#print(a1.__y)   -> don't work 
a1.details()
#accessing private variable---------------------------
#print(a1._ABC__y)  # Output: 6

# #calling private method-----------------------
# a1.__method()        #Output: AttributeError: 'ABC' object has no attribute '__method'
