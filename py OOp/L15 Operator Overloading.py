# class sum:
#     def __init__(self, x, y):
#         self.num=x + y
# num1=sum(10, 20)
# num2=sum(20, 30)
# print(num1+num2)  #===============Error
# print(num1.num+num2.num)  #===============Error

"""to overload the (+) operator, we need to implement __add__() method in the class"""
class data:
    def __init__(self, x):
        self.x = x
    #adding two object
    def __add__(self, other):
        return self.x + other.x
num1=data(10)   #num1=10 ->integer but num1=data(10)-> data's object
num2=data(20)   #num2->variable
str1=data('CSE')
str2=data('IT')
print(num1+num2) #num1.__add__(num2) #===============Output: 30
print(str1+str2) #str1.__add__(str2) #===============Output:

"""to overload the (>) operator, we need to implement __gt__() method in the class"""

class data:
    def __init__(self, x):
        self.x = x
        #greater than
    def __gt__(self, other):
        if (self.x > other.x):
            return True
        else:
            return False
num1= data(10)     #num1=10 ->integer but num1=data(10)-> data's object
num2= data(20)     #num2=variable

if (num1> num2): #num1.__gt__(num2)
    print("num1 is greater than num2") #===============Output: num1 is greater than num2
else:
    print('num2 is greater than num1')
    #===============Output: num2 is greater than num1

"""to overload the (<) operator, we need to implement __lt__() method in the class"""
class data:
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        if (self.x< other.x):
            return "num1 is less than num2"
        else:
            return "num2 is less than num1"
num1=data(10)
num2=data(20)
print(num1<num2) #num1.__lt__(num2) 

"""to overload the (==) operator, we need to implement __eq__() method in the class"""
class data:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        if (self.x == other.x):
            return "Both are equal"
        else:
            return "not equal"
num1 = data(30)
num2 = data(30)
print(num1==num2) #num1.__eq__(num2) #===============Output:Both are equal
            

            
