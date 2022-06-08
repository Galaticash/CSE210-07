##Used for testing... may change as needed to adjust screen height.
#May also use or change this variable in code to adapt
# MAX_SCREEN_HEIGHT = 10

#creates the Rock class (PARENT class)
class Rock():
    def __init__(self):
        #creates the symbol, that will display on screen
        
        ## NOT SURE IF THIS IS RIGHT... AM I SUPPOSED TO USE RAYLIB?
        ## OR IS THAT THE JOB OF THE GUI CLASS??
        self.symbol = "O"

        #sets the speed of the rock along the y-axis of the screen to -1.
        self.speedY = -1
    
        # define amount awarded for a hit
        self.point = 1

        #sets the position of the item to fall from the top of screen
        self.position = MAX_SCREEN_HEIGHT


    #creates a method that subtracts 1 point from score
    def hit(self):
        return -self.point

    #keeps track of the location of the item as it falls 
    def location(self):
        self.position += self.speedY
        
#creates the Gem class (CHILD class--inherits)
class Gem(Rock): 
    def __init__(self): 
        super().__init__()
        #creates the symbol, that will display on screen
        
        ## NOT SURE IF THIS IS RIGHT... AM I SUPPOSED TO USE RAYLIB?
        ## OR IS THAT THE JOB OF THE GUI CLASS??
        self.symbol = "+"

    def hit(self):
        return self.point


#Checks that the Gem class is inheriting the speed of Rock class.
g = Gem()
print(g.speedY)

#Checks that the Rock class has the correct symbol
r = Rock()
print(r.symbol)

#Checks that the Gem class has the correct symbol
print(g.symbol)

#checks that rock hit subtracts 1
print(r.hit())

#checks that gem hit adds 1
print(g.hit())

#checks that the position of the item changes by -1.
print(r.position)
r.location()
print(r.position)

