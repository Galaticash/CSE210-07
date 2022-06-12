from tkinter import font
import pyray
import random

FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["easy"]

"""
    Requries:
        Does NOT update the position of anything, only displays their current position
        Player, based off of Rock/Actor (all the same base object type)
        Array of Rocks, which holds all falling objects
    
        Rock/Actor base class
            .get_character --> returns the character to print
            .get_x --> x position (0,0 being the top left)
            .get_y --> y position (0,0 being the top left)
            .get_color?? --> could adjust so GUI is in charge of, then only import pyray here?
            .get_font_size --> also can adjust

        Player
            .get_score() --> returns player's current score
"""

class Window():
    """
        A Window which upda a visual representation of the state of the Game.
        __init__() will create the window
        .close() will close the window
        .update(player, rocks) will update the graphical positions of the player and rocks

        get_width() and get_height() for randomizing the locations of the rocks
        all other methods are private (indicated by "_")
    """
    def __init__(self, width, height, font_size):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        pyray.init_window(self._width, self._height, "Greed Game - Team F")
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)
        self._font_size = font_size

        # NOTE: Colors are changing every frame
        self._colors = [pyray.RED, pyray.ORANGE, pyray.YELLOW, pyray.GREEN, pyray.BLUE, pyray.VIOLET]

    def _print_score(self, player):
        """
            Message 1, displays the Player's current score.
        """
        pyray.draw_text(f"Score: {player.get_score()}", 0, 0, int(self._font_size * 2), pyray.RED)

    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_symbol(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def update(self, player, rocks):
        """
            Draws a frame of the Game given the actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        # Updates all the rocks
        for a in rocks:
            self._print_actor(a)
        
        # Updates the player
        self._print_actor(player)

        # Updates the score
        self._print_score(player)

        pyray.end_drawing()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()

