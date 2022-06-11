##Used for testing... may change as needed to adjust screen height.
#May also use or change this variable in code to adapt
# Max y value is not needed since the top of the screen is y = 0

import random

#creates the Rock class (PARENT class)
class Rock():
    def __init__(self, max_x):
        #creates the symbol, that will display on screen        
        ## NOT SURE IF THIS IS RIGHT... AM I SUPPOSED TO USE RAYLIB?
        ## OR IS THAT THE JOB OF THE GUI CLASS??
        # You're good! An ASCII character will be displayed by raylib
        #   and it asks the Rock what it's symbol is with .get_symbol()
        self._symbol = "O"

        #sets the speed of the rock along the y-axis of the screen to -1.
        # Will be positive since y = 0 is the top of the screen
        self._speedY = 1
    
        # define amount awarded for a hit
        self._point = -1

        #sets the position of the item to fall from the top of screen
        self._position = [0, 0]
        # Later have a randomized x value: 0 - max screen width
        self._max_x = max_x

        # Will randomly choose one of the fall speeds
        self._speeds = [3, 8, 10, 13, 20, 24, 30, 50]
        self.randomize()

    def get_symbol(self):
        # Returns the symbol to be printed
        return self._symbol

    def randomize(self):
        # Randomizes the x position
        self._position[0] = random.randint(0, self._max_x)
        # Chooses a fall speed from the list values
        self._speedY = random.choice(self._speeds)

    #creates a method that subtracts 1 point from score
    def get_points(self):
        # Returns the point value of the Rock
        # Called when the Rock hits the Player
        return self._point

    # Returns only the x position
    def get_y(self):
        return self._position[1]

    # Returns only the y position
    def get_x(self):
        return self._position[0]

    #keeps track of the location of the item as it falls 
    def fall(self):
        # changes the y position as the item falls
        self._position[1] += self._speedY
        
#creates the Gem class (CHILD class--inherits)
class Gem(Rock): 
    def __init__(self, max_x): 
        super().__init__(max_x)
        #creates the symbol, that will display on screen
        self._symbol = "+"
        # Overwrite the points
        self._point = 5
        
        # No additional methods needed, only values changed with Gem

class Big_Rock(Rock):
    def __init__(self, max_x):
        super().__init__(max_x)
        # Change font size here?

# Testing
if __name__ == "__main__":
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

