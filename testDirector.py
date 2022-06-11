from GraphicInterface import FONT_SIZE, Window
from player import Player
from RockGem import *
import random

# Dictionaries of Actor attributes
CHARACTERS = {"Rock": 'O', "Gem": "*", "Player": "#"}
POINTS = {"Rock": -1, "Gem": 5, "Player": 0}
ROCK_POPULATION = {"Total": 10, "Rocks": 7, "Gems": 3}

# Should be the only place with these consts, share with other classes as needed (.get_screensize() or something)
WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600

class Game():
    """
        The game of Greed.
    """
    def __init__(self):
        self._game_over = False
        # Creates a Window given a maximum value for both width and height
        self._window_max_x = WINDOW_MAX_X
        self._window_max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE
        self._window = Window(self._window_max_x, self._window_max_y)
        # Creates a Player for the user to control
        self._player = Player([450, WINDOW_MAX_Y - self._font_size])
        # Gets a number of rocks to create from a constant
        self._num_rocks = ROCK_POPULATION["Total"]
        # Initializes a list of rocks
        self._rocks = []

    def generate_rocks(self):
        """
            Adds Rocks to the empty list of rocks.
        """
        for i in range(self._num_rocks):
            self.new_rock()

    def new_rock(self):
        """
            Creates a new Rock or Gem based on the Rock Population's distribution.
            Randomizes all values for the new Rock, and adds it to the Game's list of rocks.
        """
        new_rock = (random.choices([Rock(self._window_max_x, self._window_max_y), Gem(self._window_max_x, self._window_max_y)], weights=(ROCK_POPULATION["Rocks"], ROCK_POPULATION["Gems"]),))[0]

        # Randomize the position, speed, and color
        new_rock.randomize()
        self._rocks.append(new_rock)
    
    def replace_actor(self, actor):
        """
            Removes a Rock that has hit rock bottom *cymbal crash*
            And adds a new Rock at the top.
        """
        self._rocks.pop(self._rocks.index(actor))
        self.new_rock()

    def start(self):
        """
            Begins the Game of greed, which the Player may play for as long
             as they want. There is no specific end goal yet.
        """
        self.generate_rocks()
        self._window.update(self._player, self._rocks)

    def is_player_hit(self, rock):
        """
            Determines if the Player has been hit by a rock
              that is nearing the bottom of the board.
        """
        # Player's hitbox determines hit
        # player's font size determines hitbox range
        left_x = self._player.get_x() - self._font_size//2
        right_x = self._player.get_x() + self._font_size//2
        top_y = self._player.get_y() - self._font_size//2

        if rock.get_y() > top_y and rock.get_x() > left_x and rock.get_x() < right_x:
            self._player.hit(rock.get_points())
            return True
        else:
            return False
        
        # OR

        # Rock's hitbox determines hit - better for big rocks, etc
        left_x = rock.get_x() - self._font_size//2
        right_x = rock.get_x() + self._font_size//2
        bottom_y = rock.get_y() + self._font_size//2

        if self._player.get_y() < bottom_y and self._player.get_x() > left_x and self._player.get_x() < right_x:
            self._player.hit(rock.get_points())
            return True
        else:
            return False

    def update(self):
        """
            Updates the game based on Player movement and the falling Rocks. 
        """
        self._player.move()

        # Have each rock fall, and check if they are nearing the bottom
        for a in self._rocks:
            a.fall() # [Rock] - needs method to have rock falls
            if a.get_y() > self._window_max_y:
                self.replace_actor(a)
            # If the rock hasn't hit the bottom, but is near the Player
            elif a.get_y() > self._window_max_y - self._font_size:
                if self.is_player_hit(a):
                  self.replace_actor(a)
        
        # Updates the visuals of the game
        self._window.update(self._player, self._rocks)
        
        # A simple exit condition
        if self._player.get_x() > self._window_max_x or self._player.get_x() < 0 or self._player.get_y() > self._window_max_y or self._player.get_y() < 0:
            self._game_over = True

    def get_game_over(self):
        """
            Returns to main/director if the game has finished.
        """
        return self._game_over

    def end(self):
        """
            Ends the game by closing the window. Additional things may be added
              like adding a game over animation/screen.
        """
        self._window.close()

if __name__ == "__main__":
    # Play a game of Greed
    test_game = Game()
    test_game.start()
    while not test_game.get_game_over():
        test_game.update()    
    test_game.end()