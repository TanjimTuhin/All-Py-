class Student:
    uni_name="MIST"         #class variable 
    
    def __init__(self, name, id):    #constructor
        self.name = name
        self.__id = id
    
    def details(self):      #instance method
        print (f"Name: {self.name}, ID: {self.__id}",
               f"University: {Student.uni_name} "       #class variable
               )     
    
    @classmethod                  #Decorator 
    def up_uni_name(cls, u_name):     #class method
        cls.uni_name= u_name
    
    @staticmethod
    def check_dept( id ):
        if   id[4:7]=='140': print("CSE")
        elif id[4:7]=='160': print("EEE")
        
        
s1=Student("Yuhan", 202014032)
s2=Student("Madara", 202016058)

s2.details()    #object_name.class_name()-> parentheses
s1.details() 

Student.check_dept("202016058")
