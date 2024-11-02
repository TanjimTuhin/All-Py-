"""creating class without argument and parameter"""

class House:
    def __init__(self):  #without calling parameter 
        self.window=4   #instance variable
        self.door=2
    def view(self):
        print(f"House has {self.window} windows and {self.door} doors")

#creating object===========================
h1=House()  #has no argument 
h2=House()
#variable update===========================
h1.window=5
h1.door=3 
#accessing attribute==========================
print(h1.window)
print(h2.door)
#calling method==========================
h1.view()
h2.view()
