from pyray import RAYWHITE

class Actor():
    def __init__(self, max_x, max_y, font_size):
        self._position = [0, 0]
        self._max_x = max_x
        self._max_y = max_y
        self._symbol = "#"
        self._font_size = font_size
        self._color = RAYWHITE

    def get_x(self):
        """
            Returns the X position of the Actor
        """
        return self._position[0]

    def get_y(self):
        """
            Returns the Y position of the Actor.
        """
        return self._position[1]

    def get_symbol(self):
        return self._symbol

    def get_font_size(self):
        """
            Returns the font size of the Actor.
        """
        return self._font_size

    def get_color(self):
        """
            Returns the color of the Actor.
        """
        return self._color