class Employee:
#parameterized constructor
    def __init__ (self, name, no):
        self.id = no #instance variable
        self.name = name #instance variable

#instance method
    def display (self):
        print (self.name, self.id)

emp1=Employee ("John", 11) #instance 1 
emp2=Employee ("David", 12) #instance 2

emp1.display()
emp2.display()