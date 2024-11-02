
class Car:
    def __init__(self,name,model):
        self.name=name           #instance variable
        self.model_year=model    #instance variable
        self.wheel=4             #instance variable

    def view(self):              #instance method 
        print("The model year of this",self.model_year,
              "is",self.name)      #accessing instance variable
        print("it is a ",self.wheel, 'wheel car')
#creating object=====================
car1= Car("Toyota",2019)
car2=Car("Audi",2017)
car1.view()
