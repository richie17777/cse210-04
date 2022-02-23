import os

# import pyray as raylibpy
import pyray as raylib


class game:
    def __init__(self):
        pass

    def start(self):
        # draw the window
        raylib.init_window(800, 450, "Greed Game")
        raylib.set_target_fps(60)

        # writing the main loop to draw and close the window
        while not raylib.window_should_close():
            raylib.begin_drawing()
            raylib.clear_background(raylib.RAYWHITE)
            raylib.draw_text(
                "This is our first window by Richard ):!", 190, 200, 20, raylib.LIGHTGRAY
            )
            raylib.end_drawing()

        raylib.close_window()


if __name__ == "__main__":
    game = game()
    game.start()
