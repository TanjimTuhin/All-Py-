# n1= 15
# n2= 25
# print(n1+n2)
# print(type(n1))       #n1,n2 is the object of int class
# print(n1.__add__(n2)) #actually this happens when we write print(n1+n2)

"""Example 1 ======================================"""
# class data:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, other):   #other-> pass by reference
#         return self.x + other.x
    
# num1=data(10)   #num1=10 ->integer but num1=data(10)-> data's object
# num2=data(20)   #num2->variable
# str1=data('CSE')
# str2=data('IT')
# print(num1+num2) #num1.__add__(num2) #===============Output: 30
# print(str1+str2) #str1.__add__(str2) #===============Output: CSEIT


"""Example 2======================================="""
class House:
    def __init__(self, w , d):
        self.window=w
        self.door=d
    def view(self):
        print("The house has", self.window,
              "windows and", self.door, "doors")
    def __add__(self,other):
        new_window=self.window + other.window
        new_door  =self.door   + other.door
        obj=House(new_window,new_door)   #creating new object of new_house
        return obj
        return "New house has "+str(new_window)+ " windows and "+str(new_door)+ " doors "
h1=House(6,2)
h2=House(4,1)
h1.view() 
h2.view()
print(h1+h2) #h1.__add__(h2)
h3=h1+h2
h3.view()
