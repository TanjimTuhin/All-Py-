"""Hierarchical Inheritance | Method Resolution Order"""

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name: {self.name}, ID: {self.id}")

class CSEStudent(Student):
    def __init__(self, name, id, lab):
        super().__init__(name, id)  #[self.name = name] [self.id = id]
        self.lab = lab
    def cry(self):
        print("CSE Student ",self.name, 
              "is cryin caz of",self.lab,' labs')

class BBAStudent(Student):
    def party(self):
        print('All day party')
        
s1=CSEStudent("Eren", 11, 5)
s2=BBAStudent("Mikasa", 13)
s1.details()
s1.cry()
s2.details()
s2.party()

