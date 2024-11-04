class Cat:
    def __init__(self,color,action):
        self.color=color
        self.action=action
    def view(self,num,clr):
        num=num+5
        clr1=clr
        clr1[0]='Green'
        print('Method Inside:',num)
        print('Method Inside',clr1)
    
#creating object=======================
colors=["Black","Yellow","Gray","Brown"]
actions=["Jump","Run","Eat","Sleep"]
#cat1=Cat(colors[0],actions[0])
cat1=Cat("White","jumping")
x=55
cat1.view(x,colors) # [x-> pass by value] [colors->pass by reference]

print('Method outside:',x)
print('Method outide',colors)