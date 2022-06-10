class Player:
    def __init__(self):
        self.position = [0]
        self.direction = 0

    # Change the position of the player (delta)
    @direction.setter
    def direction(self, direction):
        if(direction != -1 or direction != 1):
            raise ValueError("Direction must be either -1 or 1")
        self.direction = direction

    # Move the player
    def move(self, direction):
        self.position[0] += direction