"""Multilevel Inheritance======================"""
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name: {self.name}, ID: {self.id}")
#------------------------------
class CSEStudent(Student):
    def __init__(self, name, id, lab):
        super().__init__(name, id)  #[self.name = name] [self.id = id]
        self.lab = lab
    def cry(self):
        print("CSE Student ",self.name, 
              "is cryin caz of",self.lab,' labs')
#------------------------------
class CSEFresher(CSEStudent):
    def enroll(self):
        print(f"Enrolling {self.name} in CSE-101 course")
#-----------------------------
fresher1 = CSEStudent("John", 123, "Python")
fresher2 = CSEFresher("Armin", 143, "Linux")

fresher1.details()
fresher1.cry()
fresher2.details()
fresher2.enroll()


        