from src.Exceptions.IncorrectSecretCodeError import IncorrectSecretCodeError
from src.Models.RuleGame import GameRule
from src.Models.SecretCode import SecretCode
from src.Views.View import View


class ControllerGame:
    def __init__(self, game_rule: GameRule, view: View):
        self.__game = game_rule
        self.__view = view

    def check(self, possible_code: SecretCode):
        count_correct_positions = self.__game.get_count_correct_position(possible_code)
        count_incorrect_positions = self.__game.get_count_incorrect_position(possible_code)
        is_win = self.__game.check(possible_code)
        self.__view.answer(possible_code, count_correct_positions, count_incorrect_positions)
        if is_win:
            self.__view.win()
        if self.__game.attempt_number > self.__game.max_attempt():
            self.__view.game_over()

    @staticmethod
    def __convert(string):
        list1 = []
        list1[:0] = string
        return list1

    def check_from_string(self, secret_code_raw):
        code_list = ControllerGame.__convert(secret_code_raw)
        if len(code_list) != 4:
            raise IncorrectSecretCodeError("Wrong size of code")
        code_dict = dict()
        try:
            for key in range(0, 4):
                code_dict[key] = int(code_list[key])
        except IndexError:
            raise IncorrectSecretCodeError("Too short code")
        except ValueError:
            raise IncorrectSecretCodeError("Not an integer number in code")

        possible_secret_code = SecretCode(code_dict)

        self.check(possible_secret_code)
