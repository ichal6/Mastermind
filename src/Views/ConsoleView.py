from src.Models.SecretCode import SecretCode
from src.Views.View import View


class ConsoleView(View):
    def __init__(self):
        super().__init__()

    def answer(self, provide_code: SecretCode, count_correct_number, count_incorrect_position):
        print(f'Wprowadzona liczba: {provide_code}')
        print(f'Liczba cyfr poprawnie wprowadzonych: {count_correct_number}')
        print(f'Liczba cyfr na niepoprawnych pozycjach: {count_incorrect_position}')

    def win(self):
        print('Moje gratulacje! Wygrałeś!')

    def game_over(self):
        print('Niestety nie udało się. Może następnym razem?')

    def check_button_clicked(self, secret_code_str=None):
        secret_code_str = input("Prosze podać kod: ") if secret_code_str is None else secret_code_str
        if self.controller:
            self.controller.check_from_string(secret_code_str)

    @staticmethod
    def _View__fair_game_message(secret_code: str):
        print('Tere fere. Wylosowany kod: ' + secret_code)

    @staticmethod
    def _View__cheat_game_message():
        print('Złapałeś//łaś mnie!')
