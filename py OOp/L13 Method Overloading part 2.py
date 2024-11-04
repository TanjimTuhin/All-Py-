#Method Overloading = multiple method with same name in a class with diferrent variable

from multipledispatch import dispatch
class my_calculator:
    @dispatch(int)
    def product(self, num1):
        print( num1 )
        
    @dispatch(int, int)
    def product(self, num1, num2):
        print( num1 * num2 )
    
    @dispatch(int, int, int)
    def product(self, num1, num2, num3):
        print(num1 * num2* num3)

    @dispatch(str, str)
    def product(self, num1, num2):
        print( int(num1) * int(num2) )
        
    @dispatch(float, float, float)
    def product(self, num1, num2, num3):
        print(num1 * num2* num3)
        
    @dispatch(str, int)
    def product(self, num1, num2):
        print("eita string ar integer value")
        print( int(num1) *(num2) )
    
            
#creating object=============
c1= my_calculator()
c1.product(4)
c1.product(4,5)
c1.product(4,5,6)
c1.product("4","5") 
c1.product(4.0,3.0,6.3)
c1.product("4",5)