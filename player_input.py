#borrowed from RFK and simplified#
import pyray

class KeyboardService:

    def get_direction(self):
        dx = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            raise EOFError("Game over, invalid input")
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            raise EOFError("Game over, invalid input")
        
        return dx