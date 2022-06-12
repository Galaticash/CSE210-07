import pyray
import random

FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["easy"]
WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
FONT_SIZE = 25

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
    def __init__(self, width = WINDOW_MAX_X, height = WINDOW_MAX_Y):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        pyray.init_window(self._width, self._height, "Greed Game - Team F")
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)
        self._font_size = FONT_SIZE
        # NOTE: Colors are changing every frame
        self._colors = [pyray.RED, pyray.ORANGE, pyray.YELLOW, pyray.GREEN, pyray.BLUE, pyray.VIOLET]

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def _print_num_rocks(self, rocks):
        """
            Message 1, displays how many rocks are falling. For Debug
        """
        pyray.draw_text(f"Falling: {len(rocks)}", 0, 0, int(self._font_size * 2), pyray.RED)

    def _print_score(self, player):
        """
            Message 2, displays the Player's current score.
        """
        pyray.draw_text(f"Score: {player.get_score()}", 0, int(self._font_size * 2), int(self._font_size * 2), pyray.RED)

    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_character(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def _print_rock(self, rock):
        """
            Prints the given rock on the board. All variables used are recieved from the actor itself.
        """
        pyray.draw_text(rock.get_symbol(), rock.get_x(), rock.get_y(), self._font_size, random.choice(self._colors))

    def _print_player(self, player):
        pyray.draw_text("#", player.get_x(), player.get_y(), self._font_size, pyray.RAYWHITE)

    def update(self, player, rocks):
        """
            Draws a frame of the Game given the actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        # Updates all the rocks
        for a in rocks:
            self._print_rock(a)
        
        # Updates the player
        self._print_player(player)

        # Updates the score
        self._print_num_rocks(rocks) # Debugging: Checking that rocks are restocked
        self._print_score(player)

        pyray.end_drawing()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()

