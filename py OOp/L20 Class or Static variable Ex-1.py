class Player:
    team_run=0             #Static / Class variable
    def __init__(self, run):
        self.run = run            # instance variable/ instance attribute
     
    def hit_four(self):           # instance method
        self.run+=4
        Player.team_run+=4        # class reference
        #print(f"Player {self.run} hits a four")
    
    def hit_six(self):
        self.run+=6 
        Player.team_run+=6
        #print(f"Player {self.run} hits a Six!")
        
#creating object-------------------------------
print(Player.team_run)
sakib=Player(0)
tamim=Player(0)
tamim.hit_four()
tamim.hit_four()
sakib.hit_six()
print("Sakib:",sakib.run)
print("Tamim:",tamim.run)
print("Team Run:",Player.team_run)


# print("Tamim",tamim.__dict__)
# print("sakib",sakib.__dict__)    #instance variable is just one(1)-> [self.run]