"""Incomplete======================"""

class Student:
    def __init__(self,name, id):
        self.name = name
        self.id = id
class Dummy:
    def __init__(self):
        self.val=0
    def detail(self, std):
        print(std.name)
        print(std.id)
#creating object==============================
s1=Student("yuhan", 11)
d1=Dummy()

# d1.detail(s1.name)      #pass by value 
# d1.detail(s1.id)        #pass by value 

d1.detail(s1)           #pass by reference