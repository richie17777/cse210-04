import os

import pyray as raylib


class game:
    '''
    Draws and closses the window of the greed game
    '''
    def __init__(self):
        pass

    def start(self):
        # draw the window
        raylib.init_window(950, 550, "Greed Game")
        raylib.set_target_fps(70)

        # writing the main loop to draw and close the window
        while not raylib.window_should_close():
            raylib.begin_drawing()
            raylib.clear_background(raylib.RAYWHITE)
            raylib.draw_text(
                "This is our first window by Richard ):", 190, 250, 30, raylib.LIGHTGRAY
            )
            raylib.end_drawing()

        raylib.close_window()


if __name__ == "__main__":
    game = game()
    game.start()
