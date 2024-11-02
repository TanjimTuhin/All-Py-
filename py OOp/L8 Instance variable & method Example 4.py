'''Dog class design'''
# __dict__ | dir()

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def update_color(self,new_color):
        self.color = new_color 
    
    def poke(self):
        print (f" {self.color} {self.name} is samiling & Age is {self.age} ")

#creating class==================================
dog1=Dog("rover",5,"brown")
dog2=Dog("tommy",4,"white & black")

#method====================================
dog1.poke()
dog1.update_color("blue")
dog1.poke()

dog2.poke()

print(dog1.__dict__) #built in method-> to show attributes value in form of dictionary
print(dir(dog1)) #built in method-> to show all attributes and methods of class in