class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(self)
    def __str__(self):                #location name over write
        return "my name is " + self.name
    
        
s1=Student("Yuhan",12)
s2=Student("Yagar",14)

# print(s1)   #s1.__str__() ->inside print statement
# print(s2)        
# print(s1.__str__())
