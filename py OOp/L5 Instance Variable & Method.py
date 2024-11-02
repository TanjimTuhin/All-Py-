"""Class Object Constructor attributes methods"""
"""By creating parameter"""
class Student:
    def __init__(self,name,id): 
        #name,id ->attribute of student
        self.name = name   #instance variable
        self.id = id       #instance variable
        #print('a student object created')
    def details(self):    #instance method  
        print("Name:",self.name,"ID:",self.id)
        
        
#creating object ==============================
s1 = Student('John',1)
s2 = Student('Alice',2)
s1.id=24
# print(s1.name,s1.id)
s1.details()
s2.details()


# s1.id=33 #variable update 
# print(s1.name,s1.id)
# print(s2.name,s2.id)

# print("s1", s1)
# print("s2", s2)