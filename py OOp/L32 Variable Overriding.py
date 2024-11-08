class animal:
                                #parent/super/base class
    def __init__(self, name):
        self.name = name
        self.color='White'
        
    def eat(self):
        print(f'{self.color} {self.name} is eating')

#-------------------------------------------
class Dog(animal):
    def __init__(self, name, color ):
        super().__init__(name)
        self.color=color          #changing color of dog ->> method overriding/ attribute overriding
    
    def bark(self):
        print(f'{self.color} {self.name} is barking')
#-------------------------------------------
class Cat(animal):
    def __init__(self, name):
        super().__init__(name)
    def meww(self):
        print(f'{self.color} {self.name} is mewwing')
#-------------------------------------------
dog = Dog('Rex',  "Brown")
cat = Cat('Whiskers')
#-------------------------------------------
dog.eat()
#-------------------------------------------
dog.bark()
#-------------------------------------------
cat.eat()
#-------------------------------------------
cat.meww()



