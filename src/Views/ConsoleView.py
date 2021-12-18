from src.Models.SecretCode import SecretCode
from src.Views.View import View


class ConsoleView(View):
    def __init__(self):
        super().__init__()

    def answer(self, provide_code: SecretCode, count_correct_number, count_incorrect_position):
        print(f'Liczba: {provide_code}')
        print(f'Liczba cyfr poprawnie wprowadzonych: {count_correct_number}')
        print(f'Liczba cyfr na niepoprawnych pozycjach: {count_incorrect_position}')
