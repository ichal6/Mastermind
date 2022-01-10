import tkinter as tk

from src.Controllers.ControllerGame import ControllerGame
from src.Models.CheatGame import CheatGame
from src.Models.SecretCode import SecretCode
from src.Views.TkInterView import TkinterView


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mastermind')

        secret_code = SecretCode()
        game = CheatGame(secret_code)
        view = TkinterView(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = ControllerGame(game, view)
        view.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
