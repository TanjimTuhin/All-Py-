class ABC:
    def __init__(self, x, y):
        self.x = x
        self.__y = y             #private variable
    def details(self):
        print(f"X: {self.x}, Y: {self.__y}")
#creating object----------------------------------
a1=ABC(5,6)
a2=ABC(15,17)
print(a1.x)
print(a1.__y)

a1.details()
#accessing private variable---------------------------
#print(a1._ABC__y)  # Output: 6
