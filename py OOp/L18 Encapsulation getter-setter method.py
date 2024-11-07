"""Getter setter method================="""
class Student:
    def __init__(self, name, id):
        self.name = name     #instance variable
        self.__id = id       #private instance variable
    def display(self):       #instance method
        print("Name:", self.name, "ID:", self.__id)
        
    def set_id(self, id):
        if(id>0):
            self.__id = id
        else:
            print("Invalid ID") 
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.name=name 
    def get_name(self):
        return self.name

#creating an object of Student class
s1=Student("Yuhan",17)
s2=Student("Frankestine",22)
s1.set_id(18)
print(s1.get_id())
s2.set_id(23)
s2.get_id()
print(s2.get_id())

s1.set_name="mike"
print(s1.get_name())

s1.name="Tuhin"             #public variable that's why it work's without calling get set method
print(s1.name)

# print(s1.__id) 
#s1.__id=-66
#print(s1.__dict__)

# s1.updt_id(-66)       #invalid id 
# s1.updt_id(66)        #updated id

s1.display()
s2.display()