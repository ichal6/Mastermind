import tkinter as tk
import random

from src.Controllers.ControllerGame import ControllerGame
from src.Models.CheatGame import CheatGame
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from src.Views.TkInterView import TkinterView

WIDTH = 550
HEIGHT = 620


class App(tk.Tk):
    """
    A class for display main window of app
    """
    def __init__(self):
        """
        Set title, generate code to guess, random game rule, set up TkInterView
        and set a controller
        """
        super().__init__()

        self.title('Mastermind')
        secret_code = SecretCode()
        game_rule = random.choice([CheatGame, FairGame])
        game = game_rule(secret_code)
        view = TkinterView(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = ControllerGame(game, view)
        view.set_controller(controller)


if __name__ == "__main__":
    """
    Run a main program and set size of window and run a mainloop of window
    """
    app = App()

    # set minimum window size value
    app.minsize(WIDTH, HEIGHT)

    # set maximum window size value
    app.maxsize(WIDTH, HEIGHT)
    app.mainloop()
