class Cat:
    def __init__(self,color,action):
        self.color=color
        self.action=action
    def view(self):
        print("This is a", self.color, "cat who is", self.action)    
    def compare(self, ct):
        if self.action == ct.action:  #pass by reference
            print("Both cats are", self.action)
        else:
            print("They are different")
#creating object=======================
cat1=Cat("brown","jumping")
cat2=Cat("Gray","sitting")

cat1.view()
cat2.view()

cat1.compare(cat2)