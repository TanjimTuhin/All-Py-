class Student:
    uni_name="MIST"         #class variable 
    
    def __init__(self, name, id):    #constructor
        self.name = name
        self.__id = id
    
    def details(self):      #instance method
        print (f"Name: {self.name}, ID: {self.__id}",
               f"University: {Student.uni_name} "       #class variable
            #f"University: {self.uni_name}"       #instance variable
               )     
    
    # #trying to change all uni name by instance method
    # def up_uni_name(self, u_name):     #instance method
    #      self.uni_name= u_name
    
    
    #changing all uni name by class method
    @classmethod
    def up_uni_name(cls, u_name):     #class method
        cls.uni_name= u_name
        

#creating object for instance method-------------------------        

s1=Student("Yuhan",23)
s2=Student("Turyo",30)
s1.details()  # Output: Name: Yuhan, ID: 23, University: MIST
s2.details()
#Student.uni_name="Sad"          #changing variable without calling any method
#s1.up_uni_name('qwe')            #calling through instance method-> can't change all uni name at once
Student.up_uni_name('qwe')       #calling through class method
s1.up_uni_name('qwe')            #it will work also caz when s1 is called main class is updated for all
s1.details()  # Output: Name: Yuhan, ID: 23, University: qwe
s2.details()


