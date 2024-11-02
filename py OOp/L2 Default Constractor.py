"""Class Object Constructor attributes methods()"""

class Student:
    def __init__(self):
        print(self)
        print("a student object created")
        

#Creating Object ======================
#variable = class_name()

student1=Student() #created object-> automatically call constractor
student2=Student()
print("s1",student1) #<__main__.Student object at 0x0000021C9
