"""Class Object Constructor attributes"""
class Student:
    def __init__(self,name,id):
        self.name = name   #instance variable
        self.id = id       #instance variable
        #print('a student object created')

#creating object ==============================
s1 = Student('John',1)
s2 = Student('Alice',2)
print(s1.name,s1.id)

s1.id=33 #variable update 
print(s1.name,s1.id)
print(s2.name,s2.id)

# print("s1", s1)
# print("s2", s2)


        