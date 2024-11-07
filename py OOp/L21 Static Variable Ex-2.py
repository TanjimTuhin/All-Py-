"""why we will update static variable only in constructor method"""
class Student:
    counter=0                  #Static variable
    def __init__(self, name, id):
        self.name=name
        self.id=id
        Student.counter+=1    #counter value will increase as many student object created
    def details(self):
        print("Name:", self.name, "Id:", self.id,
              "\ nTotal Student Count:", Student.counter)
        # Student.counter+=1     #counter will be increase how much time it calls
        # print("Total Student not in constructor method:", Student.counter)

s1=Student("Titu", 12)
s2=Student("Motu", 13) 
s3=Student("Yuhan", 15)

s1.details()