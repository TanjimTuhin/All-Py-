#inheritance-> is a relationship between a subclass and its superclass.
#Composition -> Has-A relationship between a class and its member objects.


class Engine:
    def __init__(self, cc):
        self.capacity=cc
    def start(self):
        print("The engine is started")
    def stop(self):
        print("The engine is stopped")
        
#class Car(Engine):     -> Car is a Engine   
class Car:       
    def __init__(self, name, cc):
        self.engine= Engine(cc)      #create a obj of engine class with pass cc
        self.name=name   
    def run(self):
        self.engine.start()           #[self.engine]->object has access the Engine class
        print("car is running")
        
car1=Car("BMW", 2000)
car1.run()
    
    
    
    
    
    
    