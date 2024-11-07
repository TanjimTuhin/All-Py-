class Student:
    uni_name="MIST"         #class variable 
    
    def __init__(self, name, id):    #constructor
        self.name = name
        self.__id = id
    
    def details(self):      #instance method
        print (f"Name: {self.name}, ID: {self.__id}",
               f"University: {Student.uni_name} "       #class variable
               )     
    
    @classmethod
    def up_uni_name(cls, u_name):     #class method
        cls.uni_name= u_name
    
    @classmethod
    def from_string(cls, info):
        name, id = info.split('-')
        obj = cls (name, id)
        return obj
        
s1=Student("Yuhan", 22)
s2=Student("Madara", 58)
s3=Student.from_string("Uchina-24")

s2.details()
s3.details()
#print(Student.from_string("madara-23"))