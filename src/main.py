import tkinter as tk

from src.Controllers.ControllerGame import ControllerGame
from src.Models.CheatGame import CheatGame
from src.Models.FairGame import FairGame
from src.Models.SecretCode import SecretCode
from src.Views.TkInterView import TkinterView

WIDTH = 550
HEIGHT = 620


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mastermind')
        # TODO Usunąć na produkcji
        secret_code_dict = {0: 5, 1: 4, 2: 3, 3: 4}
        secret_code = SecretCode(secret_code_dict)
        game = FairGame(secret_code)
        view = TkinterView(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = ControllerGame(game, view)
        view.set_controller(controller)


if __name__ == "__main__":
    app = App()

    # set minimum window size value
    app.minsize(WIDTH, HEIGHT)

    # set maximum window size value
    app.maxsize(WIDTH, HEIGHT)
    app.mainloop()
