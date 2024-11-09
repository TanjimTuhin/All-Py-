"""
Abstract  method- has no body
Concreate method- has name, body and implementation
"""

from abc import ABC, abstractmethod  #ABC-> abstract base class
 
class food(ABC):         #food class inherit from ABC
    @abstractmethod      #decorator
    def taste(self):
        pass             #abstract method has no body

#rule1: We can't create a object of abstract class 
#rule2: We can't instantiate an abstract class

class pizza(food):
    def size(self):
        print ("Large")  
#rule3: As pizza class derived from food class and didn't overwrite 
#       taste method so pizza is now a abstract class
    def taste(self):
        print("Pizza is tasty")  #overwriting taste method


p=pizza()
p.size()
p.taste()