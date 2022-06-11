
import math
from random import random

from GraphicInterface import WINDOW_MAX_X, WINDOW_MAX_Y, Window
from player_input import KeyboardService
from player import Player
from RockGem import Gem, Rock
from Score import Score
# Game/Director
# Has:
#     Player
#     List of Rock/Gems being generated on the screen
#     GUI/Screen
#     Score
#     *Difficulty - determine the average speed of the falling rocks



CHARACTERS = {"Rock": 'o', "Gem": "*", "Player": "#"}
POINTS = {"Rock": -1, "Gem": 5, "Player": 0}
ROCK_POP = {"Total": 10, "Rocks": 7, "Gems": 3}


WINDOW_MAX_X = 1000
WINDOW_MAX_Y = 400


class Director:

    def __init__(self):
        self._game_over = False
        self._window_max_x = WINDOW_MAX_X
        self._window_max_y = WINDOW_MAX_Y
        self._window = Window(self._window_max_x, self._window_max_y)
        self._KeyboardService = KeyboardService()
        self._Player = Player()
        self._Gem = []
        self._Rock = []
        self._Score = Score()
        self._num_rocks = ROCK_POP["Total"]
        


    def start_game(self):
        for rock in range(10):
            new_rock = (random.choices([]))


    def update_game(self):

    
    def end_game(self):








if __name__ == "__main__":
    director_test = Director()
