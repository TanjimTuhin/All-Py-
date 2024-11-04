"""method overloading and showing where is he problem"""
# class my_calculator:
#     def product(self, num1, num2):
#         print(num1* num2)
        
#     def product(self, num1, num2, num3): #method overloadding so previous same method name will not work
#         print(num1* num2* num3)
        
# #creating object=============
# c1= my_calculator()
# c1.product(4,5,6)       #output: 120
# c1.product(4,5)         #will not work for method overloadding

"""by pass method overloading======================"""

class my_calculator:
    def product(self, num1, num2=None, num3=None):
        if num1!=None and num2 !=None and num3!=None:
            print(num1 * num2* num3)
        elif num1!=None and num2 !=None:
            print(num1 * num2)
        else:
            print(num1)
        
#creating object=============
c1= my_calculator()
c1.product(4)
c1.product(4,5)
c1.product(4,5,6)

"""For n number=================================== """

class my_calculator:
    def product(self, *nums):
        sum= 1
        for x in nums:
            sum*= x
        print(sum)
        
#creating object=============
c1= my_calculator()
c1.product(4)
c1.product(4,5)
c1.product(4,5,6)