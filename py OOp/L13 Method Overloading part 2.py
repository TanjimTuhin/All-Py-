#Method Overloading= multiple method with same name in a class with diferrent variable
class my_calculator:
    def product(self, num1, num2=None, num3=None):
        if num1!=None and num2 !=None and num3!=None:
            print(num1 * num2* num3)
        elif num1!=None and num2 !=None:
            print(num1 * num2)
        else:
            print(num1)

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