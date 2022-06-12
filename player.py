from Score import Score
from player_input import KeyboardService

STEP_SIZE = 5

class Player:
    def __init__(self, position):
        self._position = position
        self._direction = 0
        self._keyboard =  KeyboardService()
        self._score = Score()
        self._step_size = STEP_SIZE

    def get_direction(self):
        return self.direction

    # Change the position of the player (delta)
    #@direction.setter
    def set_direction(self, direction):
        if(direction != -1 or direction != 1):
            raise ValueError("Direction must be either -1 or 1")
        self.direction = direction

    def get_x(self):
        return self._position[0]

    def get_y(self):
        return self._position[1]

    def hit(self, points):        
        self._score.add_score(points)

    def get_score(self):
        return self._score.get_score()

    # Move the player
    def move(self):
        direction = self._keyboard.get_direction()
        self._position[0] += direction * self._step_size