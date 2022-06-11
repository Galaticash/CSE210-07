

class Score():
    def __init__(self):
        self._score = 0

    # score getter
    def get_score(self):
        return self._score

    # increments score based on value of object hit
    def add_score(self, points):
        self._score += points