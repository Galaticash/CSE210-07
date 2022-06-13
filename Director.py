from hashlib import new
import random

from GraphicInterface import Window
from player import Player
from RockGem import * # Imports all the types of Rocks and Gems

# The population distribution of the Rocks
ROCK_POP = {"Total": 12, "Big Rocks": 2, "Rocks": 7, "Gems": 3}

# How large the game window is 
#   (also used for generating Rocks)
WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
# How large the characters are 
#   (also used for hitbox math)
FONT_SIZE = 25

class Director:
    """
        The game of Greed.
    """
    def __init__(self):
        self._game_over = False

        # Creates a window of a certain width and height
        self._window_max_x = WINDOW_MAX_X
        self._window_max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE
        self._window = Window(self._window_max_x, self._window_max_y, self._font_size)

        # Creates a Player and places them in the center bottom of the screen
        # The Score and Keyboard_Input classes will be used within the Player class
        self._Player = Player(self._window_max_x, self._window_max_y, self._font_size)
        
        # Given a number of rocks, will create a list of Rock objects
        self._num_rocks = ROCK_POP["Total"]
        self._Rocks = []
        
    def _new_rock(self):
        """
            Creates a new Rock or Gem based on the Rock Population's distribution.
            Adds the new Rock to the Game's list of rocks.
        """
        # Randomly decides if the Rock will be a Gem or a Rock,
        #  given the chance values (ex: 7/10 are Rocks and 3/10 are Gems).
        
        # Now that I think about this more, maybe not the most efficient - makes a list of 12 Rocks but only keeps 1
        #new_rock = random.choices([Rock(self._window_max_x, self._window_max_y, self._font_size),  Big_Rock(self._window_max_x, self._window_max_y, self._font_size), Gem(self._window_max_x, self._window_max_y, self._font_size)], weights=(ROCK_POP["Rocks"], ROCK_POP["Big Rocks"], ROCK_POP["Gems"]))[0]
        
        new_rock = None
        rock_type = random.randint(0, self._num_rocks)
        # Between 0 and "Rocks" num (0 - 7)
        if rock_type < ROCK_POP["Rocks"]:
            new_rock = Rock(self._window_max_x, self._window_max_y, self._font_size)
        # Between "Rocks" num and "Big Rocks" + "Rocks" num (7 - 9)
        elif rock_type < ROCK_POP["Rocks"] + ROCK_POP["Big Rocks"]:
            new_rock =  Big_Rock(self._window_max_x, self._window_max_y, self._font_size)
        # Between "Total" num - "Gems" num (9 - 12)
        else:
            new_rock =  Gem(self._window_max_x, self._window_max_y, self._font_size)
        
        self._Rocks.append(new_rock)

    def _replace_rock(self, rock):
        """
            Removes a Rock and creates a new one.
        """
        # Pops the Rock from the list.
        self._Rocks.pop(self._Rocks.index(rock))
        del rock
        # Creates a new Rock to take its place.
        self._new_rock()

    def _is_player_hit(self, rock):
        """
            Determines if the Player has been hit by a rock
              that is nearing the bottom of the board.
        """
        player_hitbox = True
        
        if player_hitbox:
            # Player's hitbox determines hit
            # player's font size determines hitbox range
            left_x = self._Player.get_x() - self._font_size//2
            right_x = self._Player.get_x() + self._font_size//2
            top_y = self._Player.get_y() - self._font_size//2

            if rock.get_y() > top_y and rock.get_x() > left_x and rock.get_x() < right_x:
                self._Player.hit(rock.get_points())
                return True
            else:
                return False
        # OR Rock's hitbox
        else:
            # Rock's hitbox determines hit - better for big rocks, etc
            left_x = rock.get_x() - self._font_size//2
            right_x = rock.get_x() + self._font_size//2
            bottom_y = rock.get_y() + self._font_size//2

            if self._Player.get_y() < bottom_y and self._Player.get_x() > left_x and self._Player.get_x() < right_x:
                self._Player.hit(rock.get_points())
                return True
            else:
                return False

    def start_game(self):
        """
            Begins the Game of greed, which the Player may play for as long
             as they want. The Player can exit by attempting to move up or down.
        """
        # Given a number of rocks, will create a list of Rock objects
        for rock in range(self._num_rocks):
            self._new_rock()
        # Updates the window for the first time
        self._window.update(self._Player, self._Rocks)

    def update_game(self):
        """
            Updates the game based on Player movement and the falling Rocks. 
        """
        if self._window.should_close():
            self._game_over = True
        else:
            # Sees if the Player has moved, updates position
            self._Player.move()

            # Have each rock fall, and check if they are nearing the bottom
            for rock in self._Rocks:
                rock.fall()

                # If the Rock has hit rock bottom,
                if rock.get_y() > self._window_max_y:
                    # This Rock dissapears and is replaced by a new Rock
                    self._replace_rock(rock)
                # Else if the Rock is near the Player,
                elif rock.get_y() > self._window_max_y - self._font_size:
                    # Check if the Player has been hit by said rock
                    if self._is_player_hit(rock):
                        # Rock dissapears if it hits the Player
                        self._replace_rock(rock)
            
            # Updates the visuals of the game
            self._window.update(self._Player, self._Rocks)

    def get_game_over(self):
        """
            Returns to main/director if the game has finished.
        """
        return self._game_over

    def end_game(self):
        """
            Ends the game by closing the window. Additional things may be added
              like adding a game over animation/screen.
        """
        self._window.close()

if __name__ == "__main__":
    director_test = Director()
    director_test.start_game()
    while not director_test.get_game_over():
        director_test.update_game()    
    director_test.end_game()