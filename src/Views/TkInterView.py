from src.Models.SecretCode import SecretCode
from src.Views.View import View
import tkinter as tk


class TkinterView(View, tk.Frame):
    def __init__(self, parent):
        super().__init__()
        tk.Frame.__init__(self, parent)

        # create widgets:
        # labels
        self.guess_code_lbl = tk.Label(self, text='Zgadnij kod:')
        self.guess_code_lbl.grid(row=1, column=0)

        # entries
        self.s_code_var = tk.StringVar()
        self.s_code_ent = tk.Entry(self, textvariable=self.s_code_var, width=4)
        self.s_code_ent.grid(row=2, column=0, sticky=tk.NS)

        # buttons
        self.check_btn = tk.Button(self, text='Sprawdź', command=self.check_button_clicked)
        self.check_btn.grid(row=2, column=1, padx=10)
        self.cheat_btn = tk.Button(self, text='Oszust', command=self.is_cheater)
        self.cheat_btn.grid(row=3, column=0, padx=10, pady=10)
        self.reset_btn = tk.Button(self, text='Reset', command=self.reset)
        self.reset_btn.grid(row=3, column=1, padx=10, pady=10)

        # error
        self.error_lbl = tk.Label(self, text='', foreground='red')
        self.error_lbl.grid(row=2, column=0, sticky=tk.W)

    def answer(self, provide_code: SecretCode, count_correct_number, count_incorrect_position):
        print(f'Wprowadzona liczba: {provide_code}')
        print(f'Liczba cyfr poprawnie wprowadzonych: {count_correct_number}')
        print(f'Liczba cyfr na niepoprawnych pozycjach: {count_incorrect_position}')

    def win(self):
        print('Moje gratulacje! Wygrałeś!')

    def game_over(self):
        print('Niestety nie udało się. Może następnym razem?')

    def check_button_clicked(self):
        if self.controller:
            self.controller.check_from_string(self.s_code_var.get())

    def reset(self):
        self.controller.reset()
        print('Zrestartowano grę')

    def show_error(self, message):
        self.error_lbl['text'] = message
        self.error_lbl['foreground'] = 'red'
        self.error_lbl.after(3000, self.__hide_error)
        self.s_code_ent['foreground'] = 'red'

    def __hide_error(self):
        """
        Hide error
        :return:
        """
        self.error_lbl['text'] = ''

    @staticmethod
    def _View__fair_game_message(secret_code: str):
        print('Tere fere. Wylosowany kod: ' + secret_code)

    @staticmethod
    def _View__cheat_game_message():
        print('Złapałeś/łaś mnie!')
